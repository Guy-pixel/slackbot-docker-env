import os
from slack_bolt import App

# Initialize bot with Slack token and signing secret
app = App(token=os.getenv("SLACK_BOT_TOKEN"), signing_secret=os.getenv("SLACK_SIGNING_SECRET"))

@app.event("message")
def handle_message_events(event, say):
    say(f"Hello <@{event['user']}>! You said: {event['text']}")

if __name__ == "__main__":
    app.start(3000)