# API command evidence templates

Replace `<dealer_id>` with a valid ID from the dataset.
```powershell
curl.exe http://127.0.0.1:8000/djangoapp/get_dealers/
curl.exe http://127.0.0.1:8000/djangoapp/get_dealers/Kansas
curl.exe http://127.0.0.1:8000/djangoapp/dealer/<dealer_id>
curl.exe http://127.0.0.1:8000/djangoapp/reviews/dealer/<dealer_id>
curl.exe http://127.0.0.1:8000/djangoapp/get_cars
curl.exe http://127.0.0.1:5050/analyze/Fantastic%20services
```

These are runnable commands, not claimed execution transcripts. Add actual outputs after running the services.
