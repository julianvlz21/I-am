##Sistema para salchipapeeria, que muestre sus productos
from time import sleep
productos = []

cantidad = int(input("cuántos productos van a ingresar: "))

for a in range(cantidad):
    nombre = input(f"Qué producto va a ingresar {a+1}: ")
    costo = int(input(f"Qué costo tendrá el producto {a+1}: "))

    productos.append({
        "productos": nombre,
        "costo": costo
    })

local = input("Nonbre del locál: ").upper()
##VISTA USUARIO
print (f"\n---------------Bienvenidos a {local}---------------")
print ("\nMenú de pruductos")
for idx, menu in enumerate(productos):
    print(f"{idx+1}.{menu["productos"]}: ${menu["costo"]}")

##ENTRADA USUARIO
opcion = int(input("Qué producto va a llevar: "))
while opcion == len(productos):

    print("\n5. Para salir")
    if opcion == 1:
        cuantos = int(input(f"Cuantas {productos[0]['productos']} vas a llevar: "))
        for total in enumerate(productos):
            print ({'costo'[0]} * cuantos)


    elif opcion == 5:
        break
    