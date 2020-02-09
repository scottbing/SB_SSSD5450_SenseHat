from flask import Flask, render_template, request, url_for, redirect, jsonify
import requests

app=Flask(__name__)

api_key="0f0a1651856c0eadb52a9ce0b9e95211"

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':

        zip_code="87121"
        api_url = "https://api.openweathermap.org/data/2.5/weather?zip="+zip_code+",us&appid="+api_key+"&units=imperial"

        response = requests.get(api_url)
        data = response.json()

        temp = data["main"]["temp"]

        return render_template('index.html', location = "Albuquerque (default)", temperature=temp)

    if request.method == 'POST':

        location = request.form['location']
        #api_url = "https://api.openweathermap.org/data/2.5/weather?q="+location+",us&appid="+api_key+"&units=imperial"

        #response = requests.get(api_url)
        #data = response.json()

        #place = data["name"]
        #temp = data["main"]["temp"]

        return redirect(url_for('index.html', location = place, temperature = temp)

@app.route('/forecast/<zip_code>')
def forecast(zip_code):



	api_url = "https://api.openweathermap.org/data/2.5/forecast?zip="+zip_code+",us&appid="+api_key+"&units=imperial"
	response = requests.get(api_url)
	data = response.json()

	return render_template('forecast.html', forecast=data)

@app.route('/json')
def json():

	zip_code = "87122"
	api_url = "https://api.openweathermap.org/data/2.5/forecast?zip="+zip_code+",us&appid="+api_key+"&units=imperial"
	response = requests.get(api_url)
	data = response.json()

	return jsonify(data)











        
