import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")
SERPAPI_URL = os.getenv("SERPAPI_URL")
