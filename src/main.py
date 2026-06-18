from extract import extract_weather_data
from transform import transform_weather_data
from load import load_weather_data

LATITUDE = 15.5
LONGITUDE = -90.25


def run_pipeline():

    extract_weather_data(
        latitude=LATITUDE,
        longitude=LONGITUDE
    )

    transform_weather_data()

    load_weather_data()

    print(
        "Pipeline executed successfully."
    )


if __name__ == "__main__":
    run_pipeline()