import json
import logging
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CarMake, CarModel
from .populate import initiate
from .restapis import get_request, analyze_review_sentiments, post_review

logger = logging.getLogger(__name__)

@csrf_exempt
def login_user(request):
    if request.method != "POST":
        return JsonResponse({"error":"POST required"}, status=405)
    try:
        data=json.loads(request.body or b"{}")
        username=data.get("userName","")
        user=authenticate(request, username=username, password=data.get("password",""))
        if user:
            login(request,user)
            return JsonResponse({"userName":username,"status":"Authenticated"})
        return JsonResponse({"userName":username,"status":"Invalid credentials"},status=401)
    except (ValueError, TypeError):
        return JsonResponse({"error":"Invalid JSON"},status=400)

@csrf_exempt
def logout_request(request):
    if request.method not in ("POST","GET"):
        return JsonResponse({"error":"Method not allowed"},status=405)
    logout(request)
    return JsonResponse({"success":True,"message":"Logged out successfully"})

@csrf_exempt
def registration(request):
    if request.method != "POST": return JsonResponse({"error":"POST required"},status=405)
    try: data=json.loads(request.body or b"{}")
    except ValueError: return JsonResponse({"error":"Invalid JSON"},status=400)
    required=("userName","password","firstName","lastName","email")
    if not all(data.get(k) for k in required): return JsonResponse({"error":"All fields are required"},status=400)
    username=data["userName"]
    if User.objects.filter(username=username).exists(): return JsonResponse({"username":username,"error":"Already Registered"},status=409)
    user=User.objects.create_user(username=username,password=data["password"],first_name=data["firstName"],last_name=data["lastName"],email=data["email"])
    login(request,user)
    return JsonResponse({"userName":username,"status":"Authenticated"},status=201)

def get_cars(request):
    if not CarMake.objects.exists(): initiate()
    return JsonResponse({"CarModels":[{"CarModel":m.name,"CarMake":m.car_make.name} for m in CarModel.objects.select_related("car_make")]})

def get_dealerships(request,state="All"):
    endpoint="/fetchDealers" if state=="All" else "/fetchDealers/"+state
    dealers=get_request(endpoint) or []
    return JsonResponse({"status":200,"dealers":dealers})

def get_dealer_reviews(request,dealer_id):
    reviews=get_request(f"/fetchReviews/dealer/{dealer_id}") or []
    for review in reviews:
        result=analyze_review_sentiments(review.get("review","")) or {}
        review["sentiment"]=result.get("sentiment","neutral")
    return JsonResponse({"status":200,"reviews":reviews})

def get_dealer_details(request,dealer_id):
    dealer=get_request(f"/fetchDealer/{dealer_id}")
    if not dealer: return JsonResponse({"status":404,"message":"Dealer not found"},status=404)
    return JsonResponse({"status":200,"dealer":dealer})

@csrf_exempt
def add_review(request):
    if request.method!="POST": return JsonResponse({"error":"POST required"},status=405)
    if not request.user.is_authenticated: return JsonResponse({"status":403,"message":"Unauthorized"},status=403)
    try: data=json.loads(request.body or b"{}")
    except ValueError: return JsonResponse({"error":"Invalid JSON"},status=400)
    data["name"]=request.user.get_full_name() or request.user.username
    result=post_review(data) or {}
    if result.get("status")==500: return JsonResponse({"status":500,"message":"Could not save review"},status=502)
    return JsonResponse({"status":200,"message":"Review posted successfully","review":result})
