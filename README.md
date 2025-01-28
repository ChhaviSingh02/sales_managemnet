
# **Sales and Inventory Management System**

A Python-based application to manage inventory and sales records efficiently. The system uses a MySQL database for data storage and retrieval, enabling users to add, update, view, and manage products and sales records.

---

## **Features**

1. **Add Product**: Add new products to the inventory with name, quantity, and price.
2. **View Inventory**: View all products currently in the inventory.
3. **Update Product**: Update the quantity of an existing product.
4. **Record Sale**: Record sales transactions and adjust inventory automatically.
5. **View Sales Report**: View detailed reports of all sales, including product names, quantities sold, and sale dates.

---

## **Technologies Used**

- **Programming Language**: Python
- **Database**: MySQL
- **Libraries**: 
  - `mysql-connector-python` for database interaction
  - `tabulate` for displaying data in table format

---

## **Setup Instructions**

### **Prerequisites**
1. Python 3.8+ installed on your system.
2. MySQL database server installed and running.
3. Install required Python libraries:
   ```bash
   pip install mysql-connector-python tabulate
   ```

### **Database Configuration**
1. Create a MySQL database named `sales_management`:
   ```sql
   CREATE DATABASE sales_management;
   ```
2. Create the necessary tables:
   ```sql
   CREATE TABLE products (
       product_id INT AUTO_INCREMENT PRIMARY KEY,
       product_name VARCHAR(100) NOT NULL,
       quantity INT NOT NULL,
       price DECIMAL(10, 2) NOT NULL
   );

   CREATE TABLE sales (
       sale_id INT AUTO_INCREMENT PRIMARY KEY,
       product_id INT NOT NULL,
       quantity_sold INT NOT NULL,
       sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       FOREIGN KEY (product_id) REFERENCES products(product_id)
   );
   ```

3. Update the database connection details in the script (`sales_inventory.py`):
   ```python
   return mysql.connector.connect(
       host="localhost",
       port=3300,
       user="root",          # Replace with your MySQL username
       password="1234",      # Replace with your MySQL password
       database="sales_management"
   )
   ```

---

## **Usage**

1. Run the Python script:
   ```bash
   python sales_inventory.py
   ```

2. Follow the menu options to manage inventory and sales:
   - **Add Product**: Enter product details.
   - **View Inventory**: View all available products.
   - **Update Product**: Update the quantity of a specific product.
   - **Record Sale**: Enter sales information.
   - **View Sales Report**: View detailed sales transactions.

---

## **Screenshots**

### Menu Interface:
```
--- Sales and Inventory Management System ---
1. Add Product
2. View Inventory
3. Update Product
4. Record Sale
5. View Sales Report
6. Exit
```

### Inventory Example:
```
+------------+----------------+----------+--------+
| Product ID | Product Name   | Quantity | Price  |
+------------+----------------+----------+--------+
|     1      | Laptop         |    10    | 55000  |
|     2      | Smartphone     |    25    | 15000  |
+------------+----------------+----------+--------+
```

---

## **Error Handling**

- **Database Connection**: Handles errors if the database is unavailable or credentials are incorrect.
- **Validation**: Prevents invalid entries, such as negative quantities or invalid product IDs.

---

## **Future Enhancements**

- Add a search feature to find products by name or ID.
- Export reports to CSV files for offline use.
- Introduce user roles for restricted access to certain features.
- Create a GUI using `tkinter` or `PyQt`.

---

## **License**

This project is open-source and available under the [MIT License](LICENSE).

---

## **Author**

Developed by **Chhavi Singh** (GitHub: [ChhaviSingh02](https://github.com/ChhaviSingh02)).
