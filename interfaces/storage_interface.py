# interfaces/storage_interface.py
from abc import ABC, abstractmethod
from typing import List, Dict


class StorageInterface(ABC):
    """Interface définissant les opérations de stockage (lecture/écriture de données)."""

    @abstractmethod
    def save_dict_list(self, dict_list: List[Dict], fieldnames: List[str]) -> None:
        """
        Sauvegarde une liste de dictionnaires dans un fichier (CSV, JSON, etc.).
        Chaque dictionnaire représente un enregistrement d’un modèle.
        """
        pass

    @abstractmethod
    def load_dict_list(self) -> List[Dict]:
        """
        Charge les données depuis un fichier et les retourne sous forme de liste de dictionnaires.
        """
        pass
