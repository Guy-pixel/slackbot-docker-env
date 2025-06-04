import os
import sys
import logging

print('step1');

from slack_bolt import App

print('step2')

# Initialize bot with Slack token and signing secret
app = App(token=os.getenv("SLACK_BOT_TOKEN"), signing_secret=os.getenv("SLACK_SIGNING_SECRET"))

print('step3')
@app.event("app_mention")
def handle_app_mention(event, say):
    logging.info(f"Received an app mention event: {event}")
    say("Hello! I am running!")

if __name__ == "__main__":
    logging.info("Starting the Slack bot...")
    app.start(port=3042)