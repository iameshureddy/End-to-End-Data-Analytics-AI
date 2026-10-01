from tools.weather_tool import get_weather

result = get_weather.invoke(
    {
        "latitude": 17.3850,
        "longitude": 78.4867,
    }
)

print(result)