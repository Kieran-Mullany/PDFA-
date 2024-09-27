import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()

#checked output from url in browser to see structure
print(data['bpi']['EUR']['rate_float'])