# Abetter
TwitterをスクレイピングしてLSTMに学習させた発言をランダムに生成するウェブアプリ

環境：
* Docker
* Python3.6
* PyTorch
* Flask

外部で学習させた重みをFlaskのウェブアプリで使用可能にしています。

モデルはLSTMです。

## 使用方法
1. git clone this/repo
2. cd abetter
3. docker build -t container:1.0 .
4. docker run -it -p 5000:5000 -v ~path/to/repo:/abetter container:1.0
5. Docker内部へ移動
6. cd abetter
7. flask run --host 0.0.0.0
表示されたURLにブラウザでアクセス

あとはご自由にお楽しみください。
モデルの精度は今後LSTM以外を使ったりして改善していく予定です。

## 参考記事
モデルの読み込み
https://qiita.com/derodero24/items/f4cc46f144f404054501

Flaskで自然言語処理アプリの作成
https://qiita.com/oreyutarover/items/909d614ca3b48d2c9e16

ポート開放でハマった所の解決策
https://stackoverflow.com/questions/30323224/deploying-a-minimal-flask-app-in-docker-server-connection-issues
