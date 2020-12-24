from datetime import timedelta
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from django.conf import settings

calendar_id = settings.DEFAULT_FROM_EMAIL


""" Code for working with google calendar api take and modified from the following sources:
    https://gist.github.com/nikhilkumarsingh/8a88be71243afe8d69390749d16c8322
    https://learndataanalysis.org/google-py-file-source-code/
    https://stackoverflow.com/questions/45051157/modifying-google-calendar-api-to-accept-environment-variables-rather-than-a-json
    https://developers.google.com/calendar/quickstart/python """


def getGoogleCalendarService():
    """ links to google calendar api and gets google calendar """
    API_SERVICE_NAME = 'calendar'
    API_VERSION = 'v3'
    CLIENT_SECRET_FILE = 'client_secret.json'
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    creds = None
    token = 'token.pkl'

    if os.path.exists(token):
        with open(token, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server()

        with open('token.pkl', 'wb') as token:
            pickle.dump(creds, token)
    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=creds)
        return service
    except Exception as e:
        print(e)
        return None


def addGoogleCalendarEvent(start_time_str, name, email, description=None):
    """ When appointment is added on site calendar adds corresponding event on google calendar """
    start_time = start_time_str
    end_time = start_time + timedelta(hours=1)

    event = {
        'summary': f'Appointment for {name}',
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
        'attendees': [
            {'displayName': name, 'email': email, 'responseStatus': 'accepted'}
        ],
        'colorId': '5',
        'backgroundColor': '#e3b72f',
        'foregroundColor': '#212529',
        'status': 'confirmed'
    }
    googleCalendarEvent = {}
    service = getGoogleCalendarService()
    googleCalendarEvent = service.events().insert(calendarId=calendar_id, sendNotifications=True, body=event).execute()
    return googleCalendarEvent


def updateGoogleCalendarEvent(start_time_str, name, email, eventId, description=None):
    """ When appointment is updated on site calendar updates corresponding event on google calendar """
    start_time = start_time_str
    end_time = start_time + timedelta(hours=1)

    event = {
        'summary': f'Appointment for {name}',
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
        'attendees': [
            {'displayName': name, 'email': email, 'responseStatus': 'accepted'}
        ],
        'colorId': '5',
        'backgroundColor': '#e3b72f',
        'foregroundColor': '#212529',
        'status': 'confirmed'
    }
    service = getGoogleCalendarService()
    updateEvent = service.events().update(calendarId=calendar_id, sendNotifications=True, eventId=eventId, body=event).execute()
    return updateEvent


def deleteGoogleCalendarEvent(eventId):
    """ When appointment is deleted from site calendar deletes corresponding event from google calendar """
    service = getGoogleCalendarService()
    deleteEvent = service.events().delete(calendarId=calendar_id, eventId=eventId).execute()
    return deleteEvent
