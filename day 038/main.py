import requests
import datetime as dt

APP_ID = "20f27c29"
API_KEY = "2e7d379041ba633223f0aec760116477"

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 172
AGE = 37

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

#Bearer Token Authentication
bearer_headers = {
    "Authorization": "Bearer **********"
}


nutri_exercice_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


text = input("Which exercise you did today?: ")

excercise_params = {
    "query": text,
    "gender": "male",
    "weight_kg": 72,
    "height_cm": 160,
    "age": 21
}
response = requests.post(url=nutri_exercice_endpoint, json=excercise_params, headers=exercise_headers)
result = response.json()

#print(result)

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet1 = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "Excercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

#print(sheet1)
sheet_response = requests.post(url="https://api.sheety.co/aa6e900f6d8ba249bf400e256f987ac2/myWorkouts/sheet1", json=sheet1, headers=bearer_headers)
print(sheet_response.text)
