# 8-Puzzle — Busca em Espaço de Estados

## O que implementar

### `puzzle/state.py`
- `neighbors()` — gera os estados filhos a partir do espaço vazio
- `path()` — reconstrói a sequência de estados do inicial até este
- `actions()` — retorna a sequência de ações usando `path()`

### `algorithms/bfs.py`
- `BFS.search(initial)` — Busca em Largura

### `algorithms/dfs.py`
- `DFS.search(initial)` — Busca em Profundidade

### `algorithms/a_star.py`
- `AStar.heuristic(state)` — função heurística admissível
- `AStar.search(initial)` — Busca A*

## Estrutura

```
├── puzzle/
│   ├── state.py        # State — IMPLEMENTAR neighbors, path, actions
│   ├── result.py       # SearchResult — não alterar
│   └── base_search.py  # Interface BaseSearch — não alterar
├── algorithms/
│   ├── bfs.py          ← IMPLEMENTAR
│   ├── dfs.py          ← IMPLEMENTAR
│   └── a_star.py       ← IMPLEMENTAR
└── main.py
```

