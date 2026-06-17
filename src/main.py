from extract import extract_weather_data
from transform import transform_weather_data

# For Guatemala
LATITUDE = 15.5
LONGITUDE = -90.25

raw_data = extract_weather_data(
    latitude=LATITUDE,
    longitude=LONGITUDE
)

if raw_data:
    processed_data = transform_weather_data()

    print("Pipeline executed successfully.")