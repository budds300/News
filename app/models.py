class News:
    '''
    News class to define new objects
    '''
    
    def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description
        
class Articles:
    '''
    Class that defines article objects
    '''
    
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage=urlToImage
        self.publishedAt= publishedAt
        