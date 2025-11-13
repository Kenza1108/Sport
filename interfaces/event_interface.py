# interfaces/event_interface.py
from abc import ABC, abstractmethod
from typing import Dict


class EventInterface(ABC):
    """Interface définissant les méthodes de base d’un événement."""

    @abstractmethod
    def display_html_row(self) -> str:
        """
        Retourne une ligne HTML (<tr>) représentant l’événement.
        Utilisée pour l’affichage dans une table web.
        """
        pass

    @abstractmethod
    def describe(self) -> str:
        """
        Fournit une description textuelle de l’événement.
        Peut être utilisée pour les rapports ou les journaux.
        """
        pass

    @abstractmethod
    def to_dict(self) -> Dict:
        """
        Retourne une représentation de l’événement sous forme de dictionnaire.
        Sert pour la sauvegarde (CSV, JSON, base de données, etc.).
        """
        pass

    @abstractmethod
    def schedule(self) -> None:
        """
        Planifie l’événement (par exemple : ajouter à un calendrier ou une liste des événements à venir).
        """
        pass
