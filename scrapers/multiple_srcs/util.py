import pandas as pd
from openpyxl import load_workbook

def get_years():
    return [str(year) for year in range(2019, 2026)]

def get_col_names():
    col_names = ['Ticker', 'Name', 'Market Cap', 'Sector', 'Business Summary', 
                 'Industry', 'Shares Outstanding', 'Institution Ownership', 'Current Price', 
                 '52-Week High', '52-Week Low', 'Enterprise Value', 'Beta', 
                 'Weekly Price Change %', 'Monthly Price Change %', 'Quarterly Price Change %', 
                 'Half-Yearly Price Change %', 'Yearly Price Change %', 'YTD Price Change %', 
                 '2019 Revenues', '2020 Revenues', '2021 Revenues', '2022 Revenues', 
                 '2023 Revenues', '2024 Revenues', '2025 Revenues', '2019 Net Income', 
                 '2020 Net Income', '2021 Net Income', '2022 Net Income', '2023 Net Income', '2024 Net Income', 
                 '2025 Net Income', '2019 EBITDA', '2020 EBITDA', '2021 EBITDA', '2022 EBITDA', 
                 '2023 EBITDA', '2024 EBITDA', '2025 EBITDA', '2019 EBIT', '2020 EBIT', 
                 '2021 EBIT', '2022 EBIT', '2023 EBIT', '2024 EBIT', '2025 EBIT', 'Currency', 'Unit']

    return col_names