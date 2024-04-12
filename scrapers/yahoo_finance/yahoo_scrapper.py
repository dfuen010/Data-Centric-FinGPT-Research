import yfinance as yf
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter
from requests import Session
import pandas as pd

# Custom requests session with rate limiting
class LimiterSession(LimiterMixin, Session):
    pass

# Configure rate limiter
limiter = Limiter(RequestRate(2, Duration.SECOND * 5))  # max 2 requests per 5 seconds

# Create session
session = LimiterSession(
    limiter=limiter,
    bucket_class=MemoryQueueBucket
)

# Set custom User-Agent header
session.headers['User-agent'] = 'my-program/1.0'

# Define a list of stock symbols
stock_symbols = ['AAPL', 'MSFT', 'GOOGL']

# Iterate over each stock symbol
for symbol in stock_symbols:
    # Use custom session with Ticker constructor
    ticker = yf.Ticker(symbol, session=session)

    # Example: Retrieve actions data
    actions_data = ticker.actions

    # Example: Deal with multi-level columns
    # Assume you have a DataFrame with multi-level columns
    # actions_data is a placeholder for actual data obtained from yfinance
    # actions_data = ticker.actions

    # Flatten multi-level columns
    actions_data.columns = ['_'.join(col).strip() for col in actions_data.columns.values]

    # Example: Saving DataFrame to CSV
    actions_data.to_csv(f'{symbol}_actions_data.csv', index=False)
