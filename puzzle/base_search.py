from abc import ABC, abstractmethod
from puzzle.state import State
from puzzle.result import SearchResult


class BaseSearch(ABC):
    """Interface que todos os algoritmos de busca devem implementar.

    Regras:
      - `search` deve retornar um `SearchResult`.
      - Não modifique a assinatura de `search`.
      - Algoritmos informados recebem `heuristic` como callable opcional.
    """

    @abstractmethod
    def search(self, initial: State) -> SearchResult:
        """Executa a busca a partir do estado inicial e retorna o resultado."""
        ...
