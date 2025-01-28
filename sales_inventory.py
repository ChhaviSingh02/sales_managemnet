import mysql.connector
from tabulate import tabulate

# Database connection
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="2549",  # Replace with your MySQL password
        database="project_sales"
    )

# Add a new product
def add_product():
    conn = connect_to_db()
    cursor = conn.cursor()
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    cursor.execute("INSERT INTO products (product_name, quantity, price) VALUES (%s, %s, %s)",
                   (product_name, quantity, price))
    conn.commit()
    print("Product added successfully!")
    conn.close()

# View inventory
def view_inventory():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    print(tabulate(rows, headers=["Product ID", "Product Name", "Quantity", "Price"], tablefmt="pretty"))
    conn.close()

# Update product quantity
def update_product():
    conn = connect_to_db()
    cursor = conn.cursor()
    product_id = int(input("Enter product ID to update: "))
    quantity = int(input("Enter new quantity: "))
    cursor.execute("UPDATE products SET quantity = %s WHERE product_id = %s", (quantity, product_id))
    conn.commit()
    print("Product updated successfully!")
    conn.close()

# Record a sale
def record_sale():
    conn = connect_to_db()
    cursor = conn.cursor()
    product_id = int(input("Enter product ID sold: "))
    quantity_sold = int(input("Enter quantity sold: "))
    cursor.execute("INSERT INTO sales (product_id, quantity_sold) VALUES (%s, %s)", (product_id, quantity_sold))
    cursor.execute("UPDATE products SET quantity = quantity - %s WHERE product_id = %s",
                   (quantity_sold, product_id))
    conn.commit()
    print("Sale recorded successfully!")
    conn.close()

# View sales report
def view_sales():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT sales.sale_id, products.product_name, sales.quantity_sold, sales.sale_date "
        "FROM sales JOIN products ON sales.product_id = products.product_id"
    )
    rows = cursor.fetchall()
    print(tabulate(rows, headers=["Sale ID", "Product Name", "Quantity Sold", "Sale Date"], tablefmt="pretty"))
    conn.close()

# Main menu
def main():
    while True:
        print("\n--- Sales and Inventory Management System ---")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Update Product")
        print("4. Record Sale")
        print("5. View Sales Report")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            update_product()
        elif choice == '4':
            record_sale()
        elif choice == '5':
            view_sales()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

