import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print(type(data))
print(data)


# Had to pip3 install requests
# Also updated pip3 with cmd >python.exe -m pip install --upgrade pip