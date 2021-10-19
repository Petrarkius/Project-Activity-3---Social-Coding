import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Kyev, Ukraine"
dest = "Lviv, Ukraine"
key = "woQNSbipD4X6Xf0U12j1hL8zTxE3aYJY"

url = main_api + urllib.parse.urlencode({
    "key": key,
    "from": orig,
    "to": dest
})

json_data = requests.get(url).json()

print(json_data)