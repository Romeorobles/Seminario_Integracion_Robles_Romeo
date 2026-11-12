# mp 10 - Ciclos while con tema LigaPro
# Autor: Romeo Robles

puntos = 0
while puntos < 15:
    print(f"Liga gana otro partido, lleva {puntos} puntos")
    puntos += 3
print(f"Liga llego a {puntos} puntos y es lider")

minuto = 90
while minuto > 80:
    print(f"Minuto {minuto}: Barcelona se defiende")
    minuto -= 2
print("Termina la presion final")

print("Continue y break")
fecha = 0
while fecha > -1:
    fecha += 1
    if fecha == 3:
        print("Fecha 3: suspendida por lluvia")
        continue
    print(f"Fecha {fecha}: se juega normal")
    if fecha == 6:
        print("Fin de la primera etapa")
        break

partido = 0
while partido < 10:
    partido += 1
    if partido == 4:
        print("Partido 4: el delantero esta suspendido, no juega")
        continue
    if partido == 7:
        print("Partido 7: el delantero se lesiona, se acaba su temporada")
        break
    print(f"El delantero juega el partido {partido}")
