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
 2. 1.で取得したキーをそれぞれファイルに書き込む
     * project/main.pyの14〜18行目にある「YOUR_*」
 3. http://c4sa.nifty.com/ へアクセスして、Flaskコンテクストでキャンバスを作る
     * pythonの軽量Webフレームワーク
 4. C4SA上のproject配下にリポジトリのファイルをアップロード
 5. C4SAコンパネの「デーモン管理」で「gunicorn」を「リスタート」
 7. ヘッダー部分にあるURLへアクセスして動作確認する

