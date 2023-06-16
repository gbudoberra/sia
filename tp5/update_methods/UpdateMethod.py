from abc import ABC, abstractmethod


class UpdateMethod(ABC):
    @abstractmethod
    def get_delta(self, gradient, layer):
        pass
