# Twitter API keys. You might need to get approved for this.

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Twitter Settings

follow_ids = [44196397]  # Just follow Elon by default. These are Twitter IDs.
follow_words = {         # Hit words (lowercase), corresponding to their market symbols.
        "doge": "DOGEUSDT",
        "bitcoin": "BTCUSDT",
        " btc": "BTCUSDT",
        "$btc": "BTCUSDT"
}

# Binance API keys. You must generate the key, make sure it has ALL of these perms: Enable Reading. Enable Spot & Margin Trading. Enable Futures

api_key = ''
api_secret = ''

# Trading Settings

trade_size = 40 # How much ya bettin in USDT
cash_out_percent = 20 # Take Profit/Stop Loss based on percentage of current price. For manual mode, set to False
