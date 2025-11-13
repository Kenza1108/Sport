# models/FileStorage.py
import csv
from interfaces.storage_interface import StorageInterface


class FileStorage(StorageInterface):
    """Classe responsable de la gestion des fichiers CSV (lecture/écriture)."""

    def __init__(self, filename: str):
        self.filename = filename

    def save_dict_list(self, dict_list: list, fieldnames: list):
        """
        Enregistre une liste de dictionnaires dans un fichier CSV.
        Chaque dictionnaire représente un enregistrement (membre, événement, abonnement...).
        """
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
            writer.writeheader()
            writer.writerows(dict_list)
        print(f"💾 Données sauvegardées dans {self.filename}")

    def load_dict_list(self) -> list:
        """
        Charge les données d’un fichier CSV et les retourne sous forme de liste de dictionnaires.
        Si le fichier n’existe pas, retourne une liste vide.
        """
        data = []
        try:
            with open(self.filename, encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter="\t")
                for row in reader:
                    data.append(row)
            print(f"📂 {len(data)} enregistrements chargés depuis {self.filename}")
        except FileNotFoundError:
            print(f"⚠️ Fichier introuvable : {self.filename} — Création lors de la sauvegarde.")
        return data
