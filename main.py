import os
from dotenv import load_dotenv

import tweepy

load_dotenv()

auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_CLIENT_KEY"),
    os.getenv("TWITTER_CLIENT_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"),
    os.getenv("TWITTER_ACCESS_SECRET"),
)

api = tweepy.API(auth)


class CheesemasterReply(tweepy.Stream):
    def on_status(self, status):
        if hasattr(status, "retweeted_status"):
            return

        if status.in_reply_to_status_id is not None:
            return

        if status.author.id != int(os.getenv("TWITTER_USER_ID")):
            return

        api.update_status(
            status="omg this blew up!!! anyways stream videos games by trixie mattel",
            in_reply_to_status_id=status.id,
            auto_populate_reply_metadata=True,
        )


reply = CheesemasterReply(
    os.getenv("TWITTER_CLIENT_KEY"),
    os.getenv("TWITTER_CLIENT_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"),
    os.getenv("TWITTER_ACCESS_SECRET"),
)
reply.filter(follow=[os.getenv("TWITTER_USER_ID")])
