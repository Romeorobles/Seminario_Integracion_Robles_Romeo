# mp 04 - Operadores con tema LigaPro
# Autor: Romeo Robles

victorias = 15
empates = 7
derrotas = 8
goles_favor = 48
goles_contra = 30

print("OPERADORES ARITMETICOS")
partidos = victorias + empates + derrotas
print(" + Partidos jugados:", victorias, "+", empates, "+", derrotas, "=", partidos)
print(" - Diferencia de gol:", goles_favor, "-", goles_contra, "=", goles_favor - goles_contra)
print(" * Puntos por victorias:", victorias, "* 3 =", victorias * 3)
print(" / Promedio de goles:", goles_favor, "/", partidos, "=", goles_favor / partidos)
print(" // Goles por partido (entero):", goles_favor, "//", partidos, "=", goles_favor // partidos)
print(" % Partidos sobrantes al dividir en 4 bloques:", partidos, "% 4 =", partidos % 4)
print(" ** Potencia:", 2, "**", 3, "=", 2 ** 3)

puntos = victorias * 3 + empates
print("Puntos totales:", puntos)

print("Tabla de puntos por victorias")
print("1 victoria =", 1 * 3, "puntos")
print("2 victorias =", 2 * 3, "puntos")
print("3 victorias =", 3 * 3, "puntos")
print("4 victorias =", 4 * 3, "puntos")
print("5 victorias =", 5 * 3, "puntos")

print("OPERADORES DE COMPARACION")
puntos_liga = 55
puntos_barcelona = 52
print(" == Igual:", puntos_liga, "==", puntos_barcelona, "=", puntos_liga == puntos_barcelona)
print(" != Diferente:", puntos_liga, "!=", puntos_barcelona, "=", puntos_liga != puntos_barcelona)
print(" < Menor:", puntos_liga, "<", puntos_barcelona, "=", puntos_liga < puntos_barcelona)
print(" > Mayor:", puntos_liga, ">", puntos_barcelona, "=", puntos_liga > puntos_barcelona)
print(" <= Menor o igual:", derrotas, "<=", 8, "=", derrotas <= 8)
print(" >= Mayor o igual:", victorias, ">=", 10, "=", victorias >= 10)

print("OPERADORES LOGICOS")
es_local = True
tiene_titulares = False

puede_ganar_facil = es_local and tiene_titulares
print("Gana facil (and):", puede_ganar_facil)

tiene_chance = es_local or tiene_titulares
print("Tiene chance (or):", tiene_chance)

print("No es local (not):", not es_local)
