import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
api_key = 'doorbell-198222-d6d70f86b538.json' 

def connect_gs():
	credentials = ServiceAccountCredentials.from_json_keyfile_name(api_key, scope)
	gc = gspread.authorize(credentials)
	return gc.open("temphum").sheet1
