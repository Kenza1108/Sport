import csv
from models.events import Event

class EventRepository:
    def __init__(self, filepath="data/events.csv"):
        self.filepath = filepath
        self.events = []
        self.load_events()

    def load_events(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter='\t')
                for row in reader:
                    if any(e.event_name == row["event_name"] for e in self.events):
                        continue
                    try:
                        event = Event(
                            event_name=row["event_name"],
                            description=row.get("description", ""),
                            event_date=row["event_date"],
                            organizer=row.get("organizer", ""),
                            participants=row.get("participants", "")
                        )
                        self.events.append(event)
                    except KeyError as e:
                        print(f"⚠️ Missing column in CSV: {e}")
            print(f"📂 {len(self.events)} event(s) loaded from file.")
        except FileNotFoundError:
            print("⚠️ No events file found, starting empty.")
        except Exception as e:
            print(f"❌ Error loading events: {e}")

    def save_events(self):
        try:
            with open(self.filepath, "w", encoding="utf-8", newline="") as f:
                fieldnames = ["event_name", "description", "event_date", "organizer", "participants"]
                writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
                writer.writeheader()
                for e in self.events:
                    writer.writerow({
                        "event_name": e.event_name,
                        "description": e.description,
                        "event_date": e.event_date,
                        "organizer": e.organizer,
                        "participants": e.participants
                    })
            print("💾 Events saved successfully.")
        except Exception as e:
            print(f"❌ Error saving events: {e}")

    def add_event(self, event: Event):
        if any(e.event_name == event.event_name for e in self.events):
            print(f"⚠️ Event '{event.event_name}' already exists.")
            return
        self.events.append(event)
        self.save_events()
        print(f"✅ Event '{event.event_name}' added successfully.")

    def get_all_events(self):
        return self.events

    def find_event_by_name(self, name: str):
        for e in self.events:
            if e.event_name.lower() == name.lower():
                return e
        return None

    def remove_event(self, name: str):
        event = self.find_event_by_name(name)
        if event:
            self.events.remove(event)
            self.save_events()
            print(f"🗑️ Event '{name}' removed successfully.")
            return True
        return False
