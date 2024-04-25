import os
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
stock_symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'TSLA', 'NVDA', 'JPM', 'V', 'JNJ']

# Define start and end dates for the time frame
start_date = '2022-01-01'
end_date = '2022-12-31'

# Define the folder path where CSV file will be saved
folder_path = 'datasets/News/yahoo_finance'

# Create an empty DataFrame to store the concatenated data
all_actions_data = pd.DataFrame()

# Iterate over each stock symbol
for symbol in stock_symbols:
    # Fetch actions data for the specified time frame
    ticker_actions = yf.Ticker(symbol).actions

    # Filter actions data for the specified time frame
    ticker_actions_filtered = ticker_actions[(ticker_actions.index >= start_date) & (ticker_actions.index <= end_date)]

    # Add a column for the stock symbol
    ticker_actions_filtered['Symbol'] = symbol

    # Concatenate the filtered actions data to the DataFrame
    all_actions_data = pd.concat([all_actions_data, ticker_actions_filtered])

# Save the concatenated actions data to a single CSV file
file_path = os.path.join(folder_path, 'all_companies_actions_data.csv')
all_actions_data.to_csv(file_path, index=True)

# Display additional information about each action taken by the companies
for index, row in all_actions_data.iterrows():
    print(f"Company: {row['Symbol']}")
    print(f"Date: {index}")
    print(f"Action: {row['Dividends'] if pd.notnull(row['Dividends']) else ''} "
          f"{row['Stock Splits'] if pd.notnull(row['Stock Splits']) else ''}")
    print()
