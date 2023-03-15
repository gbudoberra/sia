from tp1.Methods.search_method import SearchMethod
from tp1.ColorGridStatus import ColorGridStatus
from queue import Queue


class Bfs(SearchMethod):

    def __init__(self, initial_grid: ColorGridStatus):
        super().__init__(initial_grid)
        self.queue = Queue()

    def get_next_node(self):
        return self.queue.get()

    def add_new_nodes(self, new_nodes):
        [self.queue.put(node) for node in new_nodes]

    def remaining_nodes(self):
        return not self.queue.empty()
