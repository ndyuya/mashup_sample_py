mashup_sample_py
================

WebサービスのAPIを使ったマッシュアップのサンプルプログラム (python版)

使い方
------
 0. このリポジトリのファイルを取得 (cloneでもzipダウンロードでも可)
 1. Google Maps APIとTwitterのAPIを使えるように準備する
     * Google API key
     * リクルートWEBサービス API Key <a href="http://webservice.recruit.co.jp/"><img src="http://webservice.recruit.co.jp/banner/hotpepper-s.gif" alt="ホットペッパー Webサービス" width="135" height="17" border="0" title="ホットペッパー Webサービス"></a>
 2. Dockerイメージをビルドする
 ```
 docker build -t flask .
 ```
 3. 各種キーを環境変数に指定して、Dockerコンテナを起動する
 ```
 docker run \
 -e GOOGLE_MAPS_API_KEY="YOUR_GOOGLE_MAPS_API_KEY" \
 -e RECRUIT_API_KEY="YOUR_RECRUIT_API_KEY" \
 -p 5000:5000 \
 -it flask
 ```
 4. http://127.0.0.1:5000/ にアクセスする
