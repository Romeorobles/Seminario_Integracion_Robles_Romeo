# mp 15 - POO: polimorfismo con tema LigaPro
# Autor: Romeo Robles


class Jugador:
    nombre: str

    def __init__(self, nombre: str):
        self.nombre = nombre

    def jugar(self):
        print(f"{self.nombre} está en la cancha")


class Arquero(Jugador):
    def jugar(self):
        print(f"{self.nombre} ataja el penal")


class Defensa(Jugador):
    def jugar(self):
        print(f"{self.nombre} despeja el balón")


class Delantero(Jugador):
    def jugar(self):
        print(f"{self.nombre} remata al arco")


plantilla = [
    Jugador("Suplente"),
    Arquero("Alexander Domínguez"),
    Defensa("Ricardo Adé"),
    Delantero("Alex Arce"),
]

for jugador in plantilla:
    jugador.jugar()
