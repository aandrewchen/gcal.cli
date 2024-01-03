from datetime import datetime, timedelta

def create_event(service, calendar_id, summary, color, startTime, endTime):
    color_mapping = {
        "Lavendar": 1,
        "Sage": 2,
        "Grape": 3,
        "Flamingo": 4,
        "Banana": 5,
        "Tangerine": 6,
        "Peacock": 7,
        "Graphite": 8,
        "Blueberry": 9,
        "Basil": 10,
        "Tomato": 11,
    }
   
    colorId = color_mapping[color]

    event = {
        "summary": summary,
        "colorId": colorId,
        "start": {
            "dateTime": startTime,
            "timeZone": "America/Los_Angeles",
        },
        "end": {
            "dateTime": endTime,
            "timeZone": "America/Los_Angeles",
        },
    }

    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    print("Event created: %s" % (event.get("htmlLink")))