from apiclient.discovery import build
import pickle
from datetime import datetime, timedelta

# Only need to run this code segment once (set a conditional if the pkl file exists)
#-----------------------------------------

from google_auth_oauthlib.flow import InstalledAppFlow
scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes=scopes)
credentials = flow.run_console()
pickle.dump(credentials, open("token.pkl", "wb"))

#-----------------------------------------

credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)
result = service.calendarList().list().execute()
calendar_id = result['items'][1]['id']
result = service.events().list(calendarId=calendar_id).execute()
result['items'][0]
start_time = datetime(2020, 9, 3, 6, 30, 0)
end_time = start_time + timedelta(hours=1)

# import this event dictionary(json) from a seperate file
event = {
  'summary': 'TEST EVENT',
  'location': 'margaritaville',
  'description': 'doobiedoobiedoooo',
  'start': {
    'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': 'America/Los_Angeles',
  },
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

service.events().insert(calendarId=calendar_id, body=event).execute()
