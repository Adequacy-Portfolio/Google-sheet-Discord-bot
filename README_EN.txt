Installation Instructions

To run this project, you must have Python version 3.11.0 installed on your system.

Installing Python 3.11.0

You can download Python 3.11.0 from the official Python website: https://www.python.org/downloads/release/python-3110/. Follow the installation instructions for your operating system.

Dependencies

After installing Python 3.11.0, you need to install the following dependencies using pip:

discordpy
jsons
os.path
json
google-auth
google-auth-oauthlib
google-api-python-client

To install these dependencies, run the following command in your terminal or command prompt:

pip install discordpy jsons google-auth google-auth-oauthlib google-api-python-client


---------------------------------

# Bot Setup Instructions

Before running the bot, ensure that you follow these setup instructions:

1. **Configuration File:**
    - Fill out the `configuration.json` file with the required information:
        - Token for the bot
        - Spreadsheet name and ID corresponding to the Google Sheet where you want to store information
    - Secret bot ID: Corresponds to the webhook ID
    - The "channel" field corresponds to the channel where you have set the webhook to send messages through Discord server settings.

2. **Google App Script Code:**
    - Copy the Google Apps Script code into the Google Apps Script extension in Google Sheets.
    - Change the webhook URL in the Google Apps Script code to your webhook URL.

3. **Google API Credentials:**
    - Place the credentials file obtained from the Google Sheets API inside the `google_api` folder.

4. **Additional Notes:**
    - Confirm that you have added an "on edit" trigger in Google Sheets.
    - On the first run of the bot and when using a slash command, you will be prompted to log in to your Google account.
    - Note that the column names seen in the screenshots need to be entered manually. However, the bot does not require them to fill data as it will enter them regardless.

