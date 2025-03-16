import requests
import logging
from urllib.parse import urlparse
from config import SERPAPI_KEY, SERPAPI_URL
from database import insert_ranking, check_search_quota, update_search_quota

# Setup logging
logging.basicConfig(filename="logs/serpapi_errors.log", level=logging.ERROR, format="%(asctime)s - %(message)s")

def get_serp_results(keyword):
    """
    Fetches Google SERP results using SerpAPI.
    """
    remaining_searches = check_search_quota()
    if remaining_searches <= 0:
        return {"error": "Monthly SerpAPI search limit reached!"}

    params = {
        "engine": "google",
        "q": keyword,
        "api_key": SERPAPI_KEY
    }

    try:
        response = requests.get(SERPAPI_URL, params=params)
        response.raise_for_status()
        data = response.json()

        for item in data.get("organic_results", []):
            rank = item.get("position")
            title = item.get("title")
            url = item.get("link")
            domain = urlparse(url).netloc
            is_snippet = 1 if "snippet" in item else 0  # Check if it's a featured snippet

            insert_ranking(keyword, rank, title, url, is_snippet)

        update_search_quota()
        return {"success": f"Data for '{keyword}' stored successfully!"}

    except Exception as e:
        logging.error(f"Error fetching SERP results: {e}")
        return {"error": "Request failed. Check logs."}
