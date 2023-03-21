from Methods.search_method import SearchMethod
from ColorGridStatus import ColorGridStatus
from queue import LifoQueue


class Dfs(SearchMethod):
    def __init__(self,  initial_grid: ColorGridStatus):
        super().__init__(initial_grid)
        self.stack = LifoQueue()
        self.expanded_nodes = 0

    def get_next_node(self):
        self.expanded_nodes += 1
        return self.stack.get()

    def add_new_nodes(self, new_nodes):
        [self.stack.put(node) for node in new_nodes]

    def remaining_nodes(self) -> bool:
        return not self.stack.empty()

    def boundary_nodes_size(self):
        return self.stack.qsize()

    def get_nodes_exploded_size(self):
        return self.expanded_nodes
