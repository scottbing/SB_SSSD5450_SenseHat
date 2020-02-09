from flask import Flask, render_template, request, url_for
import requests

from pprint import pprint

api_key="buo88wNnBkrso1T6H4OdeWLMl5erkwZE"

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():

    if  request.method ==  'GET':
        filter = "Obama"
        api_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+filter+"&appid="+api_key

        response = requests.get(api_url)
        data = response.json()

        result = data['response']['docs']['headline']['main']
                                        

        return render_template('index.html', headline=result)
                                        
