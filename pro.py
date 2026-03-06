##PROGRAM TO PARKING WITH 10 SPACES
#Menu for user
plates = []
def place_cars (plates):
    for idx,plate in enumerate(plates):
        print(f"In parking space {idx+1}. is the car: {plate}")

while True:
    print("\n", "-" * 20, "WELCOME TO THE PARKING MENU", "-" * 20 )
    print("1. show the number of available spaces"
    "\n2. Enter your car in the parking"
    "\n3. Take out your car" \
    "\n4. Exit menu")
    option = int(input("Choose one of the options: "))
#Show the number of available spaces
    spaces = len(plates)
    occupied = 10 - spaces
    if option == 1:
        print(f"\nIn the parking there are {spaces} occupied spaces")
        print(f"There are {occupied} availables spaces")
        print(plates.copy())
        place_cars(plates)
#Enter the car to the parking
    elif option == 2:
        print(f"There are {occupied} availables spaces")
        new_car = input("Enter the places of your car: ")
        position= int(input("Selec the position: "))
        plates.insert(position, new_car)
        print(plates)
#Take out your car
    #elif option == 3:
        