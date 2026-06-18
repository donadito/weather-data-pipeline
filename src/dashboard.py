import streamlit as st
import pandas as pd

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://weather_user:weather_password@localhost:5432/weather_db"
)

query = """
SELECT *
FROM weather_observations
ORDER BY observation_time DESC
"""

df = pd.read_sql(query, engine)

st.title("José Donado: Weather Data Dashboard")

st.dataframe(df)

latest = df.iloc[0]

st.metric(
    "Temperature (°C)",
    latest["temperature_celsius"]
)

st.metric(
    "Humidity (%)",
    latest["humidity_percent"]
)

st.metric(
    "Wind Speed (km/h)",
    latest["wind_speed_kmh"]
)

st.line_chart(
    df.set_index("observation_time")
      ["temperature_celsius"]
)

st.line_chart(
    df.set_index("observation_time")
      ["humidity_percent"]
)

st.line_chart(
    df.set_index("observation_time")
      ["wind_speed_kmh"]
)

st.subheader("Statistics")

st.write(
    df["temperature_celsius"].describe()
)


st.metric(
    "Max Temperature",
    df["temperature_celsius"].max()
)

st.metric(
    "Min Temperature",
    df["temperature_celsius"].min()
)

st.metric(
    "Average Temperature",
    round(
        df["temperature_celsius"].mean(),
        2
    )
)