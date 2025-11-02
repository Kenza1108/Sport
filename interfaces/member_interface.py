# interfaces/member_interface.py
from abc import ABC, abstractmethod

class MemberInterface(ABC):
    @abstractmethod
    def display_html_row(self):
        """Return HTML row representation of the member"""
        pass

    @abstractmethod
    def to_dict(self):
        """Return member data as a dictionary"""
        pass

    @abstractmethod
    def register_member(self):
        """Register the member"""
        pass
