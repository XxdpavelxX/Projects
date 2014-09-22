#__author__ = 'xxdpavelxx'
from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka.producer import SimpleProducer, KeyedProducer
import pymongo
from pymongo import MongoClient
import json
import ast

c = MongoClient("54.210.157.57")
db = c.test_database3
collection = db.tweet_col

kafka = KafkaClient("54.210.157.57:9092")

consumer = SimpleConsumer(kafka,"myconsumer","test")
for tweet in consumer:
    #print tweet.message.value
    jsonTweet=json.dumps(tweet.message.value)
    jsonLoad=json.loads(jsonTweet)
    #print type (ast.literal_eval( u"{u'city': u'new-york', u'name': u'Home', u'display_value': u'2 Main Street'}"))
    Jdict= ast.literal_eval(jsonLoad)
    #print type(jsonLoad.decode('string-escape').strip('"'))
    collection.insert(Jdict)
    print "it works"


