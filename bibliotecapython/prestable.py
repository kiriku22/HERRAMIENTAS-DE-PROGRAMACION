from abc import ABC, abstractmethod

class Prestable(ABC):
    @abstractmethod
    def prestar(self):
        pass

    @abstractmethod
    def devolver(self):
        pass