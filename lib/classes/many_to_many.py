class Article:
    #let's store all articles
    all = []

    #initialize Article instances
    def __init__(self, author, magazine, title):

        #confirm if the author is an instance of the author class
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of an author")
        
        #confirm if the magazine is an instance of the magazine class
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        
        #confirm that the title is a string that is the length of 5 to 50 characters
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string of len between 5 and 50")
        
        #initializing the instance variables
        self._title = title #this is a private instance variable
        self.author = author
        self.magazine = magazine

        #Adds the articles instance to the all class variable
        Article.all.append(self)
        
    # property decorator for a getter method for the title
    @property
    def title(self):
        return self._title
            
class Author:
    def __init__(self, name):
        #ensure that the name is a string that is also not empty
        if not isinstance(name, str):
            raise Exception("name must be a string")
        if len(name) == 0:
            raise Exception("name must not be empty")


        self._name = name

    # ensures that the name is read only
    @property
    def name(self):
        return self._name

    # returns a lists of articles that have been written by this specific author    
    def articles(self):
        return [article for article in Article.all if article.author == self]

    # returns a list of unique magazines written by the author
    def magazines(self):
        return list({article.magazine for article in self.articles()})

    # creates and returns a new article with the magazien and the title
    def add_article(self, magazine, title):
        # ensures thatthe magazine is an instance of the class Magazine
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of magazine")
        
        return Article(self, magazine, title)

    #returns a list of unique topic areas for this author's article
    def topic_areas(self):
        topic_areas = list(set(magazine.category for magazine in self.magazines()))
        return topic_areas if topic_areas else None

class Magazine:
    def __init__(self, name, category):
        #ensure name is a string
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        #ensure length of name is between 2 and 16
        if len(name) < 2 or len(name) > 16:
            raise Exception("name must not be empty")
        #category is a string
        if not isinstance(category, str):
            raise Exception("Category must be a string")
        
        self.name = name
        self.category = category

    @property
    def name(self):
            return self._name

    @name.setter
    def name(self, value):
        # ensure name is a string
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) < 2 or len(value) > 16:
            raise Exception("name must be between the length of 2 and 16")
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise Exception("Category must be a string")

    #returns a list of articles associated with a magazine
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    #returns authors/contributor of a magazine
    def contributors(self):
        return list({article.author for article in self.articles()})

    #returns a list of articles titles for a magazine
    def article_titles(self):
        return [article.title for article in self.articles()] if self.articles() else None

    # helps find authors who have contributes more than 2 articles in magazine
    def contributing_authors(self):
        author_count = {}

        for article in self.articles():
            if article.author in author_count:
                author_count[article.author] += 1
            else:
                author_count[article.author] = 1

        result = [author for author, count in author_count.items() if count > 2]
        return result if result else None