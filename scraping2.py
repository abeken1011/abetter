from twitter_scraper import get_tweets

tw_list = []
for i in range(1, 100):
    # 処理時間がマジで長いので繰り返し回数を表示する
    print(i)
    try:
        for tweet in get_tweets('sanma_ow', pages=i):
            if tweet["likes"] < 5 and tweet["text"] not in tw_list and tweet["text"] is not "" \
                    and tweet["entries"]["urls"] == [] and tweet["entries"]["photos"] == [] and "http" not in tweet["text"]:
                tw_list.append(tweet["text"])
            if i == 1:
                print(tweet)
    except:
      break

with open("sanma_tweets.csv", "w")as data:
    for i in tw_list:
        i = i + ",\n"
        data.write(i)