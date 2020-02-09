import requests
import pyowm
import io,json


from pprint import pprint

api_key="0f0a1651856c0eadb52a9ce0b9e95211"
#zip_code="87121"
zip_code = input("zip code: ")
api_url = "https://api.openweathermap.org/data/2.5/weather?zip="+zip_code+",us&appid="+api_key

def fetchfromOWM():
    owm = pyowm.OWM(api_key)

    place = input("Enter City State Country: ")
    observation = owm.weather_at_place(place)

    current = observation.get_weather()
    pprint(current.get_temperature('celcius'))
    print(current.get_temperature('celcius')["temp"])

def fetchfromRequests():
    response = requests.get(api_url)
    data = response.json()

    pprint(data)

    createFile(data)
    
def createFile(data):
    with io.open('openweathermao.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4))
             

if __name__ == "__main__":
    fetchfromRequests()
    fetchfromOWM()




    
