# import requests
# from crewai.tools import BaseTool
# from pydantic import BaseModel, Field
# import os
# from dotenv import load_dotenv
# from typing import Type

# # Load environment variables
# load_dotenv()
# API_KEY = os.getenv("WEATHERAPI_KEY")  # Ensure this is set in your .env file

# class WeatherToolInput(BaseModel):
#     city: str = Field(..., description="City to fetch weather forecast for (e.g., 'Mumbai').")

# class WeatherForecastTool(BaseTool):
#     name: str = "Weather Forecast Fetcher"
#     description: str = "Fetches 14-day weather forecast (temperature, humidity, rainfall) for a given city."
#     args_schema: Type[BaseModel] = WeatherToolInput  # Explicitly annotating with Type[BaseModel]

#     def _run(self, city: str) -> dict:
#         if not API_KEY:
#             return {"error": "API key is missing. Please set WEATHERAPI_KEY in environment variables."}

#         url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=14"
#         response = requests.get(url).json()

#         if "error" in response:
#             return {"error": response["error"]["message"]}

#         forecast_data = [
#             {
#                 "date": day["date"],
#                 "temperature": day["day"]["avgtemp_c"],
#                 "rainfall": day["day"].get("totalprecip_mm", 0),
#                 "humidity": day["day"]["avghumidity"]
#             }
#             for day in response["forecast"]["forecastday"]
#         ]

#         return {"city": city, "forecast": forecast_data}

# # Test the script
# if __name__ == "__main__":
#     tool = WeatherForecastTool()
#     city_input = WeatherToolInput(city=input("Enter city name: "))  # User enters the city
#     result = tool._run(city=city_input.city)

#     print(f"\n14-Day Weather Forecast for {result.get('city', 'Unknown')}:")
#     for day in result.get("forecast", []):
#         print(f"- {day['date']}: {day['temperature']}°C, Rainfall: {day['rainfall']} mm, Humidity: {day['humidity']}%")




# from crewai.tools import BaseTool
# from pydantic import BaseModel, Field
# from typing import Type
# import os
# import serpapi
# from dotenv import load_dotenv

# load_dotenv()


# api_key = os.getenv("SERPAPI_API_KEY")
# if not api_key:
#     print("API key not found!")
# else:
#     print("API key loaded successfully.")

# # Input schema
# class TrendScraperInput(BaseModel):
#     city: str = Field(..., description="City to analyze fashion trends for (e.g., 'Mumbai').")

# # Trend Scraper Tool
# class TrendScraperTool(BaseTool):
#     name: str = "Fashion Trend Analyzer"
#     description: str = (
#         "Collects fashion trends from Google Trends and Google Events for a given city."
#     )
#     args_schema: Type[BaseModel] = TrendScraperInput

#     def _run(self, city: str) -> dict:
#         # SerpApi Client initialization with your API key
#         client = serpapi.Client(api_key=os.getenv("SERPAPI_API_KEY"))
        
        
#         # Google Trends Search using SerpApi Client
#         google_trends_results = client.search({
#             'q': f'{city} fashion',  # Search query
#             'engine': 'google',      # Google search engine
#         })
        
#         # Google Events Search using SerpApi Client
#         google_events_results = client.search({
#             'q': f'{city} events',   # Search query
#             'engine': 'google',      # Google search engine
#         })
        
#         # Extracting Google Trends from the results
#         google_trends = google_trends_results.get('organic_results', [])

#         # Extracting Google Events from the results
#         google_events = google_events_results.get('organic_results', [])

#         return {
#             "google_trends": [trend['title'] for trend in google_trends],
#             "google_events": [
#                 {"title": event['title'], "link": event['link']}
#                 for event in google_events
#             ]
#         }

# # Test Script
# if __name__ == "__main__":
#     city_input = TrendScraperInput(city=input("Enter city name: "))
#     tool = TrendScraperTool()
#     trends = tool._run(city=city_input.city)

#     print("\nFashion Trends and Events:")

#     # Google Trends results
#     print("\nGoogle Trends Data:")
#     for trend in trends["google_trends"]:
#         print(f"- {trend}")

#     # Google Events results
#     print("\nGoogle Events Data:")
#     for event in trends["google_events"]:
#         print(f"- {event['title']} - {event['link']}")


# import instaloader
# from crewai.tools import BaseTool
# from pydantic import BaseModel, Field
# from typing import Type

# class InstagramTrendInput(BaseModel):
#     hashtag: str = Field(..., description="Instagram hashtag to analyze trends (e.g., 'fashiontrends2025').")

# class InstagramTrendTool(BaseTool):
#     name: str = "Instagram Hashtag Scraper"
#     description: str = "Scrapes Instagram for trending fashion hashtags."
#     args_schema: Type[BaseModel] = InstagramTrendInput

#     def _run(self, hashtag: str) -> dict:
#         loader = instaloader.Instaloader()
#         posts = loader.get_hashtag_posts(hashtag)

#         trending_posts = []
#         for post in posts:
#             trending_posts.append(post.url)
#             if len(trending_posts) >= 10:  # Limit to 10 trending posts
#                 break

#         return {"hashtag": hashtag, "trending_posts": trending_posts}

# # Test Script
# if __name__ == "__main__":
#     tool = InstagramTrendTool()
#     hashtag_input = InstagramTrendInput(hashtag="fashiontrends2025")
#     result = tool._run(hashtag=hashtag_input.hashtag)

#     print("\nTrending Instagram Posts:")
#     for post in result.get("trending_posts", []):
#         print(f"- {post}")


# from crewai.tools import BaseTool
# from pydantic import BaseModel, Field
# from typing import Type
# import tweepy

# # Input Schema for Hashtag
# class HashtagInput(BaseModel):
#     hashtag: str = Field(..., description="Hashtag to search on Twitter (e.g., 'fashiontrends')")

# # Twitter API Credentials
# API_KEY = "your_api_key"
# API_KEY_SECRET = "your_api_key_secret"
# ACCESS_TOKEN = "your_access_token"
# ACCESS_TOKEN_SECRET = "your_access_token_secret"

# # Authentication function
# def authenticate_twitter():
#     auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#     api = tweepy.API(auth)
#     return api

# # Twitter Search Tool
# class TwitterSearchTool(BaseTool):
#     name: str = "Twitter Search Tool"
#     description: str = "Searches recent tweets for a specific hashtag"
#     args_schema: Type[BaseModel] = HashtagInput

#     def _run(self, hashtag: str) -> dict:
#         # Authenticating to Twitter
#         api = authenticate_twitter()
        
#         # Search for recent tweets with the hashtag
#         tweets = []
#         for tweet in tweepy.Cursor(api.search_tweets, q=f"#{hashtag} -filter:retweets", lang="en").items(10):
#             tweets.append({"user": tweet.user.screen_name, "text": tweet.text})

#         return {"tweets": tweets}

# # Test the tool
# if __name__ == "__main__":
#     hashtag_input = HashtagInput(hashtag=input("Enter hashtag: "))
#     tool = TwitterSearchTool()
#     result = tool._run(hashtag=hashtag_input.hashtag)

#     print("\nTweets for Hashtag:", hashtag_input.hashtag)
#     for tweet in result["tweets"]:
#         print(f"{tweet['user']}: {tweet['text']}")





csv="src/inv/inventory_sample.csv"