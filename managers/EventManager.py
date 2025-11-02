from models.events import Event

class EventRepository:
    def __init__(self):
        self.events = []
    
    def add_event(self, event_name, description, event_date, organizer, participants):
        new_event =Event( event_name=event_name,description=description, event_date=event_date,
        organizer=organizer,participants=participants)
        self.events.append(new_event)
        print(f"✅ Event '{event_name}' added successfully.")

    def get_all_events(self):
        return self.events