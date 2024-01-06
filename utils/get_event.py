from utils.auth import get_auth

from dateutil.parser import parse
import datetime

def get_upcoming_events(calendar_id, maxResults):
   service = get_auth()
   now = datetime.datetime.utcnow().isoformat() + "Z"
   events_result = (
       service.events()
       .list(
           calendarId=calendar_id,
           timeMin=now,
           maxResults=maxResults,
           singleEvents=True,
           orderBy="startTime",
       )
       .execute()
   )

   events = events_result.get("items", [])
   return events

def convert_time(time):
    dt = parse(time)
    formatted_time = dt.strftime("%I:%M %p")
    return formatted_time

def convert_date(time):
    dt = parse(time)
    formatted_date = dt.strftime('%Y-%m-%d')
    return formatted_date