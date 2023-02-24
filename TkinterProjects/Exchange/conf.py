import requests
import json

API_EXCHANGE = "e6be8593b4msh5eb61692f763b88p1de129jsn6d828596d649"
url = "https://exchangeratespro.p.rapidapi.com/latest"

headers = {
    "X-RapidAPI-Key": f"{API_EXCHANGE}",
    "X-RapidAPI-Host": "exchangeratespro.p.rapidapi.com"
}


def get_user_request(currency_dt, exchange_to):
    querystring = {"base": f"{currency_dt}", "currencies": f"{exchange_to}"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.text
    parsed_data = json.loads(data)
    rates = parsed_data['rates']
    return rates
