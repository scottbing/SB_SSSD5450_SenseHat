from flask import Flask, render_template, request, url_for
import requests

from pprint import pprint

api_key="buo88wNnBkrso1T6H4OdeWLMl5erkwZE"

app = Flask(__name__)


filter="obama"
# api_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+filter+"&appid="+api_key

api_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=obama&api-key=buo88wNnBkrso1T6H4OdeWLMl5erkwZE"


def fetchfromRequests():
    response = requests.get(api_url)
    data = response.json()

    pprint(response.json())

if __name__ == "__main__":
    fetchfromRequests()
