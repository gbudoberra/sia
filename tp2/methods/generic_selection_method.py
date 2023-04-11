from abc import ABC, abstractmethod


class GenericSelectionMethod(ABC):

    def __init__(self, size):
        self.new_generation_size = size

    @abstractmethod
    def _select_parents(self, population):
        pass
