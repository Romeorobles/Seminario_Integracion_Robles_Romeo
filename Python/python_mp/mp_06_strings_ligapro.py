"""
mp 06 - Manejo de cadenas con tema LigaPro
Autor: Romeo Robles
"""

equipo1 = "Liga de Quito"
print(f"Equipo 1: {equipo1}")
print(f"Tipo de datos: {type(equipo1)}")

equipo2 = "Barcelona SC"
print(f"Equipo 2: {equipo2}")
print(f"Tipo de datos: {type(equipo2)}")

print("Funciones comunes de texto")
print("Longitud de", equipo1, ":", len(equipo1))
print("Longitud de", equipo2, ":", len(equipo2))

print("Convertir mayusculas y minusculas")
grito = "Vamos Liga carajo"
print("Original:", grito)
print("Mayusculas:", grito.upper())
print("Minusculas:", grito.lower())

print("Reemplazo de substring")
resultado = "Liga gano el clasico contra Barcelona"
nuevo_resultado = resultado.replace("Barcelona", "Emelec")
print("Original:", resultado)
print("Modificado:", nuevo_resultado)

print("Separar con split")
equipos = "Liga,Barcelona,Independiente,Emelec,Aucas"
lista_equipos = equipos.split(",")
print(lista_equipos)
print("Primer equipo:", lista_equipos[0])
print("Ultimo equipo:", lista_equipos[-1])

print("Extraer subcadenas")
frase = "Independiente del Valle"
print("Primera palabra:", frase[0:13])
print("Ultima palabra:", frase[18:23])

print("Comprobaciones utiles")
codigo_jugador = "LDU10"
dorsal = "10"
apellido = "Arce"
print(codigo_jugador.isalnum())
print(dorsal.isdigit())
print(apellido.isalpha())
print(codigo_jugador.isdigit())
