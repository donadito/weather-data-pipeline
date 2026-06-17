import json
import logging 
from datetime import datetime

def transform_weather_data():

    

    try:
        with open("data/raw/weather_raw.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        logging.error("Raw weather file not found.")
        return None


    current = data["current"]

    # normalize time and date
    # timestamp = datetime.fromisoformat(current["time"])

    processed_data = {
        "observation_time": current["time"],
        "temperature_celsius": current["temperature_2m"],
        "humidity_percent": current["relative_humidity_2m"],
        "wind_speed_kmh": current["wind_speed_10m"]
    }


    with open("data/processed/weather_processed.json", "w") as file: #write 
        json.dump(processed_data, file, indent=4)
    
    logging.basicConfig(level=logging.INFO)
    logging.info(
        "Processed weather data successfully."
    )

    return processed_data

if __name__ == "__main__":
    
    result = transform_weather_data()

    print(result)
  


