# models/events.py
from interfaces.event_interface import EventInterface

# --- Classe de base : Event ---
class Event(EventInterface):
    """Classe représentant un événement dans le club sportif."""

    def __init__(self, event_name, description, event_date, organizer, participants):
        self.event_name = event_name
        self.description = description
        self.event_date = event_date
        self.organizer = organizer
        self.participants = participants

    def describe(self):
        """Retourne une courte description de l’événement."""
        return f"Événement '{self.event_name}' organisé par {self.organizer} le {self.event_date}."

    def schedule(self):
        """Planifie un événement générique."""
        print(f"📅 Planification de l’événement '{self.event_name}' le {self.event_date}.")

    def to_dict(self):
        """Retourne une représentation dictionnaire de l’événement."""
        return {
            "event_name": self.event_name,
            "description": self.description,
            "event_date": self.event_date,
            "organizer": self.organizer,
            "participants": self.participants
        }

    def display_html_row(self):
        """Retourne une ligne HTML représentant l’événement."""
        return (
            f"<tr>"
            f"<td>{self.event_name}</td>"
            f"<td>{self.description}</td>"
            f"<td>{self.event_date}</td>"
            f"<td>{self.organizer}</td>"
            f"<td>{self.participants}</td>"
            f"</tr>"
        )


# --- Sous-classes spécialisées ---
class Trip(Event):
    """Sous-classe pour les voyages organisés."""
    def __init__(self, event_name, description, event_date, organizer, participants, location):
        super().__init__(event_name, description, event_date, organizer, participants)
        self.location = location

    def describe(self):
        return f"Voyage '{self.event_name}' vers {self.location} organisé par {self.organizer}."

    def schedule(self):
        print(f"📍 Planification du voyage '{self.event_name}' à {self.location} le {self.event_date}.")

    def display_html_row(self):
        return super().display_html_row()[:-5] + f"<td>{self.location}</td></tr>"


class Meeting(Event):
    """Sous-classe pour les réunions."""
    def __init__(self, event_name, description, event_date, organizer, participants, room):
        super().__init__(event_name, description, event_date, organizer, participants)
        self.room = room

    def describe(self):
        return f"Réunion '{self.event_name}' dans la salle {self.room}, organisée par {self.organizer}."

    def schedule(self):
        print(f"🏢 Planification de la réunion '{self.event_name}' (salle {self.room}) le {self.event_date}.")

    def display_html_row(self):
        return super().display_html_row()[:-5] + f"<td>{self.room}</td></tr>"


class Competition(Event):
    """Sous-classe pour les compétitions."""
    def __init__(self, event_name, description, event_date, organizer, participants, prize):
        super().__init__(event_name, description, event_date, organizer, participants)
        self.prize = prize

    def describe(self):
        return f"Compétition '{self.event_name}' avec prix '{self.prize}' organisée par {self.organizer}."

    def schedule(self):
        print(f"🏆 Planification de la compétition '{self.event_name}' (prix : {self.prize}) le {self.event_date}.")

    def display_html_row(self):
        return super().display_html_row()[:-5] + f"<td>{self.prize}</td></tr>"
    
# --- Fonction utilitaire ---
def display_event_details(event: Event):
    """Affiche les détails d’un événement quel que soit son type."""
    print("📘 Détails de l’événement :")
    print(f"Nom : {event.event_name}")
    print(f"Description : {event.description}")
    print(f"Date : {event.event_date}")
    print(f"Organisateur : {event.organizer}")
    print(f"Participants : {event.participants}")
    print("→", event.describe())
    event.schedule()
    print("-" * 40)
