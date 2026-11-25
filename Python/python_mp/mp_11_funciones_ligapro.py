# mp 11 - Funciones con tema LigaPro
# Autor: Romeo Robles

print("Funciones")


def himno_liga():
    print("Liga, Liga, Liga")
    print("Vamos Liga de mi corazon")


himno_liga()


def anotar_gol(jugador):
    print(f"Goooool de {jugador}!")


anotar_gol("Alex Arce")
anotar_gol("Janner Corozo")


def calcular_puntos(victorias, empates):
    return victorias * 3 + empates


print(f"Liga tiene {calcular_puntos(15, 7)} puntos")


def clasificar(equipo: str, puntos: int):
    if puntos >= 50:
        print(f"{equipo} clasifica a Libertadores")
    else:
        print(f"{equipo} no alcanza Libertadores")


clasificar("Liga de Quito", 55)
clasificar("Aucas", 30)


def promedio_goles(goles: int, partidos: int) -> float:
    return goles / partidos


print(f"Promedio de goles: {promedio_goles(48, 30):.2f}")
