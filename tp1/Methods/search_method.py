from tp1.Node import Node
from tp1.ColorGridStatus import ColorGridStatus
from abc import ABC, abstractmethod
from memory_profiler import profile


class SearchMethod(ABC):
    def __init__(self, initial_grid: ColorGridStatus):
        self._cost = None
        self._boundary_node = None
        self.root = Node(initial_grid, None)
        self._visited_nodes = set()

    # @profile
    def search_solution(self):
        self._visited_nodes = set()
        self.add_new_nodes([self.root])
        while self.remaining_nodes():
            current_node = self.get_next_node()
            if current_node.is_complete_state():
                self._cost = current_node.get_cost()
                self._boundary_node = self.boundary_nodes_size()
                return current_node
            son_nodes = []
            for son in current_node.explode_node():
                if son not in self._visited_nodes:
                    son_nodes.append(son)
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

    @abstractmethod
    def boundary_nodes_size(self):
        pass

    def get_cost(self):
        return self._cost
