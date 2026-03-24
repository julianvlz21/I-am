##Inventario de tienda
inventario = []
contador = 0
while True:
    print("------------------------MENÚ REGISTRO INVENTARIO------------------------")
    print("""
    1. Agregar producto
    2. Mostrar inventario
    3. Calcular estadísticas
    4. Salir

""")
    opcion = input("Seleccione una opción: ")
    producto = {}

    if opcion == "1":
        cantidad = input("Cuántos producto va a agregar: ")
        while not cantidad.isdigit():
            print("\n¡¡¡Valor invalido, intenta de nuenvo!!!")
            cantidad = input("Cuántos producto va a agregar: ")

        for n in range(int(cantidad)):
            while True:
                contador += 1
                nombre_pro = input("\nEscribe el nombre del productos: ")
                try:
                    precio = float(input("Agrega un precio al producto: "))
                    cantidad_pro= int(input("Escribe la cantidad de productos: "))
                except:
                    print("\n¡¡¡Valor invalido, intenta de nuenvo!!!")

                if precio < 0 or cantidad_pro <= 0:
                    print("El valor no puede ser 0 o negaitivo")
                else:
                    break

            producto = {"ID": contador,
                "nombre": nombre_pro,
                "precio": precio,
                "cantidad": cantidad_pro
            }
            inventario.append(producto)
            print(len(inventario))

        print("===============¡¡¡Registro exitoso!!!===============")

#mostrar el inventario de productos
    elif opcion == "2":
        #print (inventario)
        if not inventario:
            print("No hay stock")

        for detalle in inventario:
            print(f"{detalle['ID']}. Producto: {detalle['nombre']} | Precio: {detalle['precio']} | Cantidad: {detalle['cantidad']}")
    
    elif opcion == "3":

    # elif opcion == 4:
    #     buscar_producto = int(input("Introduce el ID a buscar: "))   
    #     for producto in inventario:
    #         if buscar_producto == producto['ID']:
    #             print(f"Producto: {producto['nombre']} | Precio: {producto['precio']}")

        


