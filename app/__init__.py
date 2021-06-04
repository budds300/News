from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    #Creating configuration of app
    app.config.from_object(config_options[config_name])
    #initializing flask extensions
    bootstrap.init_app(app)
    
    #Registering blueprint
    from .main import configure_request
    configure_request(app)
    
    return app
