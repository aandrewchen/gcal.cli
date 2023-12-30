import datetime

def get_upcoming_events(service, calendar_id):
   now = datetime.datetime.utcnow().isoformat() + "Z"
   events_result = (
       service.events()
       .list(
           calendarId=calendar_id,
           timeMin=now,
           maxResults=10,
           singleEvents=True,
           orderBy="startTime",
       )
       .execute()
   )

   events = events_result.get("items", [])
   return events