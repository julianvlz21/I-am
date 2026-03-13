##Inventario de tienda

#Se usa ciclo "while" con "True" para solicitar los datos de cada usuario, tambien se metio este bloque dentro de un 
# "try" y "except" en caso que lleguen a ingresar un valor erroneo

nombre = str(input("\nEscribe el nombre del productos: "))

while True:
    try:
        precio = float(input("Agrega un precio al producto: "))
        cantidad = int(input("Escribe la cantidad de productos: "))

        if precio < 0 or cantidad <= 0:
            print("El valor no puede ser 0 o negaitivo") 
            continue
    except:
        print("\n¡¡¡Valor invalido, intenta de nuenvo!!!")

#Se crea una varible que guarde el "costo_total" de la multiplicaión del "precio * cantdad" y se imprimen los valores
# para que el usuario los vea la información del producto de manera organizada
    try:
        costo_total = precio * cantidad
        print(f"\nProducto: {nombre}")
        print(f"Precio unitario: ${precio} | Cantidad: {cantidad} | Costo total: ${costo_total}")
    except NameError:
        print ("")


