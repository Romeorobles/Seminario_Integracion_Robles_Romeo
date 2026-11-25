class Guerrero:
    nombre: str
    __poder: int

    def __init__(self, nombre:str, poder:int):
        self.nombre = nombre
        self.__poder = poder

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Poder ", self.__poder)

goku = Guerrero("Goku", 9000)
vegeta = Guerrero("Vegeta", 6000)
piccolo = Guerrero("Piccolo", 10000)
romeo = Guerrero("Romeo", 5000)

goku.mostrar_info()
vegeta.mostrar_info()
piccolo.mostrar_info()
romeo.mostrar_info()
