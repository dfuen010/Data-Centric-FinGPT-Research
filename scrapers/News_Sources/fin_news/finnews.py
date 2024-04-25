import FinNews as fn

cnbc_feed = fn.CNBC(topics=['finance', 'earnings'])
print(cnbc_feed.get_news())
print(cnbc_feed.possible_topics())

# Some feeds have support for feeds by ticker, tickers can be passed as a topic and are denoted by $XXX. These feeds will have 'ticker' as a possible topic.
fn.SeekingAlpha(topics=['financial', '$AAPL'], save_feeds=True)

# You can also pass in '*' to select all possible topic feeds.
fn.WSJ(topics=['*'], save_feeds=True)

# Selecting all topics will not add specific ticker feeds. You will have to add tickers manually.
fn.Yahoo(topics=['*']).add_topics(['$DIS', '$GOOG'])

# There is also a Reddit class that allows you to get the rss feed of any subreddit. There are a few feeds established in the package but you can pass through any subreddit like you would a ticker. (r/news = $news)
fn.Reddit(topics=['$finance', '$news'])

# Each topic is converted into a Feed object. "save_feeds" is a boolean to determine if the previous entries in the feed should be saved or overwritten whenever get_news() is called.
fn.Investing(topics=['*'], save_feeds=True)

# Current RSS Feeds:
FinNews.CNBC() # CNBC
FinNews.SeekingAlpha() # Seeking Alpha*
FinNews.Investing() # Investing.com
FinNews.WSJ() # Wall Street Journal
FinNews.Yahoo() # Yahoo Finance*
FinNews.FT() # Finance Times
FinNews.Fortune() # Fortune
FinNews.MarketWatch() # MarketWatch
FinNews.Zacks() # Zacks
FinNews.Nasdaq() # Nasdaq*
FinNews.Reddit() # Reddit
FinNews.CNNMoney() # CNN Money
FinNews.Reuters() # Reuters


# (* denotes ticker feed support)