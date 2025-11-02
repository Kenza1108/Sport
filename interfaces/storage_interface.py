from abc import ABC, abstractmethod

class StorageInterface(ABC):
    @abstractmethod
    def save_dict_list(self, dict_list, fieldnames):
        pass

    @abstractmethod
    def load_dict_list(self):
        pass
