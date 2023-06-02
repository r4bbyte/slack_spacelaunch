import requests
import pytz
from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Your Slack token
SLACK_TOKEN = ""

# Launch Library 2 API URL
LAUNCH_LIBRARY_API_URL = "https://ll.thespacedevs.com/2.2.0/launch/upcoming"

# Get upcoming rocket launches
def get_upcoming_launches():
    response = requests.get(LAUNCH_LIBRARY_API_URL)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        return None

def is_future_launch(launch_date):
    launch_date = datetime.strptime(launch_date, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=pytz.UTC)
    current_date = datetime.now(pytz.UTC)
    return launch_date > current_date


# Send a reminder to Slack channel
def send_reminder_to_slack(launch):
    client = WebClient(token=SLACK_TOKEN)
    try:
        missions = launch.get('missions')
        description = missions[0]['description'] if missions else 'No mission information available'

        rocket = launch.get('rocket', {})
        rocket_name = rocket.get('name', 'N/A')
        rocket_agency = rocket.get('agency', 'N/A')

        location = launch.get('location', {})
        location_name = location.get('name', 'N/A')

        response = client.chat_postMessage(
            channel="#spacelaunch",
            text=f"Reminder: Upcoming Rocket Launch!\n"
                 f"Date: {launch['net']}\n"
                 f"Rocket: {rocket_name}\n"
                 f"Agency: {rocket_agency}\n"
                 f"Location: {location_name}\n"
                 f"Description: {description}"
        )
        print(response)
    except SlackApiError as e:
        print(f"Error sending reminder to Slack: {e.response['error']}")

# Main plugin function
def remind_upcoming_launches():
    launches = get_upcoming_launches()
    if launches:
        for launch in launches:
            if is_future_launch(launch['net']):
                send_reminder_to_slack(launch)

# Run the plugin
remind_upcoming_launches()