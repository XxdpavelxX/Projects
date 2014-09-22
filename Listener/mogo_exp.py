__author__ = 'xxdpavelxx'

import pymongo
import json

from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka.producer import SimpleProducer, KeyedProducer
import twitter
import sys
from twitter.oauth_dance import parse_oauth_tokens
from twitter.oauth import read_token_file, write_token_file


def oauth_login():
    # XXX: Go to http://twitter.com/apps/new to create an app and get values
    # for these credentials that you'll need to provide in place of these
    # empty string values that are defined as placeholders.
    # See https://dev.twitter.com/docs/auth/oauth for more information
    # on Twitter's OAuth implementation.

    CONSUMER_KEY = 'ULI6uCZ07LS2MMGW7DVhfP9Kh'
    CONSUMER_SECRET = 'JWVLqxIqDzAMDICq7ni5WYm2sm06kNUqI465YE1Y6vhJPuJmOV'
    OAUTH_TOKEN = '535814971-cHEHHJz01svTweT1KvF6HuGGtnL45O4WUVXfxgnO'
    OAUTH_TOKEN_SECRET = '5FOQ8Q38p3C8Qy0CzGwJU73V5BFVVpkqmwTchVxbb3ORa'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

# Query terms
def runner():
    q = 'UFC' #Comma-separated list of terms

    print >> sys.stderr, 'Filtering the public timeline for track="%s"' % (q,)

# Returns an instance of twitter.Twitter
    twitter_api = oauth_login()

# Reference the self.auth parameter
    twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

# See https://dev.twitter.com/docs/streaming-apis
    stream = twitter_stream.statuses.filter(track=q)

# For illustrative purposes, when all else fails, search for Justin Bieber
# and something is sure to turn up (at least, on Twitter)
    db = pymongo.MongoClient().test
    for tweet in stream:
        db.tweets.insert(json.loads(tweet))
    #if tweet.hangup==True:
     #       print 'hangup'
        try:
            print tweet["text"]
            producer.send_messages("test", str(tweet["text"]))
        except:
            continue


    #try:
        #runner()
    #except:
    #    print "Sorry not enough tweets to continue this feed, please restart the program to continue"
if __name__ =='__main__':
    kafka = KafkaClient("54.210.157.57:9092")
    producer = SimpleProducer(kafka)
    x = 0
    while x<10:
        print "Starting up"
        runner()
        x = x+1