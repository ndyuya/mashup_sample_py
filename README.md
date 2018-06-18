mashup_sample_py
================

WebサービスのAPIを使ったマッシュアップのサンプルプログラム (python版)

使い方
------
 0. このリポジトリのファイルを取得 (cloneでもzipダウンロードでも可)
 1. Google Maps APIとTwitterのAPIを使えるように準備する
     * Google API key
     * Twitter [Consumer key]
     * Twitter [Consumer secret]
     * Twitter [Access Token]
     * Twitter [Access Token secret]
 2. Dockerイメージをビルドする
 ```
 docker build -t flask .
 ```
 3. 各種キーを環境変数に指定して、Dockerコンテナを起動する
 ```
 docker run \
 -e GOOGLE_MAPS_API_KEY="YOUR_GOOGLE_MAPS_API_KEY" \
 -e TWITTER_CONSUMER_KEY="YOUR_TWITTER_CONSUMER_KEY" \
 -e TWITTER_CONSUMER_SECRET="YOUR_TWITTER_CONSUMER_SECRET" \
 -e TWITTER_ACCESS_TOKEN="YOUR_TWITTER_ACCESS_TOKEN" \
 -e TWITTER_ACCESS_TOKEN_SECRET="YOUR_TWITTER_ACCESS_TOKEN_SECRET" \
 -p 5000:5000 \
 -it flask
 ```
 4. http://127.0.0.1:5000/ にアクセスする
