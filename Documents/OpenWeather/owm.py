#3rdParty modules
import requests
import pyowm 

#python core modules
from pprint import pprint
import io, json

#API
api_key = "f68f0b9148188e3bb8f02d971c55bece"
#zip_code = "87121"
zip_code = input("zip code: ")
api_url = "https://api.openweathermap.org/data/2.5/weather?zip="+zip_code+",us&appid="+api_key

#requests function
def fetchfromRequests():    
    response = requests.get(api_url)
    data = response.json()
    
    #nicely display json data
    pprint(data)

    #create json file
    createFile(data)

#OWM library function
def fetchfromOWM():
    owm = pyowm.OWM(api_key)
    
    #observation = owm.weather_at_place('Albuquerque,NM,US')
    place = input("Enter City,State,Country: ")
    observation = owm.weather_at_place(place)
    
    current = observation.get_weather()
    pprint(current.get_temperature('celsius'))
    print(current.get_temperature('celsius')["temp"])

def createFile(data):
    with io.open('openweathermap.json', 'w', encoding='utf-8') as json_file:
        #indent - size for nested structures
        #sort_keys - output of dictionaries will be sorted by key
        #ensure_ascii -x output is guaranteed to have all incoming non-ASCII characters escaped
        json_file.write(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4))

#main code block
if __name__ == "__main__":
    fetchfromRequests()
    fetchfromOWM()
