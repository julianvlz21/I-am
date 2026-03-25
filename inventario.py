##Inventario de tienda
#Validaciones
# def si_vacio (valor):
#     return valor == False

def si_0_negativo(valor):
    return int(valor) <= 0

inventario = []
contador = 0
while True:
    print("\n\033[1;34m------------------------MENÚ REGISTRO INVENTARIO------------------------\033[0m")
    print("""
    \033[1;34m 1.\033[0m Agregar producto
    \033[1;34m 2.\033[0m Mostrar inventario
    \033[1;34m 3.\033[0m Calcular estadísticas
    \033[1;34m 4.\033[0m Salir

""")
    opcion = input("Seleccione una opción: ")
    producto = {}

    if opcion == "1":
        print("\033[32m CAPACIDAD PARA 20 PRODUCTOS\033[0m") 
        cantidad = input("\nCuántos producto va a agregar: ")
        while not cantidad.isdigit():
            print("\n\033[1;31m ¡¡¡Valor invalido, intenta de nuevo!!!\033[0m")
            cantidad = input("Cuántos producto va a agregar: ")
            
        if not cantidad:
            print("\n\033[1;31m =====!!!El valor no puede ser 0 o negaitivo¡¡¡=====\033[0m")
        elif int(cantidad) > 20:
            print("\033[32m CAPACIDAD PARA 20 PRODUCTOS\033[0m") 
        else:
            None

        for n in range(int(cantidad)):
            while True:
                nombre_pro = input("\nEscribe el nombre del productos: ")
                if not nombre_pro:
                    print("\033[34m NOMBRE OBLIGATORIO\033[0m")
                else:
                    None
                try:
                    precio = float(input("Agrega un precio al producto: "))
                    cantidad_pro= int(input("Escribe la cantidad de productos: "))

                    if si_0_negativo(precio) or si_0_negativo(cantidad_pro):
                        print("\n\033[1;31m =====!!!El valor no puede ser 0 o negaitivo¡¡¡=====\033[0m")
                    else:    
                        contador += 1
                        break
                except:
                    print("\n¡¡¡Valor invalido, intenta de nuenvo!!!")

            producto = {"ID": contador,
                "nombre": nombre_pro,
                "precio": precio,
                "cantidad": cantidad_pro
            }
            inventario.append(producto)
            print(len(inventario))

        print("\n\033[1;32m===============¡¡¡Registro exitoso!!!===============\033[0")

#mostrar el inventario de productos
    elif opcion == "2":
        #print (inventario)
        if not inventario:
            print("\n\033[34mInventario vacio\033[0m")

        for detalle in inventario:
            print(f"\033[34m{detalle['ID']}.\033[0m Producto: {detalle['nombre']} | Precio: {detalle['precio']} | Cantidad: {detalle['cantidad']}")
    
    elif opcion == "3":     
        total_precio=sum(valor['precio']*valor['cantidad']for valor in inventario)
        print(f"El valor total del inventario es: {total_precio}")

        total_inventario =sum(suma_inventario['cantidad']for suma_inventario in inventario)
        print (f"Hay {total_inventario} productos en el inventario")

    elif opcion == 4:
        print("\n\033[34m ===============ADIOS===============\033[0m")
        break

    else:
        print("\n\033[1;31m¡¡¡Valor invalido, intenta de nuenvo!!!\033[0m")
    #     buscar_producto = int(input("Introduce el ID a buscar: "))   
    #     for producto in inventario:
    #         if buscar_producto == producto['ID']:
    #             print(f"Producto: {producto['nombre']} | Precio: {producto['precio']}")

        


