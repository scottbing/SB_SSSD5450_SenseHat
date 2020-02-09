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
##        print(response.json())

        status = data['status']
        num_results = data['num_results']

##        i = 0
##        for books in data['results']['books']:
##            print(data['results']['books'][i]['rank'])
##            print(data['results']['books'][i]['title'])
##            print(data['results']['books'][i]['author'])
##            print(data['results']['books'][i]['publisher'])
##            print(data['results']['books'][i]['description'])
##            print(data['results']['books'][i]['weeks_on_list'])
##            print(data['results']['books'][i]['book_image'])
##            i = i + 1

        # build a matrix of the selected JSON    
        matrix = [[]]
        for i in range(0,14):
            matrix[i] = data['results']['books'][i]['rank']
            for j in range(0,5):
                matrix.append(data['results']['books'][j]['title'])
                matrix.append(data['results']['books'][j]['title'])
                matrix.append(data['results']['books'][j]['author'])
                matrix.append(data['results']['books'][j]['publisher'])
                matrix.append(data['results']['books'][j]['description'])
                matrix.append(data['results']['books'][j]['weeks_on_list'])
                matrix.append(data['results']['books'][j]['book_image'])

        print(matrix[0])

        rank = data['results']['books'][10]['rank']
        title = data['results']['books'][10]['title']
        author = data['results']['books'][10]['author']
        publisher = data['results']['books'][10]['publisher']
        description = data['results']['books'][10]['description']
        weeks = data['results']['books'][10]['weeks_on_list']
        book_image = data['results']['books'][10]['book_image']


        return render_template('books.html', rank=rank, title=title, author=author, publisher=publisher, weeks=weeks, description=description,
                               book_image=book_image, len = len(matrix), matrix = matrix)

