from tweepy import OAuthHandler
from tweepy import Stream

import config
import stream_twitter

if __name__ == '__main__':
    l = stream_twitter.Listener()

    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    stream = Stream(auth, l)

    # Annoyingly, in Tweepy, IDs are sometimes noted as strings and other times as ints
    str_ids = []
    for tid in config.follow_ids:
        str_ids.append(str(tid))

    stream.filter(follow=str_ids)
