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
# def generato_clients (limit):
#     client = 1

#     while client <= limit:
#         client * 7
#         client += 1 
# obaaaa = generato_clients(10)


# for c in (obaaaa):
#     print(c)
# # print(next(ob))
# # print("Kevin prince wuatem")
# # print(next(ob))

counter = 0

for q in range(1, 5):
    counter += 1
    print (counter)
