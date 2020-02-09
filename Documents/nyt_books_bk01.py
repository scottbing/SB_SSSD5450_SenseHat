from flask import Flask, render_template, request, url_for
import requests, pprint

app=Flask(__name__)

api_key="s9KHLyU9kgUE9ioGGzemRgoOjVWyxFgQ"

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':

        
        #api_url = "https://api.openweathermap.org/data/2.5/weather?zip="+zip_code+",us&appid="+api_key+"&units=imperial"
        
        api_url = "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key="+api_key

	# get the data from the URL
        response = requests.get(api_url)
        data = response.json()
        print(response.json())

        status = data['status']
        num_results = data['num_results']
        

        #title = data['title']
        
	# define variables using dictioanry notation  key >>> value pairs
##        rank = data[books]['rank']
##        title = data['title']
##        author = data['author']
##        publisher = data['publisher']
##        weeks = data['weeks_on_list']
        
        return render_template('books.html', booktitle=status, num_results=num_results)
 
