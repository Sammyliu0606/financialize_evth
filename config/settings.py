import os
from dotenv import load_dotenv

load_dotenv()

# API base URLs
POLYMARKET_EVENTS_URL   = "https://gamma-api.polymarket.com/events"
KALSHI_MARKETS_URL      = "https://api.elections.kalshi.com/trade-api/v2/markets"
KALSHI_HIST_MARKETS_URL = "https://api.elections.kalshi.com/trade-api/v2/historical/markets"
KALSHI_HIST_CUTOFF_URL  = "https://api.elections.kalshi.com/trade-api/v2/historical/cutoff-timestamps"

# Date filters
POLY_START_DATE   = os.getenv("POLY_START_DATE",   "2025-01-01T00:00:00Z")
KALSHI_START_DATE = os.getenv("KALSHI_START_DATE", "2025-01-01T00:00:00Z")

# Pagination
FETCH_LIMIT = int(os.getenv("FETCH_LIMIT", "50"))

# File paths
DATA_RAW_DIR       = "data/raw"
DATA_PROCESSED_DIR = "data/processed"
DATA_EXPORTS_DIR   = "data/exports"

# Request settings
REQUEST_TIMEOUT_SECONDS = 30
PAGINATION_DELAY_SECONDS = 0.5
