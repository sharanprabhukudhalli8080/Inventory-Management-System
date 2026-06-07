# models.py
from db import get_connection

# --------------------------------------------------
# 📦 PRODUCT OPERATIONS
# --------------------------------------------------

# Insert new product into database
def insert_product(product):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO products VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(query, product)

    conn.commit()
    conn.close()


# Fetch all products from database
def get_all_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()

    conn.close()
    return data


# Update product quantity
def update_quantity(pid, qty):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE products SET quantity=%s WHERE product_id=%s",
        (qty, pid)
    )

    conn.commit()
    conn.close()


# Get products with low stock (quantity < threshold)
def get_low_stock():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products WHERE quantity < threshold")
    data = cursor.fetchall()

    conn.close()
    return data


# Delete product from inventory
def delete_product(pid):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products WHERE product_id=%s", (pid,))
    conn.commit()

    rows_deleted = cursor.rowcount

    conn.close()
    return rows_deleted


# Search product by name (partial match)
def search_product(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE name LIKE %s",
        ('%' + name + '%',)
    )
    data = cursor.fetchall()

    conn.close()
    return data


# --------------------------------------------------
# 🔐 USER AUTHENTICATION
# --------------------------------------------------

# Check if user exists (used for login & signup validation)
def user_exists(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()

    conn.close()
    return user


# Create new user (signup)
def create_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users VALUES (%s, %s)",
        (username, password)
    )
    conn.commit()

    conn.close()


# Verify login credentials (CASE-SENSITIVE)
def check_login(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username=%s",
        (username,)
    )
    result = cursor.fetchone()

    conn.close()

    if result:
        stored_password = result[0]
        return stored_password == password
    else:
        return False