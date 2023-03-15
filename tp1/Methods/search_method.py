from Node import Node
from ColorGridStatus import ColorGridStatus
from abc import ABC, abstractmethod


class SearchMethod(ABC):
    def __init__(self, initial_grid: ColorGridStatus):
        self.root = Node(initial_grid, None)
        self._visited_nodes = set()

    def search_solution(self):
        self._visited_nodes = set()
        self.add_new_nodes([self.root])
        while self.remaining_nodes():
            current_node = self.get_next_node()
            if current_node.is_complete_state():
                return current_node
            son_nodes = [son for son in current_node.explode_node() if son not in self._visited_nodes]
            self._visited_nodes.update(son_nodes)
            self.add_new_nodes(son_nodes)
        return None

    @abstractmethod
    def get_next_node(self):
        pass

    @abstractmethod
    def add_new_nodes(self, new_nodes):
        pass

    @abstractmethod
    def remaining_nodes(self):
        pass
