import os
import requests
from urllib.parse import quote
from dotenv import load_dotenv
load_dotenv()
backend_url=os.getenv("backend_url","http://localhost:3030").rstrip("/")
sentiment_analyzer_url=os.getenv("sentiment_analyzer_url","http://localhost:5050/").rstrip("/")

def get_request(endpoint,**kwargs):
    try:
        response=requests.get(backend_url+endpoint,params=kwargs,timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return []

def analyze_review_sentiments(text):
    try:
        response=requests.get(sentiment_analyzer_url+"/analyze/"+quote(text,safe=""),timeout=5)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException,ValueError):
        return {"sentiment":"neutral"}

def post_review(data_dict):
    try:
        response=requests.post(backend_url+"/insert_review",json=data_dict,timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return {"status":500,"message":"Backend unavailable"}
