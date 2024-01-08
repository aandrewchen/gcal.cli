from utils.auth import get_auth

def delete_event_by_id(calendar_id, id):
    service = get_auth()
    service.events().delete(calendarId=calendar_id, eventId=id).execute()
    return