class Guerrero:
    nombre: str
    __poder: int
    def __init__(self, nombre: str, poder:int):
        self.nombre= nombre
        self.poder = poder

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Poder: {self.poder}")

goku = Guerrero("Goku", 2)
romeo = Guerrero("Romeo", 19283091280389213)

romeo.mostrar_info()
goku.mostrar_info()
print(romeo.nombre)
print(goku.nombre)
print(romeo.poder)
print(goku.poder)
