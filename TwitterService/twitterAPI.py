'''
Eb3fSiF7rMZiv0CrtpHms9yOW (API key)
pGkE3xGXAh6w3i2odQ3YOnsng9QKKZ7TBY8aKcVHRLFz0V1oYO (API secret key)

Personal Access Tokens--
1434974690703908864-0hJrYAZoqUFPZAXlRBPckWlQJbhkOY (Access token)
8P5CDkA7jUkXsHWlQEWMH1MXNeHevXwthM4gYZu0QFpgH (Access token secret)
Read and write (Access level)
'''
import twitter
import itertools

# Using python-twitter library that provides a pure python interface for Twitter API


# Authenticate API #
def auth():
	consumer_token = 'Eb3fSiF7rMZiv0CrtpHms9yOW'
	consumer_secret_token = 'pGkE3xGXAh6w3i2odQ3YOnsng9QKKZ7TBY8aKcVHRLFz0V1oYO'
	access_token = '1434974690703908864-0hJrYAZoqUFPZAXlRBPckWlQJbhkOY'
	secret_access_token = '8P5CDkA7jUkXsHWlQEWMH1MXNeHevXwthM4gYZu0QFpgH'
	api = twitter.Api(consumer_key=consumer_token,
				consumer_secret=consumer_secret_token,
				access_token_key = access_token,
				access_token_secret = secret_access_token)
	return(api)


# New Tweet #
def tweet(message):
	api = auth()
	post_update = api.PostUpdate(status=message)
	return(post_update)

### Get_All_Tweets ###
def get_tweets(user):
	api = auth()
	update = api.GetUserTimeline(screen_name=user)
	return(update)

# Delete Tweet #
def del_tweet(tweet_id):
	api = auth()
	destroyed = api.DestroyStatus(status_id=tweet_id)
	return destroyed

def paging(iterable, page_size):
    while True:
        i1, i2 = itertools.tee(iterable)
        iterable, page = (itertools.islice(i1, page_size, None),
                list(itertools.islice(i2, page_size)))
        if len(page) == 0:
            break
        yield page
