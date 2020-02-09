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

        T = [[11, 12, 5, 2], 
	    [15, 6,10, 22], 
	    [10, 8, 12, 5], 
	    [12,15,  8, 6]]

        # making list of pokemons 
        Pokemons =["Pikachu", "Charizard", "Squirtle", "Jigglypuff", "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]

        status = data['status']
        num_results = data['num_results']

	
        rank = data['results']['books'][0]['rank']
        title = data['results']['books'][0]['title']
        author = data['results']['books'][0]['author']
        publisher = data['results']['books'][0]['publisher']
        description = data['results']['books'][0]['description']
        weeks = data['results']['books'][0]['weeks_on_list']
        book_image = data['results']['books'][0]['book_image']

        
        return render_template('books.html', rank=rank, title=title, author=author, publisher=publisher, weeks=weeks, description=description,
                               book_image=book_image, len = len(Pokemons), Pokemons = Pokemons)
 
