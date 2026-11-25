# mp 13 - POO: encapsulamiento con tema LigaPro
# Autor: Romeo Robles


class Club:
    nombre: str
    __presupuesto: int

    def __init__(self, nombre: str, presupuesto: int):
        self.nombre = nombre
        self.__presupuesto = presupuesto

    def recibir_premio(self, monto: int):
        if monto > 0:
            self.__presupuesto += monto

    def fichar(self, jugador: str, costo: int):
        if costo <= self.__presupuesto:
            self.__presupuesto -= costo
            print(f"{self.nombre} ficha a {jugador}")
        else:
            print(f"{self.nombre} no puede pagar a {jugador}")

    def mostrar_presupuesto(self):
        print(f"Presupuesto de {self.nombre}: {self.__presupuesto}")


liga = Club("Liga de Quito", 500000)
aucas = Club("Aucas", 100000)

liga.fichar("Alex Arce", 300000)
liga.recibir_premio(50000)
aucas.fichar("Janner Corozo", 250000)

liga.mostrar_presupuesto()
aucas.mostrar_presupuesto()
