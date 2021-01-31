from tweepy.streaming import StreamListener

import config
import purchase_contracts

class Listener(StreamListener):
    def on_status(self, status):
        if status.author.id in config.follow_ids:
            print(str(status.author.name) + ": " + status.text)

            ticker = ""
            for key in config.follow_words:
                if key in status.text.lower():
                    ticker = config.follow_words[key]
                    break

            if ticker:
                print("HOLY SHIT IM BUYING " + ticker)
                purchase_contracts.buy(ticker)

        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False
