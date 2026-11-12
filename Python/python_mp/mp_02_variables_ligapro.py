# mp 02 - Variables con tema LigaPro
# Autor: Romeo Robles

equipo = "Liga de Quito"
puntos = 55
print(equipo)
print(puntos)

# Tipado con anotaciones (type hints)
ciudad: str = "Quito"
print(ciudad)

print("Tipo de variables")
print("Tipo Texto o String")
estadio = "Rodrigo Paz Delgado"
print(estadio)
print(type(estadio))

print("Tipo de variable Entera")
goles_a_favor = 48
print(goles_a_favor)
print(type(goles_a_favor))

print("Tipo de variable Decimal o Float")
promedio_goles = 1.6
print(promedio_goles)
print(type(promedio_goles))

print("Tipo de variable Bool")
clasificado_libertadores = True
print("Clasificado a Libertadores:", clasificado_libertadores)
print(type(clasificado_libertadores))

victorias = 15
print("victorias")
print(victorias)
victorias = victorias + 1
print("victorias despues de ganar el clasico")
print(victorias)
victorias += 2
print("victorias despues de dos fechas mas")
print(victorias)
