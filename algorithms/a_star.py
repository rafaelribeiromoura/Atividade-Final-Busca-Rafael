import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        # TODO: implemente a heurística aqui
        raise NotImplementedError

    def search(self, initial: State) -> SearchResult:
        # TODO: implemente o A* aqui
        raise NotImplementedError
