import twitter_old
import json


CONSUMER_KEY = 'CxT0uevMd2EsjqM5rNRDM9VlW'
CONSUMER_SECRET = 'u7EcEpvOVjlSjDFkfqN7gl4r1pau59I4txvPQgDOSksf5JEzw4'
OAUTH_TOKEN = '535814971-q66nrKX1BLvCQes6q8wPxwNlKvNV83DehNd5LE4M'
OAUTH_TOKEN_SECRET = 'wXeZV751OjZof5xkRVzvo7MoDLgs4t9jWVQh0ibSWrgtH'

auth = twitter_old.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter_old.Twitter(auth=auth)

q = '#MentionSomeoneImportantForYou'
count = 100

search_results = twitter_api.search.tweets(q=q, count=count)
statuses = search_results['statuses']

#Iterate through 5 more batches of results by following the cursor

for _ in range(5):
	print "Length of statuses", len(statuses)
	try:
		next_results = search_results['search_metadata']['next_results']
	except KeyError, e: #No more results when next_results doesn't exist
		break
		# Create a dictionary from next_results, which has the following form:
		# ?max_id=313519052523986943&q=NCAA&include_entities=1
		kwargs = dict([kv.split('=') for kv in next_results[1:].split("&") ])

		search_results = twitter_api.search.tweets(**kwargs)
		statuses += search_results['statuses']
	# Show one sample search result by slicing the list...
	print json.dumps(statuses[0], indent=1)