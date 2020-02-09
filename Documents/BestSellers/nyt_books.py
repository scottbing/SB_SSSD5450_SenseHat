from flask import Flask, render_template, request, url_for
import requests, pprint

app=Flask(__name__)

api_key="s9KHLyU9kgUE9ioGGzemRgoOjVWyxFgQ"

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':

        api_url = "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key="+api_key

	# get the data from the URL
        response = requests.get(api_url)
        data = response.json()

        return render_template('books.html', books = data['results']['books'])

