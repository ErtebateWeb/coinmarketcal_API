import requests
import config
url = "https://developers.coinmarketcal.com/v1/events"
querystring = {"max":"10","coins":"kava"}
payload = ""
headers = {
    'x-api-key': config.key,
    'Accept-Encoding': "deflate, gzip",
    'Accept': "application/json"
}
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
print(response.text) 
