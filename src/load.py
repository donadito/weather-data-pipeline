import json
import logging

from sqlalchemy import create_engine
from sqlalchemy import text


def load_weather_data():

    with open(
        "data/processed/weather_processed.json",
        "r"
    ) as file:
        data = json.load(file)

    engine = create_engine(
        "postgresql+psycopg2://weather_user:weather_password@localhost:5432/weather_db"
    )

    query = text("""
        INSERT INTO weather_observations (
            observation_time,
            temperature_celsius,
            humidity_percent,
            wind_speed_kmh
        )
        VALUES (
            :observation_time,
            :temperature_celsius,
            :humidity_percent,
            :wind_speed_kmh
        )
        ON CONFLICT (observation_time)
        DO NOTHING        
    """)

    with engine.connect() as connection:

        connection.execute(
            query,
            data
        )

        connection.commit()

    logging.info(
        "Weather observation inserted successfully."
    )

    return data


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    result = load_weather_data()

    print(result)