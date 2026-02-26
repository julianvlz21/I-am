##PRUEBAS PARA GIT

while True:
    try:
        print ("\nPrueba \nIngresa dos números para restar")
        numero_1 = int(input("\nIntroduce el primer número entero: "))
        numero_2 = int(input("Introduce el segundo número entero: "))
        resta = numero_1 - numero_2
        if resta >= 0:
            print(f"\nLa resta de {numero_1} - {numero_2} es = {resta}")
            if resta == 13:
                    print ("¡¡¡¡AYYYYYYYY!!!!")

        elif resta < 0:
            print(f"\nLa resta de {numero_1} - {numero_2} es = {resta}")
    except ValueError:
     print("\nEscribe un número entero CV")