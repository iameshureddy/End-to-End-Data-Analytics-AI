"""
weather_tool.py
---------------
LangChain tool to fetch current weather using Open-Meteo API.
"""

import requests
from langchain_core.tools import tool

from config import WEATHER_API_URL
from utils.logger import logger


@tool
def get_weather(latitude: float, longitude: float) -> str:
    """
    Get the current weather for the given latitude and longitude.

    Args:
        latitude: Latitude of the location.
        longitude: Longitude of the location.

    Returns:
        Current weather information as a string.
    """

    try:
        logger.info(
            f"Weather tool called (lat={latitude}, lon={longitude})"
        )

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True,
        }

        response = requests.get(
            WEATHER_API_URL,
            params=params,
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        current = data.get("current_weather")

        if not current:
            return "Weather information not available."

        result = (
            f"Temperature: {current['temperature']}°C\n"
            f"Wind Speed: {current['windspeed']} km/h\n"
            f"Wind Direction: {current['winddirection']}°\n"
            f"Weather Code: {current['weathercode']}"
        )

        logger.info("Weather tool executed successfully.")

        return result

    except Exception as e:
        logger.error(f"Weather tool error: {e}")
        return f"Error fetching weather: {e}"