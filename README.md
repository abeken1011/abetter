# Abetter
TwitterをスクレイピングしてLSTMに学習させた発言をランダムに生成するウェブアプリ

環境：Docker
Python3.6
PyTorch
Flask

外部で学習させた重みをFlaskのウェブアプリで使用可能に

## 使用方法
git clone this/repo
cd abetter
docker build -t container:1.0 .
docker run -it -p 5000:5000 -v ~path/to/repo:/abetter container:1.0
Docker内部へ移動
cd abetter
flask run --host 0.0.0.0
表示されたURLにブラウザでアクセス

あとはご自由にお楽しみください。
モデルの精度は今後LSTM以外を使ったりして改善していく予定です。
