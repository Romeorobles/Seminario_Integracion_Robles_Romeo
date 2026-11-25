# mp 03 - Input con tema LigaPro
# Autor: Romeo Robles

print("Registro de hincha de la LigaPro")
nombre_hincha = input("Ingrese su nombre: ")
equipo = input("De que equipo es hincha?: ")
print("Hola", nombre_hincha, "bienvenido, hincha de", equipo)
print("Hasta luego " + nombre_hincha)

# input() siempre devuelve str, hay que convertir
goles = int(input("Cuantos goles hizo su equipo la fecha pasada? "))
total = goles + 2
print("Si mete 2 mas, llegaria a:", total)

print("CONVERSIONES")
print("=== BOLETERIA DEL ESTADIO ===")
cantidad = int(input("Cuantas entradas quiere? "))
precio = float(input("Precio de la entrada: "))
total_pagar = cantidad * precio
print(nombre_hincha, "el total a pagar es (round):", round(total_pagar, 2))
print(f"Total a pagar (f): {total_pagar:.2f}")
