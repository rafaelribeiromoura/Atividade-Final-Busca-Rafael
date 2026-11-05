from __future__ import annotations
from typing import List, Optional, Tuple


GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Movimentos do espaço vazio: nome da ação -> (delta linha, delta coluna)
MOVES = (
    ("UP", -1, 0),
    ("DOWN", 1, 0),
    ("LEFT", 0, -1),
    ("RIGHT", 0, 1),
)


class State:
    """Representa um estado do 8-puzzle como tupla imutável de 9 inteiros (0 = espaço vazio)."""

    def __init__(self, tiles: Tuple[int, ...], parent: Optional["State"] = None, action: Optional[str] = None, cost: int = 0):
        if len(tiles) != 9 or set(tiles) != set(range(9)):
            raise ValueError("Estado inválido: deve conter exatamente os valores 0-8.")
        self.tiles = tiles
        self.parent = parent
        self.action = action
        self.cost = cost

    @property
    def is_goal(self) -> bool:
        return self.tiles == GOAL_STATE

    @property
    def is_solvable(self) -> bool:
        """Num tabuleiro 3x3, um estado alcança GOAL_STATE se e só se o número
        de inversões (ignorando o vazio) tiver a mesma paridade do objetivo."""
        def inversions(t: Tuple[int, ...]) -> int:
            seq = [x for x in t if x != 0]
            return sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq)) if seq[i] > seq[j])
        return inversions(self.tiles) % 2 == inversions(GOAL_STATE) % 2

    @property
    def blank_index(self) -> int:
        return self.tiles.index(0)

    def neighbors(self) -> List["State"]:
        """Retorna os estados filhos válidos a partir deste estado."""
        children: List["State"] = []
        blank = self.blank_index
        row, col = divmod(blank, 3)
        for action, dr, dc in MOVES:
            r, c = row + dr, col + dc
            if 0 <= r < 3 and 0 <= c < 3:
                target = r * 3 + c
                tiles = list(self.tiles)
                tiles[blank], tiles[target] = tiles[target], tiles[blank]
                children.append(State(tuple(tiles), parent=self, action=action, cost=self.cost + 1))
        return children

    def path(self) -> List["State"]:
        """Retorna a sequência de estados do estado inicial até este."""
        states: List["State"] = []
        node: Optional["State"] = self
        while node is not None:
            states.append(node)
            node = node.parent
        states.reverse()
        return states

    def actions(self) -> List[str]:
        """Retorna a sequência de ações do estado inicial até este."""
        return [s.action for s in self.path()[1:]]

    def __eq__(self, other: object) -> bool:
        return isinstance(other, State) and self.tiles == other.tiles

    def __hash__(self) -> int:
        return hash(self.tiles)

    def __lt__(self, other: "State") -> bool:
        return self.cost < other.cost

    def __repr__(self) -> str:
        t = self.tiles
        return (
            f"+-------+\n"
            f"| {t[0]} {t[1]} {t[2]} |\n"
            f"| {t[3]} {t[4]} {t[5]} |\n"
            f"| {t[6]} {t[7]} {t[8]} |\n"
            f"+-------+"
        ).replace("0", " ")
