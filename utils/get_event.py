import datetime

def get_upcoming_events(service, calendar_id, maxResults):
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