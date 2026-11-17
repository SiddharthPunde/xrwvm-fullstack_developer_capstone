import json
from pathlib import Path
from .models import CarMake,CarModel

def initiate():
    data_file=Path(__file__).resolve().parents[1]/"database"/"data"/"car_records.json"
    with data_file.open(encoding="utf-8") as f: records=json.load(f).get("cars",[])
    for row in records:
        make,_=CarMake.objects.get_or_create(name=row["make"],defaults={"description":row["make"]+" vehicles"})
        CarModel.objects.get_or_create(car_make=make,name=row["model"],year=row["year"],defaults={"type":row.get("bodyType","SUV").upper()})
