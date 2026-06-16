import requests
import json

print("Starting request...")

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=40.71"
    "&longitude=-74.01"
    "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)

response = requests.get(url, timeout=10)

print(f"Status code: {response.status_code}")

data = response.json()

print("JSON received")

with open("data/raw/weather_raw.json", "w") as file:
    json.dump(data, file, indent=4)

print("File saved")