clients = {'12357': {'auto_id': 1, 'name': 'aura alean', 'email': 'shajd@gmail.com'},
            '2345678': {'auto_id': 2, 'name': 'max aleans', 'email': 'maxaleam@gmail.com'}}

products = {1: ('luis', 500.0, 5), 2: ('pozzo', 800.0, 20)}
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
        order_detail = {

        }

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

            orders[order_auto_id] = {
                "client_id": client_id,
            }

        # VALIDATE QUANTITY
            cont = 0
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
            cont += 1

            # Save without using lists


            order_detai = (
                product_data[0],
                product_data[1],
                quantity
            )

            orders["product_"+str(cont)] = order_detai


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
        
        # for ix, ord in enumerate(orders):
        #     print (f"")
        
        order_auto_id += 1

        print(f"\nOrder {order_auto_id} created successfully.")
        
        return order_auto_id

order_auto_ids = create_order(clients, products, orders, order_auto_id)



print (orders)
