# mp 14 - POO: herencia con tema LigaPro
# Autor: Romeo Robles


class Persona:
    nombre: str
    equipo: str

    def __init__(self, nombre: str, equipo: str):
        self.nombre = nombre
        self.equipo = equipo

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Equipo: {self.equipo}")


class Delantero(Persona):
    goles: int

    def __init__(self, nombre: str, equipo: str, goles: int):
        super().__init__(nombre, equipo)
        self.goles = goles

    def mostrar_goles(self):
        print(f"{self.nombre} lleva {self.goles} goles")


class Arquero(Persona):
    vallas_invictas: int

    def __init__(self, nombre: str, equipo: str, vallas_invictas: int):
        super().__init__(nombre, equipo)
        self.vallas_invictas = vallas_invictas

    def mostrar_vallas(self):
        print(f"{self.nombre} tiene {self.vallas_invictas} vallas invictas")


delantero = Delantero("Alex Arce", "Liga de Quito", 18)
arquero = Arquero("Alexander Domínguez", "Liga de Quito", 9)

delantero.mostrar_info()
delantero.mostrar_goles()
arquero.mostrar_info()
arquero.mostrar_vallas()
