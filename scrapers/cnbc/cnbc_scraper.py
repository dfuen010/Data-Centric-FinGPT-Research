import http.client

conn = http.client.HTTPSConnection("cnbc.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "4d6d8e080bmsh68dcf84f504154ap1335bbjsn0a70ea825650",
    'X-RapidAPI-Host': "cnbc.p.rapidapi.com"
}

conn.request("GET", "/symbols/get-earnings-chart?issueId=36276&numberOfYears=3", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))