"""Kafka practice work where search tweets and use this code to consume them and safe to the mongodb database"""
"""Also this code uses textblob to determine is it positive neutral or negative tweet"""


import tweepy
import time
from kafka import KafkaProducer
from pymongo import MongoClient
import json
from textblob import TextBlob
access_token =
access_token_secret =
api_key =
api_secret =
bearer_token =

client = tweepy.Client(bearer_token, api_key, api_secret,
                       access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(
    api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

search_terms = ["trump"]
producer = KafkaProducer(bootstrap_servers='localhost:9092')

client = MongoClient('localhost', 27017)
db = client['twitter']
collection = db['tweets']
MONGO_HOST = 'mongodb://localhost'


class MyStream(tweepy.StreamingClient):

    def on_connect(self):

        print("Connected")

    def on_tweet(self, tweet):

        client = MongoClient(MONGO_HOST)

        db = client["twitter"]

        dat = json.dumps(tweet.data)

        asss = json.loads(dat)

        if tweet.referenced_tweets == None:

            print(tweet.text)

            analysis = TextBlob(tweet.text)

            if analysis.sentiment.polarity > 0:
                result = "positive"
            elif analysis.sentiment.polarity < 0:

                result = "negative"
            else:
                result = "neutral"

            print(result)

            producer.send("prokkis", bytes(tweet.text, 'utf-8'))
            producer.send("prokkis", bytes(result, 'utf-8'))

            db["twiitit"].insert_one(asss, result)

            time.sleep(0.5)


stream = MyStream(bearer_token=bearer_token)
stream.delete_rules(stream.get_rules().data)

for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter(tweet_fields=["referenced_tweets"])
