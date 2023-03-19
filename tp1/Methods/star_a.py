from tp1.ColorGridStatus import ColorGridStatus
from tp1.Methods.search_method import SearchMethod
from tp1.Methods.PriorityQueue import PriorityQueue
from tp1.Methods.heuristics import heuristic_grid_remaining_colors, heuristic_cells_pending_per_color_remaining


class StarA(SearchMethod):

    def __init__(self, initial_grid: ColorGridStatus):
        super().__init__(initial_grid)
        self.priority_queue = PriorityQueue()

    def get_next_node(self):
        return self.priority_queue.pop()

    def add_new_nodes(self, new_nodes):
        [self.priority_queue.push(node, heuristic_cells_pending_per_color_remaining(node) + node.cost) for node in new_nodes]

    def remaining_nodes(self):
        return not self.priority_queue.is_empty()
