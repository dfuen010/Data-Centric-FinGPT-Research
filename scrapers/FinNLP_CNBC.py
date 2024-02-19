import sys
import os

# Change the current working directory to the FinNLP directory to import the CNBC_Streaming class
os.chdir(r'..\FinNLP')
sys.path.append(r'..\FinNLP')

from finnlp.data_sources.news.cnbc_streaming import CNBC_Streaming

# Download the streaming news data
news_downloader = CNBC_Streaming()
news_downloader.download_streaming_search(keyword = "apple stock", rounds = 3)

# Print the first 5 rows of the dataframe
print(news_downloader.dataframe.head())

# Save the dataframe to a csv file
news_downloader.dataframe.to_csv(r'C:\Users\jc219\OneDrive\Desktop\GitHub\Data-Centric-FinGPT-Research\scrapers\apple_news.csv', index = False)