import gspread, smtplib
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
api_key = 'doorbell-198222-d6d70f86b538.json'

TO = '6143615267@messaging.sprintpcs.com'
SUBJECT = 'Your Doorbell'
gmail_sender = 'door4basile@gmail.com'
gmail_passwd = 'Bell4door' 

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