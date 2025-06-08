from abc import ABC, abstractmethod

class BaseScraper(ABC):
    @abstractmethod
    def fetch(self):
        pass

    @property
    @abstractmethod
    def source(self):
        pass
