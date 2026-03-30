##Inventario de tienda
#Validaciones
# def si_vacio (valor):
#     return valor == ""

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
            cantidad = input("\nCuántos producto va a agregar: ")
            
        if si_0_negativo (cantidad):
            print("\n\033[1;31m =====!!!El valor no puede ser 0 o negaitivo¡¡¡=====\033[0m")
        elif int(cantidad) > 20:
            print("\033[32m CAPACIDAD PARA 20 PRODUCTOS\033[0m") 
        else:
            for n in range(int(cantidad)):
                while True:
                    nombre = input("\nEscribe el nombre del productos: ")
                    contador += 1
                    if not nombre:
                        print("\033[34m NOMBRE OBLIGATORIO\033[0m")
                        continue
                                        
                    try:
                        precio = float(input("Agrega un precio al producto: "))
                        cantidad_= int(input("Escribe la cantidad de productos: "))

                        if si_0_negativo(precio) or si_0_negativo(cantidad_):
                            print("\n\033[1;31m =====!!!El valor no puede ser 0 o negaitivo¡¡¡=====\033[0m")
                            continue
                        else:    
                            break
                    except:
                        print("\n¡¡¡Valor invalido, intente de nuenvo!!!")
                        
                producto = {
                    "id": contador,
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad_
                }
                inventario.append(producto)
                print(len(inventario))

            print("\n\033[1;32m===============¡¡¡Registro exitoso!!!===============\033[0m")

#mostrar el inventario de productos
    elif opcion == "2":
        #print (inventario)
        if not inventario:
            print("\n\033[34mInventario vacio\033[0m")
        else:
            for productos in inventario:
                print(f"\033[34m{productos['id']}.\033[0m Producto: {productos['nombre']} | Precio: {productos['precio']} | Cantidad: {productos['cantidad']}")
    
    elif opcion == "3":     
        total_precio=sum(valor['precio']*valor['cantidad']for valor in inventario)
        print(f"El valor total del inventario es: \033[1;32m${total_precio}\033[0m")

        total_inventario =sum(suma_inventario['cantidad']for suma_inventario in inventario)
        print (f"Hay {total_inventario} \033[1;32mproductos en el inventario\033[0m")

    elif opcion == "4":
        print("\n\033[34m ===============ADIOS===============\033[0m")
        break

    else:
        print("\n\033[1;31m¡¡¡Valor invalido, intente de nuenvo!!!\033[0m")
    #     buscar_producto = int(input("Introduce el ID a buscar: "))   
    #     for producto in inventario:
    #         if buscar_producto == producto['ID']:
    #             print(f"Producto: {producto['nombre']} | Precio: {producto['precio']}")
