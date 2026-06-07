from operations import *



while True:
    print("\n1. Login")
    print("2. Signup")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        if login():
            break
    elif choice == "2":
        if signup():  
            break
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")

while True:
    print("\n===== Inventory System =====")
    print("1. Add Product")
    print("2. Update Stock")
    print("3. View Inventory")
    print("4. Low Stock Alert")
    print("5. Delete Product")
    print("6. Search Product")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        update_stock()
    elif choice == "3":
        view_inventory()
    elif choice == "4":
        low_stock_alert()
    elif choice == "5":
        delete_stock()
    elif choice == "6":
        search_product_op()
    elif choice == "8":
        print("Exiting...")
        break
    else:
        print("Invalid choice")