# coding=utf8
import html
import os
import requests

from flask import Flask
from flask import render_template

app = Flask(__name__)

lat = 38.2603946787027
lng = 140.88238748726602

url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
body = {
    'key': os.environ["RECRUIT_API_KEY"],
    'lat': lat,
    'lng': lng,
    'range': '300m',
    'type': 'lite',
    'order': 4,
    'format': 'json'
}

maps_api_key = os.environ["GOOGLE_MAPS_API_KEY"]


def escapeText(target):
    return html.escape(target, True)


def createContents(shop):
    shop_name = "<div class=\"shop_name\"><a href=\"" + shop['urls']['pc'] + "\" target=\"_blank\">"\
                + escapeText(shop['name']) + "</a></div>"
    shop_catch = "<div class=\"shop_catch\">" + escapeText(shop['catch']) + "</div>"
    shop_image = "<div class=\"shop_image\"><img src=\"" + shop['photo']['pc']['s'] + "\"></div>"
    return "<div id=\"content\"><div id=\"siteNotice\"></div><div id=\"bodyContent\"><div class=\"shop\">"\
        + shop_name + shop_catch + shop_image + "</div></div></div>"


def getShop():
    response = requests.get(url, body).json()
    shops = []
    for shop in response['results']['shop']:
        if shop['lat'] is not None and shop['lng'] is not None:
            shops.append(
                {
                    'id': shop['id'],
                    'lat': shop['lat'],
                    'lng': shop['lng'],
                    'content': createContents(shop)
                }
            )
    return shops


@app.route('/')
def index():
    shops = getShop()
    return render_template('index.html', lat=lat, lng=lng, maps_api_key=maps_api_key, shops=shops)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
