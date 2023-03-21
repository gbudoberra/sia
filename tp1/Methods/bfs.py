from Methods.search_method import SearchMethod
from ColorGridStatus import ColorGridStatus
from queue import Queue


class Bfs(SearchMethod):

    def __init__(self, initial_grid: ColorGridStatus):
        super().__init__(initial_grid)
        self.expanded_nodes = 0
        self.queue = Queue()

    def get_next_node(self):
        return self.queue.get()

    def add_new_nodes(self, new_nodes):
        self.expanded_nodes += 1
        [self.queue.put(node) for node in new_nodes]

    def remaining_nodes(self):
        return not self.queue.empty()

    def boundary_nodes_size(self):
        return self.queue.qsize()

    def get_nodes_exploded_size(self):
        return self.expanded_nodes


