# mp 12 - POO: clase con tema LigaPro
# Autor: Romeo Robles


class Equipo:
    nombre: str
    ciudad: str
    victorias: int
    empates: int

    def __init__(self, nombre: str, ciudad: str, victorias: int, empates: int):
        self.nombre = nombre
        self.ciudad = ciudad
        self.victorias = victorias
        self.empates = empates

    def puntos(self) -> int:
        return self.victorias * 3 + self.empates

    def mostrar_info(self):
        print(f"Equipo: {self.nombre}")
        print(f"Ciudad: {self.ciudad}")
        print(f"Puntos: {self.puntos()}")


liga = Equipo("Liga de Quito", "Quito", 15, 10)
barcelona = Equipo("Barcelona SC", "Guayaquil", 14, 10)

liga.mostrar_info()
barcelona.mostrar_info()
print(liga.nombre)
print(barcelona.nombre)
