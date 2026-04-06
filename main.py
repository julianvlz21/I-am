inventario = []

def agregar_productos(id, nombre, precio, cantidad):
    producto = {
        "id": id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("\n\033[1;32m===============¡¡¡Registro exitoso!!!===============\033[0")

def mostrar_inventario(inventario):
    if not inventario:
        print("\n\033[34mInventario vacio\033[0m")
    else:
        for producto in inventario:
            print(f"\033[34m{producto['id']}.\033[0m Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

def calcular_estadisticas(inventario):
    total_precio = sum(valor['precio']*valor['cantidad']for valor in inventario)
    print(total_precio)

    total_inventario = sum(cantidad['cantidad']for cantidad in inventario)
    print (total_inventario)
    


# agregar_productos(1, "lapiz", 1200, 8)
# agregar_productos(12, "borrador", 1300, 10)
# mostrar_inventario(inventario)

# calcular_estadisticas(inventario)