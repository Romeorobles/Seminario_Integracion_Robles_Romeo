# mp 16 - POO: clase abstracta con tema LigaPro
# Autor: Romeo Robles
from abc import ABC, abstractmethod


class Partido(ABC):
    local: str
    visita: str

    def __init__(self, local: str, visita: str):
        self.local = local
        self.visita = visita

    def mostrar_partido(self):
        print(f"{self.local} vs {self.visita}")

    @abstractmethod
    def puntos_por_victoria(self) -> int:
        pass


class PartidoDeLiga(Partido):
    def puntos_por_victoria(self) -> int:
        return 3


class Amistoso(Partido):
    def puntos_por_victoria(self) -> int:
        return 0


partidos = [
    PartidoDeLiga("Liga de Quito", "Barcelona SC"),
    Amistoso("Aucas", "Emelec"),
]

for partido in partidos:
    partido.mostrar_partido()
    print(f"Puntos por ganar: {partido.puntos_por_victoria()}")
