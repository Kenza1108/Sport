# factories/event_factory.py
from models.events import Meeting, Trip, Competition

class EventFactory:
    @staticmethod
    def create_event(event_type: str, **kwargs):
        if event_type == "meeting":
            return Meeting(**kwargs)
        elif event_type == "trip":
            return Trip(**kwargs)
        elif event_type == "competition":
            return Competition(**kwargs)
        else:
            raise ValueError(f"Unknown event type: {event_type}")
