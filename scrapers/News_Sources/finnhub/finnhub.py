import finnhub

# Setup client
finnhub_client = finnhub.Client(api_key="coju591r01qq4pku84bgcoju591r01qq4pku84c0")

# # Stock candles
# res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
# print(res)

# #Convert to Pandas Dataframe
# import pandas as pd
# print(pd.DataFrame(res))

# # Aggregate Indicators
# print(finnhub_client.aggregate_indicator('AAPL', 'D'))

# Basic financials
print(finnhub_client.company_basic_financials('AAPL', 'all'))

# Earnings surprises
print(finnhub_client.company_earnings('TSLA', limit=5))


# Company News
# Need to use _from instead of from to avoid conflict
print(finnhub_client.company_news('AAPL', _from="2020-06-01", to="2020-06-10"))

# Company Peers
print(finnhub_client.company_peers('AAPL'))

# Company Profile 2
print(finnhub_client.company_profile2(symbol='AAPL'))

# Filings
print(finnhub_client.filings(symbol='AAPL', _from="2020-01-01", to="2020-06-11"))


# Financials as reported
print(finnhub_client.financials_reported(symbol='AAPL', freq='annual'))

# Forex exchanges
print(finnhub_client.forex_exchanges())


# Forex symbols
print(finnhub_client.forex_symbols('OANDA'))

# General news
print(finnhub_client.general_news('forex', min_id=0))

# Quote
print(finnhub_client.quote('AAPL'))

# Recommendation trends
print(finnhub_client.recommendation_trends('AAPL'))

# Stock symbols
print(finnhub_client.stock_symbols('US')[0:5])

# Earnings Calendar
print(finnhub_client.earnings_calendar(_from="2020-06-10", to="2020-06-30", symbol="", international=False))

# FDA Calendar
print(finnhub_client.fda_calendar())

# Symbol lookup
print(finnhub_client.symbol_lookup('apple'))

# Insider transactions
print(finnhub_client.stock_insider_transactions('AAPL', '2021-01-01', '2021-03-01'))

# Lobbying
print(finnhub_client.stock_lobbying("AAPL", "2021-01-01", "2022-06-15"))

# USA Spending
print(finnhub_client.stock_usa_spending("LMT", "2021-01-01", "2022-06-15"))

