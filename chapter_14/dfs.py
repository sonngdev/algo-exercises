from typing import Dict
from chapter_14.graph import Graph
from chapter_14.vertex import Vertex


def DFS(g: Graph, u: Vertex, discovered: Dict):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
        DFS(g, v, discovered)

def construct_path(u: Vertex, v: Vertex, discovered: Dict):
    path = []
    if v in discovered:
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()
    return path
