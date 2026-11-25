print("Incluir Datos con input()")
nombre_usuario = input("Ingrese su nombre: ")
print("Hola", nombre_usuario, "Bienvenido a la clase de Python")
print("Bienvenido al sistema")

print("Hasta luego " + nombre_usuario)


cantidad = int(input("Cuantas rosquillas hay? "))
total = cantidad + 2
print("Rosquillas totales: ", total)

print("CONVERSIONES")

print("=== TIENDA DE APU ===")
nombre_cliente = input("Ingrese su nombre: ")
precio = float(input("Precio de rosquillas: "))
total = cantidad * precio
print(nombre_cliente, "el total a pagar es: (roud):", round(total, 2))
print(f"total a pagar (f): {total:.2f}")