import feedparser
from datetime import datetime, timedelta

folders = []
unorginized_sources = []

class folder:
    name = ""
    sources = []

    def __init__(self, name):
        self.name = name
        self.sources = []

    def add_source(self, source):
        self.sources.append(source)

    def remove_source(self, source):
        self.sources.remove(source)

    def get_name(self):
        return self.name

    def get_sources(self):
        return self.sources
    
    def get_folder_feed(self):
        folder_feed = []
        for source in self.sources:
            for article in source.articles:
                folder_feed.append(article)
        return folder_feed

class source:
    name = ""
    url = ""
    articles = []

    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.articles = self.get_articles(url)

    def update(self):
        self.articles = self.get_articles(self.url)

    def add_article(self, article):
        self.articles.append(article)

    def remove_article(self, article):
        self.articles.remove(article)

    def get_name(self):
        return self.name

    def get_url(self):
        return self.url
    
    def get_articles(url):
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries:
            title = entry.title
            date = entry.published
            description = entry.description
            link = entry.link
            articles.append(article(title, date, description, link))
        return articles
    
    def get_articles(self):
        return self.articles
    
    def get_last24(self):
        last24_articles = []
        for article in self.articles:
            if article.date > datetime.now() - timedelta(days=1):
                last24_articles.append(article)
        return last24_articles
    

class article:
    title = ""
    date = ""
    description = ""
    link = ""  

    def __init__(self, title, date, description, link):
        self.title = title
        self.date = date
        self.description = description
        self.link = link

def main():
    pass

if __name__ = "__main__":
    main()