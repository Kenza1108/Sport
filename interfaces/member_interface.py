# interfaces/member_interface.py
from abc import ABC, abstractmethod
from typing import Dict


class MemberInterface(ABC):
    """Interface définissant les opérations principales d’un membre du club."""

    @abstractmethod
    def display_html_row(self) -> str:
        """
        Retourne la représentation HTML (ligne <tr>) du membre.
        Utilisée pour afficher les membres dans une table HTML.
        """
        pass

    @abstractmethod
    def to_dict(self) -> Dict:
        """
        Retourne les données du membre sous forme de dictionnaire.
        Sert pour la sauvegarde (CSV, JSON) ou la manipulation interne.
        """
        pass

    @abstractmethod
    def register_member(self) -> None:
        """
        Effectue l’enregistrement du membre (ajout dans la base de données ou fichier).
        """
        pass
