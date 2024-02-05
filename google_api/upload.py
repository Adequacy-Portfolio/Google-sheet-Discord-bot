import os.path
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

with open("configuration.json", "r") as configuration:
    config = json.load(configuration)

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = config["google"]["spreadsheetid"]
SAMPLE_RANGE_NAME = config["google"]["sample_range_name"]


def upload_to_google_sheet(data):
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "google_api/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        # Prepare data for insertion
        values = [
            data.get("DiscordID", ""),
            data.get("ID", ""),
            data.get("Pseudo", ""),
            data.get("Timestamp", ""),
            data.get("Reason", ""),
        ]

        # Call the Sheets API to append data
        sheet = service.spreadsheets()

        # Get existing values in the specified range
        result = (
            sheet.values()
            .get(spreadsheetId=SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        existing_values = result.get("values", [])

        # If the first row is empty or does not contain column names, insert column names
        if not existing_values or not existing_values[0]:
            column_names = [
                "DisocrdID",
                "Pseudo",
                "ID",
                "Raison",
                "Timestamp",
                "Accepted",
            ]
            sheet.values().append(
                spreadsheetId=SPREADSHEET_ID,
                range=SAMPLE_RANGE_NAME,
                valueInputOption="RAW",
                body={"values": [column_names]},
                insertDataOption="INSERT_ROWS",
            ).execute()
            # Shift existing data down by one row
            existing_values = [[]] + existing_values

        # Append data
        sheet.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=SAMPLE_RANGE_NAME,
            valueInputOption="RAW",
            body={"values": [values]},
            insertDataOption="INSERT_ROWS",
        ).execute()

        print("Données téléchargées avec succès.")
    except HttpError as err:
        print(f"Une erreur s'est produite: {err}")
