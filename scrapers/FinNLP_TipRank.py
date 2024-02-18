import os
import sys
os.chdir(r"..\FinNLP")
sys.path.append(r"..\FinNLP")
from finnlp.data_sources.news.tipranks_streaming import TipRanks_Streaming

news_downloader = TipRanks_Streaming()
news_downloader.download_streaming_search(keyword = "AAPL", rounds = 3)

news_df = news_downloader.dataframe

print(news_df.head())

news_df.to_csv(r'C:\Users\yit2\Desktop\Github\Data-Centric-FinGPT-Research\scrapers\tip_rankApple.csv', index = False)