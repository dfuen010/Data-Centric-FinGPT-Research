import requests

url = "https://cnbc.p.rapidapi.com/symbols/get-earnings-chart"

querystring = {"issueId":"36276","numberOfYears":"3"}

headers = {
	"X-RapidAPI-Key": "4d6d8e080bmsh68dcf84f504154ap1335bbjsn0a70ea825650",
	"X-RapidAPI-Host": "cnbc.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())