# Rocket Launch Reminder

Rocket Launch Reminder is a Python script that sends reminders about upcoming rocket launches to a designated Slack channel. It retrieves launch data from the Launch Library 2 API and utilizes the Slack API to send reminders.

## Installation

1. Clone the repository or download the code files.
2. Install the required libraries by running the following commands:
	pip install slack-sdk
	pip install requests
3. Provide your Slack token in the `SLACK_TOKEN` variable in the code. Make sure to generate a token with the necessary permissions to send messages to the desired Slack channel.

## Usage

1. Run the script by executing the following command:
	python spacelaunch.py
2. The script will fetch upcoming rocket launches from the Launch Library 2 API and send reminders to the designated Slack channel. The reminders include launch date, rocket details, agency, location, and description.

## Customization

- Modify the `SLACK_TOKEN` variable to your own Slack token.
- Adjust the Slack channel by changing the `channel` parameter in the `client.chat_postMessage()` method.
- Customize the reminder message in the `send_reminder_to_slack()` method according to your preferences.

## License

This project is licensed under the MIT License.