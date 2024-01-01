def create_event(service, calendar_id, summary, color):
    color_mapping = {
        "Graphite": 8,
    }
   
    colorId = color_mapping[color]

    event = {
        "summary": summary,
        "description": "test",
        "colorId": colorId,
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