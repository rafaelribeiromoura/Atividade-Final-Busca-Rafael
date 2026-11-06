from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:
        """Busca em profundidade com limite (pilha explícita, sem recursão).

        Um estado só é reexpandido se for alcançado por um caminho mais raso
        do que o anterior; isso evita ciclos e garante que nenhum estado dentro
        do limite fique de fora por ter sido visto antes num ramo mais fundo.
        """
        result = SearchResult(solution=None, nodes_generated=1, max_frontier_size=1)

        stack = [initial]
        best_depth = {initial.tiles: 0}

        while stack:
            node = stack.pop()

            # Entrada obsoleta: o estado já foi alcançado por um caminho mais raso.
            if best_depth.get(node.tiles, node.cost) < node.cost:
                continue

            if node.is_goal:
                result.solution = node
                result.depth = node.cost
                return result

            if node.cost >= self.depth_limit:
                continue

            result.nodes_expanded += 1
            # Inverte para que o primeiro vizinho (UP) seja explorado primeiro.
            for child in reversed(node.neighbors()):
                known = best_depth.get(child.tiles)
                if known is not None and known <= child.cost:
                    continue
                best_depth[child.tiles] = child.cost
                stack.append(child)
                result.nodes_generated += 1

            result.max_frontier_size = max(result.max_frontier_size, len(stack))

        return result
