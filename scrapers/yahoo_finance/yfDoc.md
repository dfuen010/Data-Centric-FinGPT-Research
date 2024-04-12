## Documentation on Yahoo Finance GitHub API

1. If using python, in terminal install the following package:

        $ pip install yfinance --upgrade --no-cache-dir

 2. Then you just have to import the library in your python file:

        import yfinance as yf

3. The following are the some commands used to get the company data

        
        company = yf.Ticker("MSFT") // ticker for Microsoft

        company.info // Get Company Info (location, industry, summary, etc)

        hist = company.history(period = "1mo") // get market data from the past month
        // ^ can use "1wk" "1d" "30d" etc

        FOR FINANCIAL INFORMATION

        company.income_stmt // Income Statement
        company.quarterly_income_stmt // Income Statement
        company.balance_sheet // Balance Sheet
        company.cashflow // Cash Flow Statement

        COMPANY HOLDERS
        company.major_holders 
        company.mutualfund_holders


        OPTOINS
        company.options

        NEWS
        company.news





For more commands visit the Yahoo Finance GitHub API:
https://github.com/ranaroussi/yfinance

