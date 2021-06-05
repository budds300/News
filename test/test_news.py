import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test class to test the be.havior of the news class
    '''
    def setUp(self):
        '''
        setup method will run before every test
        '''
        self.news = News('Aljazeer-news','Aljazeera News','News, analysis from the Middle East & worldwide, multimedia & interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.news,News))
        
