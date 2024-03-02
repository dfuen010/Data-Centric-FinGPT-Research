import os
import sys

# Change the current working directory to the FinNLP directory to import the CNBC_Streaming class
os.chdir(r'..\FinNLP')
sys.path.append(r'..\FinNLP')

from finnlp.data_sources.earning_calls import EarningCallTranscripts
loader = EarningCallTranscripts(2023,'AAPL','Q3')
docs = loader.load_data()
print(docs)
