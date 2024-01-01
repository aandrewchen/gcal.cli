def create_event(service, calendar_id):
   event = {
       "summary": "Test",
       "description": "Test",
       "colorId": "3",
       "start": {
           "dateTime": "2023-12-30T09:00:00-07:00",
           "timeZone": "America/Los_Angeles",
       },
       "end": {
           "dateTime": "2023-12-30T17:00:00-07:00",
           "timeZone": "America/Los_Angeles",
       },
   }

   event = service.events().insert(calendarId=calendar_id, body=event).execute()
   print("Event created: %s" % (event.get("htmlLink")))