import urllib.requesty,json
from .models import News,Articles

#Getting api key
api_key = None
#Getting the movie base url
base_url= None

def configure_request(app):
    global api_key,base_url
    api_key=app.config['NEWS_API_KEY']
    base_url_ = app.config['NEWS_API_BASE_URL']
    base_url_articles = app.config['ARTICLES_API_BASE_URL']

