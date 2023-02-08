import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.currencyapi.com/v3/latest?apikey=W7yaHgkA9a4I08IKNQrYV9HXBFNE1FO3xcGaHguN"

resp = requests.get(url)

print(resp.text)
