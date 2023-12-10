from flask import Flask, render_template, request, redirect, url_for
import feedparser

app = Flask(__name__)

# Store feed sources and folders
feed_sources = {
    'General': [
        {'name': 'OpenAI Blog', 'url': 'https://openai.com/feed.xml'},
        {'name': 'BBC News', 'url': 'http://feeds.bbci.co.uk/news/rss.xml'}
    ],
    'Tech': [
        {'name': 'TechCrunch', 'url': 'https://techcrunch.com/feed/'},
        {'name': 'Wired', 'url': 'https://www.wired.com/feed/rss'}
    ]
}

# Route for home page
@app.route('/')
def index():
    return render_template('./index.html', folders=feed_sources.keys())

# Route for displaying individual feeds
@app.route('/feed/<folder>/<source>')
def display_feed(folder, source):
    feed = [src for src in feed_sources[folder] if src['name'] == source][0]
    parsed_feed = feedparser.parse(feed['url'])
    return render_template('./feed.html', folder=folder, source=source, entries=parsed_feed.entries)

# Route for aggregated feed
@app.route('/all-feeds')
def all_feeds():
    all_entries = []
    for folder in feed_sources:
        for source in feed_sources[folder]:
            parsed_feed = feedparser.parse(source['url'])
            all_entries.extend(parsed_feed.entries)
    all_entries.sort(key=lambda x: x.published_parsed, reverse=True)
    return render_template('./all_feeds.html', entries=all_entries)

# Route for adding a new source
@app.route('/add-source', methods=['POST'])
def add_source():
    folder = request.form['folder']
    source_name = request.form['source']
    source_url = request.form['url']

    if folder not in feed_sources:
        feed_sources[folder] = []

    feed_sources[folder].append({'name': source_name, 'url': source_url})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
