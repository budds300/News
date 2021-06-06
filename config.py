import os
class Config:
    '''
    General configuration class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language={}&apiKey={}'
    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?source={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')  
class ProdConfig(Config):
    '''
    production configuration child class
    
    Args:
        Config:The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config:The parent  configuration class with General configuration settings
    '''
    DEBUG = True
    
config_options = {
    'development': DevConfig,
    'production':ProdConfig
}
