# managers/event_repository.py

from models.events import Event
from interfaces.repository_interface import RepositoryInterface

class EventRepository(RepositoryInterface):
    def __init__(self):
        self.events = []

    # ---------------------------------------------
    # CREATE
    # ---------------------------------------------
    def add(self, event: Event):
        """Add a new event only if it does not already exist."""
        if any(e.event_name.lower() == event.event_name.lower() for e in self.events):
            print(f"⚠️ Event '{event.event_name}' already exists.")
            return False
        self.events.append(event)
        print(f"✅ Event '{event.event_name}' added.")
        return True

    # ---------------------------------------------
    # READ
    # ---------------------------------------------
    def get_all(self):
        return self.events

    def find_by_name(self, event_name: str):
        """Find an event by name (case-insensitive)."""
        for e in self.events:
            if e.event_name.lower() == event_name.lower():
                return e
        return None

    # ---------------------------------------------
    # UPDATE
    # ---------------------------------------------
    def update(self, event_name: str, new_event: Event):
        for i, e in enumerate(self.events):
            if e.event_name.lower() == event_name.lower():
                self.events[i] = new_event
                print(f"🔄 Event '{event_name}' updated.")
                return True
        print(f"⚠️ Event '{event_name}' not found for update.")
        return False

    # ---------------------------------------------
    # DELETE
    # ---------------------------------------------
    def delete(self, event_name: str):
        event = self.find_by_name(event_name)
        if event:
            self.events.remove(event)
            print(f"🗑️ Event '{event_name}' removed.")
            return True
        print(f"⚠️ Event '{event_name}' not found for deletion.")
        return False
