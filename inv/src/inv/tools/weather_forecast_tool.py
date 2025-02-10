import requests
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
from typing import Type

# Load environment variables
load_dotenv()
API_KEY = os.getenv("WEATHERAPI_KEY")  # Ensure this is set in your .env file

class WeatherToolInput(BaseModel):
    """Input schema for Weather Forecast Tool."""
    city: str = Field(..., description="City to fetch weather forecast for (e.g., 'Mumbai').")

class WeatherForecastTool(BaseTool):
    """Fetches 14-day weather forecast (temperature, humidity, rainfall) for a given city."""
    name: str = "Weather Forecast Fetcher"
    description: str = "Fetches 14-day weather forecast (temperature, humidity, rainfall) for a given city."
    args_schema: Type[BaseModel] = WeatherToolInput

    def _run(self, city: str) -> dict:
        if not API_KEY:
            return {"error": "API key is missing. Please set WEATHERAPI_KEY in environment variables."}

        url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=14"
        response = requests.get(url).json()

        if "error" in response:
            return {"error": response["error"]["message"]}

        forecast_data = [
            {
                "date": day["date"],
                "temperature": day["day"]["avgtemp_c"],
                "rainfall": day["day"].get("totalprecip_mm", 0),
                "humidity": day["day"]["avghumidity"]
            }
            for day in response["forecast"]["forecastday"]
        ]

        return {"city": city, "forecast": forecast_data}
