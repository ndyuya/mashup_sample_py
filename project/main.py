# coding=utf8

from flask import Flask
from flask import render_template
from twython import Twython
from xml.sax.saxutils import *
import urllib, re, os
app = Flask(__name__)

q = u'駅'
lat = 35.691914
lng = 139.70034

maps_api_key = os.environ["GOOGLE_MAPS_API_KEY"]
tw_consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
tw_consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
tw_access_token = os.environ["TWITTER_ACCESS_TOKEN"]
tw_access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

def escapeText(target):
	return escape(target, {"'": '&apos;'})

def replaceLF(target):
	return re.compile(r'\n+').sub(r'<br>', target)

def replaceURL(target):
	return re.compile(r'([^"]|^)(https?|ftp)(://[\w:;/.?%#&=+-]+)').sub(r'\1<a href="\2\3">\2\3</a>', target)

def replaceMention(target):
	return re.compile(r'@([a-zA-Z0-9_]+)').sub(r'<a href="http://twitter.com/\1/">@\1</a>', target)

def replaceHashtag(target):
	return re.compile(r'#([^ ]+)').sub(r'<a href="http://search.twitter.com/?q=%23\1">#\1</a>', target)

def embedTweet(tw):
	text = replaceHashtag(replaceMention(replaceURL(replaceLF(escapeText(tw['text'])))))
	tw_user = "<div class=\"tw_user\"><a href=\"http://twitter.com/" + tw['user']['screen_name'] + "/\"><div class=\"tw_profile_image\"><img src=\"" + tw['user']['profile_image_url'] + "\"></div><div class=\"tw_name\">" + escapeText(tw['user']['name']) + "</div><div class=\"tw_screen_name\">@" + escapeText(tw['user']['screen_name']) + "</div></a></div>"
	tw_text = "<div class=\"tw_text\">" + text + "</div>"
	tw_created_at = "<div class=\"tw_created_at\"><a href=\"http://twitter.com/" + tw['user']['screen_name'] + "/status/" + tw['id_str'] + "\">" + tw['created_at'] + "</a></div>"
	tw_action = "<div class=\"tw_action\"><a href=\"https://twitter.com/intent/tweet?in_reply_to=" + tw['id_str'] + u"\">返信</a>&nbsp;/&nbsp;<a href=\"https://twitter.com/intent/retweet?tweet_id=" + tw['id_str'] + u"\">リツイート</a> / <a href=\"https://twitter.com/intent/favorite?tweet_id=" + tw['id_str'] + u"\">お気に入り</a></div>"
	return "<div id=\"content\"><div id=\"siteNotice\"></div><div id=\"bodyContent\"><div class=\"tw\">" + tw_user + tw_text + tw_created_at + tw_action + "</div></div></div>"

def getTweet():
	client = Twython(tw_consumer_key, tw_consumer_secret, tw_access_token, tw_access_token_secret)
	res = client.search(q=urllib.parse.quote_plus(q.encode('utf-8')), count=100, geocode="%f,%f,30km" % (lat,lng))
	statuses = []
	for tw in res['statuses']:
		if tw['geo'] is not None:
			statuses.append({'id':tw['id'], 'text':tw['text'],'created_at':tw['created_at'],'name':tw['user']['name'],'screen_name':tw['user']['screen_name'],'profile_image':tw['user']['profile_image_url'],'lat':tw['geo']['coordinates'][0],'lng':tw['geo']['coordinates'][1],'emb':embedTweet(tw)})
	return statuses

@app.route('/')
def index():
	tweets = getTweet()
	return render_template('index.html', lat=lat, lng=lng, maps_api_key=maps_api_key, tweets=tweets)

@app.route('/tweets')
def tweets():
	tweets = getTweet()
	return render_template('tweets.html', tweets=tweets)

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=True)
