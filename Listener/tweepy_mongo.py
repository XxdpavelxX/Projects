#__author__ = 'xxdpavelxx'
import sys
import tweepy
import json
from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka.producer import SimpleProducer, KeyedProducer
from pymongo import MongoClient
import json
import ast

c = MongoClient("54.210.157.57")
db = c.test
collection = db.test2

kafka = KafkaClient("54.210.157.57:9092")
consumer = SimpleConsumer(kafka,"anygroup??","random_topic2")  #(kafka, ??? collection, topic)

for tweet in consumer:
    #print tweet.message.value
    try:
        jsonTweet=json.dumps(tweet.message.value)
        jsonLoad=json.loads(jsonTweet)
        Jdict= ast.literal_eval(jsonLoad)
        collection.insert(Jdict)
        #print Jdict
    except:
        pass

