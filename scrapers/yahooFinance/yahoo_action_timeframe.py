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

# Define start and end dates for the time frame
start_date = '2022-01-01'
end_date = '2022-12-31'

# Iterate over each stock symbol
for symbol in stock_symbols:
    # Use custom session with Ticker constructor
    ticker = yf.Ticker(symbol, session=session)

    # Fetch actions data for the specified time frame
    ticker_actions = ticker.actions

    # Filter actions data for the specified time frame
    ticker_actions_filtered = ticker_actions[(ticker_actions.index >= start_date) & (ticker_actions.index <= end_date)]

    # Save the filtered actions data to a CSV file
    ticker_actions_filtered.to_csv(f'{symbol}_actions_data_{start_date}_{end_date}.csv')
