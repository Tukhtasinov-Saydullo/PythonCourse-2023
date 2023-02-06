import requests

url = "https://currency-converter-by-api-ninjas.p.rapidapi.com/v1/convertcurrency"

querystring = {"have": "UZS", "want": "EUR", "amount": "500_000_000_000_000"}

headers = {
    "X-RapidAPI-Key": "e6be8593b4msh5eb61692f763b88p1de129jsn6d828596d649",
    "X-RapidAPI-Host": "currency-converter-by-api-ninjas.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
