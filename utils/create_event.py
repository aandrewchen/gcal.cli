from utils.auth import get_auth

def create_event(calendar_id, summary, color, startTime, endTime, isRecurring, days, endDate):
    service = get_auth()
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

    days_mapping = {
        "Monday": "MO",
        "Tuesday": "TU",
        "Wednesday": "WE",
        "Thursday": "TH",
        "Friday": "FR",
        "Saturday": "SA",
        "Sunday": "SU",
        "Everyday": "MO,TU,WE,TH,FR,SA,SU",
    }

    if isRecurring == "y":
        if days == "Everyday":
            freq = "DAILY"
        else:
            freq = "WEEKLY"
            days = ",".join([days_mapping[day] for day in days])

        recurrence = f"RRULE:FREQ={freq};UNTIL={endDate}T000000Z;BYDAY={days}"

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

    if isRecurring == "y":
        event["recurrence"] = [recurrence]
    
    # event = {
    #     'summary': 'Appointment',
    #     'start': {
    #         'dateTime': '2024-01-04T10:00:00.000-07:00',
    #         'timeZone': 'America/Los_Angeles'
    #     },
    #     'end': {
    #         'dateTime': '2024-01-04T10:25:00.000-07:00',
    #         'timeZone': 'America/Los_Angeles'
    #     },
    #     'recurrence': [
    #         'RRULE:UNTIL=20240201T170000Z;BYDAY=TH,FR',
    #     ],
    # }

    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    print("Event created: %s" % (event.get("htmlLink")))
    # print(days)