from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from puzzle.state import State


@dataclass
class SearchResult:
    """Resultado padronizado retornado por qualquer algoritmo de busca."""

    solution: Optional[State]           # Estado objetivo (None se não encontrado)
    nodes_expanded: int = 0             # Quantos nós foram expandidos
    nodes_generated: int = 0            # Quantos nós foram gerados (incluindo os não expandidos)
    max_frontier_size: int = 0          # Tamanho máximo da fronteira durante a busca
    depth: int = 0                      # Profundidade da solução

    @property
    def found(self) -> bool:
        return self.solution is not None

    @property
    def actions(self) -> List[str]:
        return self.solution.actions() if self.found else []

    @property
    def path_cost(self) -> int:
        return self.solution.cost if self.found else -1
