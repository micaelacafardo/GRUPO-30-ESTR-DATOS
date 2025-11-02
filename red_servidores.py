from collections import deque

class RedServidores:
    """Modela la red de servidores como grafo no dirigido."""

    def __init__(self):
        self._conexiones = {}

    def agregar_servidor(self, nombre):
        self._conexiones[nombre] = []

    def conectar(self, a, b):
        self._conexiones[a].append(b)
        self._conexiones[b].append(a)

    def bfs(self, inicio, destino):
        visitados = set()
        cola = deque([(inicio, [inicio])])
        while cola:
            actual, camino = cola.popleft()
            if actual == destino:
                return camino
            visitados.add(actual)
            for vecino in self._conexiones.get(actual, []):
                if vecino not in visitados:
                    cola.append((vecino, camino + [vecino]))
        return None