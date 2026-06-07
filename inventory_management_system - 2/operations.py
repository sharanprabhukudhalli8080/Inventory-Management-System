# operations.py
from models import *

# Take input and add product
def add_product():
    try:
        pid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        qty = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        threshold = int(input("Enter Threshold: "))

        insert_product((pid, name, qty, price, threshold))
        print("✅ Product added!")

    except Exception as e:
        print("❌ Error:", e)


# Update stock based on product ID
def update_stock():
    try:
        pid = int(input("Enter Product ID: "))
        qty = int(input("Enter New Quantity: "))

        update_quantity(pid, qty)
        print("✅ Stock updated!")

    except Exception as e:
        print("❌ Error:", e)


# View inventory
def view_inventory():
    try:
        items = get_all_products()

        if items:
            print("\n📦 Inventory:")
            for item in items:
                print(item)
        else:
            print("⚠️ Inventory is empty.")

    except Exception as e:
        print("❌ Error:", e)


# Show low stock products
def low_stock_alert():
    try:
        items = get_low_stock()

        if items:
            print("\n⚠️ Low Stock Products:")
            for item in items:
                print(item)
        else:
            print("✅ No low stock products.")

    except Exception as e:
        print("❌ Error:", e)


# Delete product only if exists
def delete_stock():
    try:
        pid = int(input("Enter Product ID to delete: "))

        result = delete_product(pid)

        if result > 0:
            print("✅ Product deleted!")
        else:
            print("❌ No product found with this ID.")

    except Exception as e:
        print("❌ Error:", e)


# Search product
def search_product_op():
    try:
        name = input("Enter product name to search: ")
        results = search_product(name)

        if results:
            print("\n🔍 Search Results:")
            for r in results:
                print(r)
        else:
            print("❌ No product found")

    except Exception as e:
        print("❌ Error:", e)


# Signup functionality
def signup():
    try:
        username = input("Create username: ")
        password = input("Create password: ")

        if user_exists(username):
            print("⚠️ Account already exists, please login.")
            return False
        else:
            create_user(username, password)
            print("✅ Account created successfully! Logging in...")
            return True

    except Exception as e:
        print("❌ Error:", e)
        return False


# Login functionality
def login():
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if not user_exists(username):
            print("❌ No account found, please signup.")
            return False

        user = check_login(username, password)

        if user:
            print("✅ Login successful!")
            return True
        else:
            print("❌ Incorrect password")
            return False

    except Exception as e:
        print("❌ Error:", e)
        return False5