from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import os
import serpapi
from dotenv import load_dotenv

load_dotenv()

# Ensure the API key is loaded
api_key = os.getenv("SERPAPI_API_KEY")
if not api_key:
    print("API key not found!")
else:
    print("API key loaded successfully.")

# Input schema for city-based fashion trends analysis
class TrendScraperInput(BaseModel):
    city: str = Field(..., description="City to analyze fashion trends for (e.g., 'New York').")

# Trend Scraper Tool to fetch trends and events for a city
class TrendScraperTool(BaseTool):
    name: str = "Fashion Trend Analyzer"
    description: str = (
        "Collects fashion trends from Google Trends and Google Events for a given city."
    )
    args_schema: Type[BaseModel] = TrendScraperInput

    def _run(self, city: str) -> dict:
        # Initialize SerpApi Client with your API key
        client = serpapi.Client(api_key=api_key)
        
        # Google Trends Search using SerpApi Client
        google_trends_results = client.search({
            'q': f'{city} fashion',  # Search query
            'engine': 'google',      # Google search engine
        })
        
        # Google Events Search using SerpApi Client
        google_events_results = client.search({
            'q': f'{city} events',   # Search query
            'engine': 'google',      # Google search engine
        })
        
        # Extract Google Trends and Google Events data
        google_trends = google_trends_results.get('organic_results', [])
        google_events = google_events_results.get('organic_results', [])

        # Return structured data with trends and events
        return {
            "google_trends": [trend['title'] for trend in google_trends],
            "google_events": [
                {"title": event['title'], "link": event['link']}
                for event in google_events
            ]
        }

