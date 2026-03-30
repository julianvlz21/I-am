##Programa para validar si un número es divisible por 5

# num = int(input("Enter a number to know if to be divided by 5: "))
# last_digit = num % 10

# if last_digit == 5 or last_digit == 0:
#     print ("Your number is divide for 5")

# else:
#     print("This number don't to be divided by 5")

##Program for know if a number is multiple of other (3) in this case

# num = int(input("Enter a number to know if to it's multiple of 3: "))
# multiple = int(3)

# if num % multiple == 0:
#     print(f"({num}) This number is mulpile of 3")

# else:
#      print(f"({num}) This number don't to be multiple of 3")


# import csv 

# archivo = csv

# with (archivo, 'a', encoding="utf-8") as f:
#     save = 

#program for know zodiacal sign 

# day = int(input("Enter the day of birth: "))
# month = int(input("Enter the month of birth: "))



# if (day >= 21 and month == 1) or (day <= 19 and day == 2):
#     print("Acuario not worth cock")
# elif (day >= 20 and month == 2) or (day <= 20 and day == 3):
#     print("Picis not worth cock")
from time import sleep

# suma = 0
# for i in range (0,31,3):
#     # print
#     # print (f"The total sum of 1 to 10 is: {suma}")
#     print (i)
#     sleep (0.2)

# sentence = input("Enter a short sentence: ").lower()
# # works = list(sentence)
# a = 0 
# for n in works:
#     if n == "a":
#         a += 1
# print (a)
# d = ("Dormamu he venido para negociar")
# e = (d.split())


# for i in range (1):
#     print (f"\n{e[0]}\n{e[1]}\n{e[2]}\n{e[3]}\n{e[4]}")

# counter = [10]
# suma = 0
# i = 0
# while i <= 10:

#     suma += i
#     i = i + 1
#     print (suma)

# opcion= int(input("Enter a number: "))
# while opcion < 0:
#     opcion= int(input("Enter a number: "))

# print("Excelent")

# opcion = 0
# while opcion !=3:
#     print("MENÚ")
#     print("\n1. sdsd")
#     print("2. sdsd")
#     print("3. sdsd")

#     opcion = int(input("Escribe un número cv: "))
# print("Se cerró esa kg")

import random

# n = random.randint(1,10)
# print(n)
# adivina = 0

# while adivina != n:
#     adivina = int(input("Adivina el número entre 1 y 10: "))
#     if adivina < n:
#         print("El número debe ser mayor")
#     elif adivina > n:
#         print("El número debe ser menor")
# print("Melo")

# palabra = input("palabra: ")
# contador = 0
# i = 0

# while i < len(palabra):
#     if palabra[i].lower() in "aeiou":
#         contador += 1
#     i += 1
# print(f"número de vocales {contador}")

# password = ("python123")
# write = input("You write a password to enter: ")

# while write != password:
#     print("\nThe password is incorret")
#     write = input("You write a passworf to enter: ")

# print("Melo")

##PROGRAM TO PARKING WITH 10 SPACES 

#MENU FOR USER
# plates = ["libre"]*10

# option = None
# while True:
#     print("\n", "-" *15, "WELCOME TO THE PARKING", "-" *15)
#     print("\n1. Show the number of spaces avalibles\n2. Enter your car\n3. Take out your car\n4. Exit menu")

#     option = input("You select an option: ")
# #Show the number of availables spaces 
#     occupied = len(plates)
#     spaces = occupied - len(plates)
#     if option == "1":
#         # print(f"\nIn the parking there are {spaces} occupieds spaces")
#         # print(f"There are {occupied} availables spaces in the parking")
#         for idx, plate in enumerate(plates):
#             print (f"In the spaces {idx+1}. is the car with the plate: {plate}")
# #Enter the car to the parking:    
#     elif option == "2":
#         new = input("Enter the plate of your car: ")
#         for idx, change in enumerate(plates):
#             if change == "libre":
#                 plates[idx] = new
#             break

#     elif option == "3":
#         print (plates.copy())
#         exit = input("Take out your car: ")
#         plates.remove(exit)
###

# Client management system
# This module allows registering clients with validation

##### inventario = []
# contador = 0
# def agregar_productos(contador, nombre, precio, cantidad_):#Se crea un diccioanrio que gruarde los valores para cada producto, para posteriormente agregar el producto a la lista
#     producto = {
#         "id": contador,
#         "nombre": nombre,
#         "precio": precio,
#         "cantidad": cantidad_
#     }

#     inventario.append(producto)
#     print("\n\033[1;32m===============¡¡¡Registro exitoso!!!===============\033[0m")

# def mostrar_inventario(inventario):
#     if not inventario:
#         print("\n\033[34mInventario vacio\033[0m")
#     else:
#         for producto in inventario:
#             print(f"\033[34m{producto['id']}.\033[0m Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

# def calcular_estadisticas(inventario):
#     total_precio = sum(valor['precio']*valor['cantidad']for valor in inventario)
#     print(f"El valor total de los productos: \033[1;32m${total_precio}\033[0m")

#     total_inventario = sum(cantidad['cantidad']for cantidad in inventario)
#     print (f"Hay \033[1;32m{total_inventario}\033[0m productos en el inventario")

# #Validaciones de errores
# def si_vacio (valor):
#     return valor == ""

# def si_0_negativo(valor):
#     return int(valor) <= 0

# #menú para usuario
# while True:
#     print("\n\033[1;34m------------------------MENÚ REGISTRO INVENTARIO------------------------\033[0m")
#     print("""
#     \033[1;34m 1.\033[0m Agregar producto
#     \033[1;34m 2.\033[0m Mostrar inventario
#     \033[1;34m 3.\033[0m Calcular estadísticas
#     \033[1;34m 4.\033[0m Salir

# """)    
#     opcion = input("Selecciona una de las opciones: ")

#     if opcion == "1":
#         # print("\033[32m CAPACIDAD PARA 20 PRODUCTOS\033[0m") 
#         cantidad = input("\nCuántos producto va a agregar: ")
#         while not cantidad.isdigit():
#             print("\n\033[1;31m ¡¡¡Valor invalido, intenta de nuevo!!!\033[0m")
#             cantidad = input("\nCuántos producto va a agregar: ")
            
#         if si_0_negativo (cantidad):
#             print("\n\033[1;31m =====!!!El valor no puede ser 0 o negaitivo¡¡¡=====\033[0m")
#         # elif int(cantidad) > 20:
#         #     print("\033[32m CAPACIDAD PARA 20 PRODUCTOS\033[0m")
#         else:
#             for n in range(int(cantidad)):
#                 while True:
#                     nombre = input("\nEscribe el nombre del productos: ")
#                     contador += 1
#                     try:
#                         precio = float(input("Agrega un precio al producto: "))
#                         cantidad_= int(input("Escribe la cantidad de productos |valor entero|: "))

#                         if si_vacio(nombre) or si_0_negativo(precio) or si_0_negativo(cantidad_):
#                             print("\n\033[1;31m =====!!!DATO ERRONEO¡¡¡=====\033[0m")
#                             continue
#                         else:
#                             break
#                     except:
#                         print("\n\033[1;31m¡¡¡Valor invalido, intente de nuenvo!!!\033[0m")
                    
#                 agregar_productos(contador, nombre, precio, cantidad_)
#                 # print(len(inventario))
    
#     elif opcion == "2":
#         mostrar_inventario(inventario)

#     elif opcion == "3":
#         calcular_estadisticas(inventario)

#     elif opcion == "4":
#         print ("\033[1;32m================PROGRAMA FINALIZADO================\033[0m")
#         break

#     else:
#         print("\n\033[1;31m =====!!!DATO ERRONEO¡¡¡=====\033[0m")

import csv


inventory = [{'name': 'rice white', 'price': 1000.00, 'quantity': 2},{'name': 'soap', 'price': 3000.00, 'quantity': 5}, {'name': 'meat', 'price': 9000.00, 'quantity': 5}]

def argregar_productos(name, price, quantity_, inventory):
    inventory.append({
        'name': name,
        'price': price,
        'quantity': quantity_
    })

def mostrar_inventario(inventory):
    if not inventory:
        print(f"\033[1;31mEmpty inventory\033[0m")
    else:
        for idx, products in enumerate(inventory):
            print(f"\033[1;34m{idx + 1}.\033[0m {products['name']} | price: \033[32m${products['price']}\033[0m | quantity: \033[34m{products['quantity']}\033[0m")
            
def calculate_statistic(inventory):
    total_price = sum(valeu['price']*valeu['quantity'] for valeu in inventory)
    print(total_price)

    total_quantity = sum(quantity['quantity'] for quantity in inventory)
    print(total_quantity)

    expensive_product = max(inventory, key=lambda e: e['price'])

def search_products(inventory, name_product):
    for product in inventory:
        if product['name'] == name_product:
            print(f"{product['name']} | price: ${product['price']} | quantity: {product['quantity']}")

        else:
            print("Product not found")


def save_inventory (inventory):
    header = True
    if not inventory:
        print("Empty inventory")
        
        return

    try:
        with open ("database.csv", "w", newline="") as db:

            if header:
                db.write("name, price, quantity\n")

            for product in inventory:
                line = f"{product['name']}, {product['price']}, {product['quantity']}\n"
                db.write(f"{line}\n")

            print("save inventory in database.csv")

        return
    except PermissionError:
        pass

# mostrar_inventario(inventory)
# calculate_statistic(inventory)
nombre = input("rice: ").lower()
search_products(inventory, nombre)
save_inventory(inventory)