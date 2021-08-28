from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] #add this .readonly if you want to use the spreadsheet in Read Only mode
SERVICE_ACCOUNT_FILE = 'fresh-park-324313-1d12d1b8c076.json' #/path/to/serviceAccountCredentialsKeysFile.json

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '12slWO5HHOm-ep4keHYsLiJ92VPslj9cSnz3zyNG4m8Y'


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API to read from it
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sales!A1:F13").execute()
values = result.get('values', [])

# Call the Sheets API to write to it
aoa =[["1/1/2020",4000],["2/2/2021",5000],["3/3/2021",6000]]

#USER_ENTERED - The values will be parsed as if the user typed them into the UI.

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                               range="BotWriteToHere!B2", valueInputOption="USER_ENTERED", body={"values":aoa}).execute()



print(request)

print(values)

