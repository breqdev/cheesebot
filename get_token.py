import imp
import os
from dotenv import load_dotenv
import tweepy

load_dotenv()

handler = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_CLIENT_KEY"), os.getenv("TWITTER_CLIENT_SECRET"), callback="oob"
)

print(handler.get_authorization_url())

verifier = input("Verifier: ")
token, secret = handler.get_access_token(verifier)

print(f"Token: {token}")
print(f"Secret: {secret}")
