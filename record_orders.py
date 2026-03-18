clients = {}
auto_id = 1  # contador global

#----FUNCTION----
def register_client(clients, client_id, name, email, auto_id):
    """
    Register a new client in the system.

    Parameters:
        clients (dict): Dictionary where clients are stored
        client_id (str): Client identification (CC)
        name (str): Client name
        email (str): Client email

    Returns:
        tuple: (message, updated auto_id)
    """

    # VALIDATIONS

    # Validate empty fields
    if not client_id or not name or not email:
        return "Error: empty fields.", auto_id
    
     # Validate duplicate client
    if client_id in clients:
        return "Error: client already exists.", auto_id
    
    #Validate duplicate email
    for client in clients.values(): # Get all client data (ignore IDs)
        if client['email'] == email:
            return "Error: email already exists.", auto_id
    
    # Validate email format
    if "@" not in email or "." not in email: 
        return "Error: invalid email.", auto_id
    

    # SAVE CLIENT

    # Save client in dictionary
    clients[client_id] = {
        "auto_id": auto_id,
        "name": name,
        "email": email
    }

    # Increase auto-increment ID
    auto_id += 1

    return "Client registered successfully.", auto_id

#----MAIN PROGRAM----

#Ask user for data

while True:
    client_id = input("Enter CC: ")
    name = input("Enter full name: ")
    email = input("Enter email: ")

#Call function

    result, auto_id = register_client(clients, client_id, name, email, auto_id)

#Show result    

    print(result)

# Show saved client data of succssesful

    if result == "Client registered successfully.":
        print(f"\nClient registered:")
        print(f"System ID: {clients[client_id]['auto_id']}")
        print(f"CC: {client_id}")
        print(f"Name: {clients[client_id]['name']}")
        print(f"Email: {clients[client_id]['email']}\n")

        break
# 4. Solución Propuesta
# La solución consiste en desarrollar un módulo que permita registrar productos dentro del sistema utilizando estructuras de datos adecuadas.
# Los productos serán representados mediante **tuplas** y almacenados dentro de un **diccionario** para facilitar su acceso.
# Ejemplo de estructura:
# products = {
# product_id: (product_id, product_name, unit_price)
# }

# Esta estructura permite acceder rápidamente a los productos registrados.

def register_product(products):
    id_product = len (products) + 1
    name_product = input ('Enter the name of the product: ')
    price_product = float (input ('Enter the price of the product: '))
    products [id_product] = (id_product, name_product, price_product)
    products.update ({id_product : (name_product, price_product)})
    print (f'Product registered successfully. Total products: {len(products)+1}')
    print (f'Diccionario: {id_product} | Name: {name_product} | Price: {price_product}\n')

o=0
products = {}
while o == 0 :
    register_product(products)
    o= int(input ("You're new register? 0 for yes, 1 for no: "))

####----RECORD ORDERS----

orders = {}
order_auto_id = 1

def create_order(clients, products, orders, order_auto_id):
    print("\n--- CREATE ORDER ---")

    # VALIDATE CLIENT
    while True:
        client_id = input("Enter client CC: ")

        if client_id in clients:
            break
        else:
            print("Error: client does not exist. Try again.")

    # Create order structure
    order_detail = {}

    while True:
        #  VALIDATE PRODUCT ID
        while True:
            try:
                product_id = int(input("Enter product ID: "))

                if product_id in products:
                    break
                else:
                    print("Error: product does not exist. Try again.")
            except ValueError:
                print("Error: enter a valid number.")

     # 🔹 VALIDATE QUANTITY
        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    break
                else:
                    print("Error: quantity must be greater than 0.")
            except ValueError:
                print("Error: enter a valid number.")

        # Get product data
        product_data = products[product_id]

        # Save without using lists
        order_detail[product_id] = {
            "name": product_data[0],
            "price": product_data[1],
            "quantity": quantity
        }

        # VALIDATE CONTINUE OPTION
        while True:
            more = input("Add another product? (y/n): ").lower()

            if more in ["y", "n"]:
                break
            else:
                print("Error: enter 'y' or 'n'.")

        if more == "n":
            break

    # Save order
    orders[order_auto_id] = {
        "client_id": client_id,
        "products": order_detail
    }

    print(f"\nOrder {order_auto_id} created successfully.")
    order_auto_id += 1

order_auto_id = create_order(clients, products, orders, order_auto_id)