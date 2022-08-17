import pandas as pd
import tweepy
import csv

api_key = "change with your consumer key"
api_secret_key = "change with your consumer secret"
access_token = "change with your access token"
access_token_secret = "change with your access secret"

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
