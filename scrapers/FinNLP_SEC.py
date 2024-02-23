import json
import os
import sys
import subprocess

os.chdir(r'../../FinNLP')

from finnlp.data_sources.sec_filings import SECFilingsLoader


sec_data = SECFilingsLoader(
    ['AAPL'],1,'10-K',include_amends=True,num_workers=1
)

sec_data.load_data()

with open('data/AAPL/2023/10-K.json', 'r') as f:
  data = json.load(f)

data