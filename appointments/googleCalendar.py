from datetime import timedelta
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from django.conf import settings


scopes = ['https://www.googleapis.com/auth/calendar']
# flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
# credentials = flow.run_console()
# pickle.dump(credentials, open("token.pkl", "wb"))
credentials = pickle.load(open("appointments/token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)
result = service.calendarList().list().execute()

# calendar_id = settings.DEFAULT_FROM_EMAIL
calendar_id = result['items'][0]['id']
result = service.events().list(calendarId=calendar_id, timeZone="Europe/London").execute()


def addGoogleCalendarEvent(start_time_str, summary, description=None):
    start_time = start_time_str
    end_time = start_time + timedelta(hours=1)

    event = {
        'summary': f'Appointment for {summary}',
        'description': description,
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Europe/London',
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Europe/London',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 30},
            ],
        },
    }
    return service.events().insert(calendarId='primary', body=event).execute()
