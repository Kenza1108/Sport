from abc import ABC, abstractmethod

class EventInterface(ABC):
    @abstractmethod
    def display_html_row(self):
        """Return HTML row for the event"""
        pass

    @abstractmethod
    def describe(self):
        """Return textual description of the event"""
        pass

    @abstractmethod
    def to_dict(self):
        """Return dictionary representation of the event"""
        pass

    @abstractmethod
    def schedule(self):
        """Schedule the event"""
        pass
