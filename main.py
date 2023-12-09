import feedparser

urls = []

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



def main():
    pass

if __name__ = "__main__":
    main()