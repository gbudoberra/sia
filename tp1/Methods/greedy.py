from tp1.ColorGridStatus import ColorGridStatus
from tp1.Methods.search_method import SearchMethod
from tp1.Methods.PriorityQueue import PriorityQueue
from tp1.Methods.heuristics import heuristic_border_colors


class Greedy(SearchMethod):

    def __init__(self, initial_grid: ColorGridStatus, heuristic):
        super().__init__(initial_grid)
        self.priority_queue = PriorityQueue()
        self.heuristic = heuristic
        self.expanded_nodes = 0

    def get_next_node(self):
        return self.priority_queue.pop()

    def add_new_nodes(self, new_nodes):
        self.expanded_nodes += 1
        [self.priority_queue.push(node, self.heuristic(node)) for node in new_nodes]

    def remaining_nodes(self):
        return not self.priority_queue.is_empty()

    def boundary_nodes_size(self):
        return self.priority_queue.len()

    def get_nodes_exploded_size(self):
        return self.expanded_nodes

