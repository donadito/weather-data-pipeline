import json

with open("data/raw/weather_raw.json", "r") as file:
    data = json.load(file)
current = data["current"]

processed_data = {
    "observation_time": current["time"],
    "temperature_celsius": current["temperature_2m"],
    "humidity_percent": current["relative_humidity_2m"],
    "wind_speed_kmh": current["wind_speed_10m"]
}

with open("data/processed/weather_processed.json", "w") as file:
    json.dump(processed_data, file, indent=4)