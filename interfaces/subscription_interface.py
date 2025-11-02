# interfaces/subscription_interface.py
from abc import ABC, abstractmethod

class SubscriptionInterface(ABC):
    @abstractmethod
    def display_html_row(self):
        """Return an HTML table row representing the subscription"""
        pass

    @abstractmethod
    def to_dict(self):
        """Return a dictionary representation of the subscription"""
        pass
