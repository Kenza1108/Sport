import csv
from interfaces.storage_interface import StorageInterface

class FileStorage(StorageInterface):
    def __init__(self, filename):
        self.filename = filename

    def save_dict_list(self, dict_list, fieldnames):
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
            writer.writeheader()
            writer.writerows(dict_list)

    def load_dict_list(self):
        data = []
        try:
            with open(self.filename, encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter="\t")
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            pass
        return data
