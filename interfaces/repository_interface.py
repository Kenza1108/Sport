# interfaces/repository_interface.py
from abc import ABC, abstractmethod
from typing import List, Dict

class RepositoryInterface(ABC):
    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def get_all(self) -> List[Dict]:
        pass
