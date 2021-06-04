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

def get_news(language):
    '''
    Function that gets the json request to our url request
    '''
    get_news_url = base_url.format(language,api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_information = url.read()
        get_news_response= json.loads(get_news_information)
        
        news_sources = None
        
        if get_news_response['sources']:
            news_sources_list= get_news_response['sources']
            news_sources= process_sources(news_sources_list)
            
    return news_sources

def process_sources(news_list):
      '''
    Function that processes the news results and transform them to a list of objects
    
    Args:
        news_list: A list of dictionaries that contains movie objects
        
    Returns : 
        news_results : Alist of news objects
    '''