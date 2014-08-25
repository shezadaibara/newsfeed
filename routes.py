from flask import Flask, render_template, request, jsonify, Response
from pprint import pprint
from time import mktime
from datetime import datetime

import feedparser

app = Flask(__name__)


@app.route('/_feeds')
def feeds():
    keyword = request.args.get('keyword', '')
    feed_url = 'http://news.google.com/news?hl=en&gl=in&q={keyword}&um=1&ie=UTF-8&output=rss'.format(keyword=keyword)
    rawdata = feedparser.parse(feed_url)
    return render_template('feeds.html', entries=rawdata.get('entries', []))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.template_filter()
def timesince(dt, default="just now"):
    """
    Returns string representing "time since" e.g.
    3 days ago, 5 hours ago etc.
    """
    dt = datetime.fromtimestamp(mktime(dt))
    now = datetime.utcnow()
    diff = now - dt
    
    periods = (
        (diff.days / 365, "year", "years"),
        (diff.days / 30, "month", "months"),
        (diff.days / 7, "week", "weeks"),
        (diff.days, "day", "days"),
        (diff.seconds / 3600, "hour", "hours"),
        (diff.seconds / 60, "minute", "minutes"),
        (diff.seconds, "second", "seconds"),
    )

    for period, singular, plural in periods:
        
        if period:
            return "%d %s ago" % (period, singular if period == 1 else plural)

    return default


if __name__ == '__main__':
    app.run(debug=True)
    print 'hello'
