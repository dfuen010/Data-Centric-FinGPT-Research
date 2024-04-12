import requests

url = "https://cnbc.p.rapidapi.com/symbols/translate"

headers = {
	"X-RapidAPI-Key": "4d6d8e080bmsh68dcf84f504154ap1335bbjsn0a70ea825650",
	"X-RapidAPI-Host": "cnbc.p.rapidapi.com"
}

querystring = {"symbol":"TSLA"}

tslaID = requests.get(url, headers=headers, params=querystring)

querystring = {"symbol":"AAPL"}

aaplID = requests.get(url, headers=headers, params=querystring)

querystring = {"symbol":"MSFT"}
msftID = requests.get(url, headers=headers, params=querystring)

print(tslaID.json())
print(aaplID.json())
print(msftID.json())

url = "https://cnbc.p.rapidapi.com/symbols/v2/get-chart"
querystring = {"symbol":"TSLA","interval":"1M"}
response = requests.get(url, headers=headers, params=querystring)

url = "https://cnbc.p.rapidapi.com/symbols/get-summary"
querystring = {"issueIds":"36276,24812378"}
response = requests.get(url, headers=headers, params=querystring)
print(response.json())


# Export the data to a json file
with open("tsla_chart.json", "w") as f:
    f.write(response.text)