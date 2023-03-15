from Node import Node
import queue
from ColorGridStatus import ColorGridStatus


class Graph:
    def __init__(self, initial_grid: ColorGridStatus):
        self.root = Node(initial_grid)
        self._visited_nodes = set()

    def get_solution_by_dfs(self):
        self._visited_nodes = set()
        border_nodes = [self.root]
        while not border_nodes.empty():
            current_node = border_nodes.pop()
            if current_node.is_complete_state():
                print("Solucion hallada")
                return current_node
            son_nodes = [son for son in current_node.explode_node() if son not in self._visited_nodes]
            self._visited_nodes.update(son_nodes)
            border_nodes.queue.extend(son_nodes)
        print("No se encontró solución")
        return None
