import pandas as pd

def get_years():
    return [str(year) for year in range(2019, 2026)]

def get_col_names():
    col_names = [
    "Ticker",
    "Name",
    "Market Cap",
    "Sector",
    "Business Summary",
    "Industry",
    "Shares Outstanding",
    "Institution Ownership",
    "Current Price",
    "52-Week High",
    "52-Week Low",
    "Enterprise Value",
    "Beta",
    "Weekly Price Change %",
    "Monthly Price Change %",
    "Quarterly Price Change %",
    "Half-Yearly Price Change %",
    "Yearly Price Change %",
    "YTD Price Change %",
    ]
    return col_names