# mp 09 - Ciclos for con tema LigaPro
# Autor: Romeo Robles

for fecha in range(1, 6):
    print(f"Se juega la fecha {fecha} de la LigaPro")

print("Puntos acumulados por victorias")
for victorias in range(1, 11):
    print(f"{victorias} victorias x 3 = {victorias * 3} puntos")

print("Tabla de goles por equipo y partido")
for equipo in range(1, 4):
    print(f"Equipo {equipo}")
    for partido in range(1, 4):
        print(f"  Partido {partido}: {equipo * partido} goles")

equipos = [
    {"id": 1, "nombre": "Liga de Quito", "puntos": 55},
    {"id": 2, "nombre": "Barcelona SC", "puntos": 52},
    {"id": 3, "nombre": "Aucas", "puntos": 30},
]

for equipo in equipos:
    print(equipo)

goleadores = {
    "Alex Arce": 22,
    "Janner Corozo": 12,
    "Michael Hoyos": 9,
    "Jordy Caicedo": 15,
}

for nombre, goles in goleadores.items():
    if goles >= 15:
        print(f"{nombre} pelea la Bota de Oro")
    else:
        print(f"{nombre} necesita mas goles")

print("Break y Continue")
for nombre in goleadores:
    if nombre == "Michael Hoyos":
        break
    if nombre == "Alex Arce":
        continue
    print(f"Goleador: {nombre}")
