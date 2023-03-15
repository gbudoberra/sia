import heapq


class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._heap)[-1]

    def is_empty(self):
        return len(self._heap) == 0
