class FinNews:
    def __init__(self):
        pass

    def get_cnbc_news(self, topics=None):
        return CNBC(topics=topics).get_news()

    def get_seeking_alpha_news(self, topics=None, save_feeds=False):
        return SeekingAlpha(topics=topics, save_feeds=save_feeds).get_news()

    def get_wsj_news(self, topics=None, save_feeds=False):
        return WSJ(topics=topics, save_feeds=save_feeds).get_news()

    def get_yahoo_news(self, topics=None):
        yahoo_feed = Yahoo(topics=topics)
        yahoo_feed.add_topics(['$DIS', '$GOOG'])  # Example of adding tickers manually
        return yahoo_feed.get_news()

    def get_reddit_news(self, topics=None):
        return Reddit(topics=topics).get_news()

    def get_investing_news(self, topics=None, save_feeds=False):
        return Investing(topics=topics, save_feeds=save_feeds).get_news()

    @staticmethod
    def get_supported_feeds():
        supported_feeds = {
            'CNBC': 'CNBC',
            'SeekingAlpha': 'Seeking Alpha',
            'WSJ': 'Wall Street Journal',
            'Yahoo': 'Yahoo Finance',
            'Reddit': 'Reddit',
            'Investing': 'Investing.com',
            # Add more supported feeds here
        }
        return supported_feeds


# Now, you can use the `FinNews` class to fetch news from different sources easily.
fin_news = FinNews()

# Fetch news from CNBC
cnbc_feed = fin_news.get_cnbc_news(topics=['finance', 'earnings'])
print(cnbc_feed)

# Fetch news from Seeking Alpha
seeking_alpha_feed = fin_news.get_seeking_alpha_news(topics=['financial', '$AAPL'], save_feeds=True)
print(seeking_alpha_feed)

# Fetch news from Yahoo Finance
yahoo_feed = fin_news.get_yahoo_news(topics=['*'])
print(yahoo_feed)

# Fetch news from Reddit
reddit_feed = fin_news.get_reddit_news(topics=['$finance', '$news'])
print(reddit_feed)

# Fetch news from Investing.com
investing_feed = fin_news.get_investing_news(topics=['*'], save_feeds=True)
print(investing_feed)

# Get list of supported feeds
supported_feeds = FinNews.get_supported_feeds()
print("Supported Feeds:")
for key, value in supported_feeds.items():
    print(f"{key}: {value}")
