from interfaces.event_interface import EventInterface

# --- Base Event class implementing Organizable ---
class Event(EventInterface):
    def __init__(self, event_name, description, event_date, organizer, participants):
        self.event_name = event_name
        self.description = description
        self.event_date = event_date
        self.organizer = organizer
        self.participants = participants

    def describe(self):
        return f"Event '{self.event_name}' organized by {self.organizer} on {self.event_date}."

    def display_html_row(self):
        return (
            f"<tr><td>{self.event_name}</td>"
            f"<td>{self.description}</td>"
            f"<td>{self.event_date}</td>"
            f"<td>{self.organizer}</td>"
            f"<td>{self.participants}</td></tr>"
        )

    def schedule(self):
        """Default scheduling for a generic event"""
        print(f"Scheduling event '{self.event_name}' on {self.event_date}.")
    def to_dict(self):
        return {
            "event_name": self.event_name,
            "description": self.description,
            "event_date": self.event_date,
            "organizer": self.organizer,
            "participants": self.participants
        }

# --- Subclasses ---
class Trip(Event):
    def __init__(self, event_name, description, event_date, organizer, participants, location):
        super().__init__(event_name, description, event_date, organizer, participants)
        self.location = location

    def describe(self):
        return f"Trip '{self.event_name}' to {self.location} organized by {self.organizer}."

    def display_html_row(self):
        return super().display_html_row()[:-5] + f"<td>{self.location}</td></tr>"

    def schedule(self):
        print(f"Scheduling trip '{self.event_name}' to {self.location} on {self.event_date}.")


class Meeting(Event):
    def __init__(self, event_name, description, event_date, organizer, participants, room):
        super().__init__(event_name, description, event_date, organizer, participants)
        self.room = room

    def describe(self):
        return f"Meeting '{self.event_name}' held in room {self.room} organized by {self.organizer}."

    def display_html_row(self):
        return super().display_html_row()[:-5] + f"<td>{self.room}</td></tr>"

    def schedule(self):
        print(f"Scheduling meeting '{self.event_name}' in room {self.room} on {self.event_date}.")


class Competition(Event):
    def __init__(self, event_name, description, event_date, organizer, participants, prize):
        super().__init__(event_name, description, event_date, organizer, participants)
        self.prize = prize

    def describe(self):
        return f"Competition '{self.event_name}' with prize '{self.prize}' organized by {self.organizer}."

    def display_html_row(self):
        return super().display_html_row()[:-5] + f"<td>{self.prize}</td></tr>"

    def schedule(self):
        print(f"Scheduling competition '{self.event_name}' with prize '{self.prize}' on {self.event_date}.")


# --- Function for LSP ---
def display_event_details(event: Event):
    print(" Event Details:")
    print(f"Name: {event.event_name}")
    print(f"Description: {event.description}")
    print(f"Date: {event.event_date}")
    print(f"Organizer: {event.organizer}")
    print(f"Participants: {event.participants}")
    print("Info:", event.describe())
    event.schedule()  # show scheduling (Organizable interface)
    print("-" * 40)
