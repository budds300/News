from flask import render_template
from . import main
from ..request import get_articles,get_news

@main.route('/')
def index():
    
    language = get_news('en')
    title = 'Home - Welcome to News Updates sites to get the latest news'
    return render_template('index.html',en =language)

@main.route('/articles/<id>')
def articles(id):
      '''
    Views  article page function that returns the news details page and its data
    '''
      article = get_articles(id)
      print(article)
      return render('article.html',article = article)
    
    