import streamlit as st
from weather_service import fetch_weather

st.set_page_config(page_title="Weather App", page_icon="🌦️")

st.title("🌤️ Weather Forecast App")
st.write("Real-time weather information")

city = st.text_input("Enter city name")

if st.button("Get Weather"):
    try:
        weather = fetch_weather(city)
        st.success(f"Weather in {weather['city']}")
        st.write(f"🌡️ Temperature: {weather['temp']} °C")
        st.write(f"💧 Humidity: {weather['humidity']} %")
        st.write(f"🌥️ Condition: {weather['description']}")
        st.write(f"🌬️ Wind Speed: {weather['wind_speed']} m/s")
        st.write(f"🤗 Feels Like: {weather['feels_like']} °C")
    except Exception as e:
        st.error(str(e))
