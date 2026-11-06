import heapq
from itertools import count
from puzzle.base_search import BaseSearch
from puzzle.state import State, GOAL_STATE
from puzzle.result import SearchResult

# Posição (linha, coluna) de cada peça no estado objetivo.
_GOAL_POS = {tile: divmod(i, 3) for i, tile in enumerate(GOAL_STATE)}


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        """Distância de Manhattan: soma, para cada peça (exceto o vazio), das
        linhas + colunas até sua posição no objetivo. É admissível porque cada
        movimento desloca uma única peça em uma casa."""
        total = 0
        for i, tile in enumerate(state.tiles):
            if tile == 0:
                continue
            r, c = divmod(i, 3)
            gr, gc = _GOAL_POS[tile]
            total += abs(r - gr) + abs(c - gc)
        return total

    def search(self, initial: State) -> SearchResult:
        result = SearchResult(solution=None, nodes_generated=1, max_frontier_size=1)

        tie = count()  # desempate estável (FIFO) entre nós com o mesmo f
        frontier = [(self.heuristic(initial), next(tie), initial)]
        best_g = {initial.tiles: 0}
        explored = set()

        while frontier:
            _, _, node = heapq.heappop(frontier)

            if node.tiles in explored:
                continue  # entrada obsoleta na fila

            # Teste de objetivo na expansão: garante a solução ótima.
            if node.is_goal:
                result.solution = node
                result.depth = node.cost
                return result

            explored.add(node.tiles)
            result.nodes_expanded += 1

            for child in node.neighbors():
                if child.tiles in explored:
                    continue
                if child.cost < best_g.get(child.tiles, float("inf")):
                    best_g[child.tiles] = child.cost
                    f = child.cost + self.heuristic(child)
                    heapq.heappush(frontier, (f, next(tie), child))
                    result.nodes_generated += 1

            result.max_frontier_size = max(result.max_frontier_size, len(frontier))

        return result
