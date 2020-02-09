import requests

from pprint import pprint

api_key="0f0a1651856c0eadb52a9ce0b9e95211"
zip_code="87121"
api_url = "https://api.openweathermap.org/data/2.5/weather?zip="+zip_code+",us&appid="+api_key

def fetchfromRequests():
    response = requests.get(api_url)
    data = response.json()

    pprint(response.json())

if __name__ == "__main__":
    fetchfromRequests()
