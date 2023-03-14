from Node import Node
from collections import deque


class Graph:
    def __init__(self, initial_grid):
        self.root = Node(initial_grid)
        self.visitedNode = set()

    def get_solution_by_dfs(self):
        border_nodes = deque()
        border_nodes.append(self.root)
        while border_nodes:
            removed_node = border_nodes.popleft()
            if removed_node.grid_status.is_grid_complete():
                print("Solucion hallada")
            son_nodes = removed_node.explodeNode().getSons()
            border_nodes.extend(son_nodes)
