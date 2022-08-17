import pandas as pd
import tweepy
import csv

api_key = "FSy4ill1iGqLVX48czNagTzXD"
api_secret_key = "zIsaLcw8SSC5kSSL5IhEs90RG5dQhBOVqKigZ311t2BfuVyA0p"
access_token = "1531079819823554560-2kFNlXpxk9yt8WHO8wvqp0bfybp0Pn"
access_token_secret = "UuomwIRiWgyxSNDkMcb4wucGlxyoMCBBKjYYvV7jBgNSb"

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

keywords = ['polri','ferdy sambo']
f = open('data_tweet.csv', 'a', newline='')
fieldnames = ['id', 'timestamp', 'name', 'tweets', 'loc']
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()
f.close()
for k in keywords:
    tweets = api.search_tweets(k, count=1000, tweet_mode='extended')
    for item in tweets:
        if (not item.retweeted) and ('RT @' not in item.full_text):
            with open('data_tweet.csv', 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'id':item.id_str,'timestamp':item.created_at,'name':item.user.screen_name,'tweets':item.full_text,'loc':item.user.location})
