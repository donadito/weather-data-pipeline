import requests
import json

def extract_weather_data(latitude, longitude):
    print("Starting request...")

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

    print(f"Status code: {response.status_code}")

    data = response.json()

    print("JSON received")

    with open("data/raw/weather_raw.json", "w") as file:
        json.dump(data, file, indent=4)

    print("File saved")

    return data

if __name__ == "__main__":
    result = extract_weather_data(15.5, -90.25)
    print(result)