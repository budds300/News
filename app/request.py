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
      news_sources = []
      
      for news_item in news_list:
          id = news_item.get('id')
          name = news_item.get('name')
          description = news_item.get('description')
          
          if id:
              news_object = News(id,name,description)
              news_sources.append()(news_object)
              
      return news_sources
  
  
def get_articles(id):
       '''
    Function that gets the json response to our url request
    '''
       get_article_url = base_url.articles.format(id,api_key)
       
       with urllib.request.urlopen(get_article_url) as url:
           get_article_data= url.read()
           get_article_response = json.loads(get_article_data)
           
           news_article = None
           
           if get_article_response['articles']:
               news_article_list = get_article_response['articles']
               new_articles = process_articles(news_article_list)
               
       return news_article
   
def process_articles(article_list):
          '''
    Function that processes the news results and transform them to a list of objects
    
    Args:
        news_list: A list of dictionaries that contains movie objects
        
    Returns : 
        news_results : Alist of news objects
    '''
          news_articles = []
      
          for article_items in article_list:
                id = article_item.get('id')
                author = article_item.get('aurthor')
                title = article_item.get('title')
                description = article_item.get('description')
                url = article_item.get('url')
                urlToImage= article_item.get('urlToImage')
                publishedAt= article_item.get('publishedAt')
                
                if urlToImage:
                    article_object= Articles(author,title,description,url,urlToImage,publishedAt)
                    news_sources.append()(news_object)
                    
          return news_articles
  
               