import gspread, smtplib
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
api_key = 'your-private-key.json'

TO = '##########@messaging.sprintpcs.com'
SUBJECT = 'Your Doorbell'
gmail_sender = ''
gmail_passwd = '' 

def connect_gs():
	try:
		credentials = ServiceAccountCredentials.from_json_keyfile_name(api_key, scope)
		gc = gspread.authorize(credentials)
		return gc.open("temphum").sheet1
	except:
		print("Couln't connect to Google Sheet")

def connect_ge():
	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.login(gmail_sender, gmail_passwd)
		return server
	except:
		print ("Couldn't connect to Google Mail")
