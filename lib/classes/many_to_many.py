class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        author.articles().append(self)
        magazine.articles().append(self)
        if not magazine in author.magazines():
            author.magazines().append(magazine)
        if not author in magazine.contributors():
            magazine.contributors().append(author)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and not hasattr(self, '_title'):
            self._title = title
        
class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []
        self._magazines = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) and not hasattr(self, '_name'):
            self._name = name
    
    def articles(self):
        return self._articles

    def magazines(self):
        return self._magazines

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = list({magazine.category for magazine in self.magazines()})
        return topics if topics else None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        self._contributors = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category):
            self._category = category
    
    def articles(self):
        return self._articles

    def contributors(self):
        return self._contributors

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        contributing_authors = []
        for contributor in self.contributors():
            count = 0
            for article in self.articles():
                if contributor == article.author:
                    count += 1
                    if count > 2:
                        contributing_authors.append(contributor)

        return contributing_authors if contributing_authors else None