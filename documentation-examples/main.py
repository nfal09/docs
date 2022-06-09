import sqlite3

con = sqlite3.connect("products-database.db")
sql = con.cursor()

def execute_query_and_display_rows(query):
    result = sql.execute(query)
    rows = result.fetchall()

    for row in rows:
        print(row)


query = """
    SELECT * FROM products;
"""

print("All products:")
execute_query_and_display_rows(query)

query = """
    SELECT product_name || " : $" || product_price AS product_description 
    FROM products;
"""

print("\nFormatted product descriptions:")
execute_query_and_display_rows(query)

query = """
    SELECT SUM(product_price) AS total_price_computers 
    FROM products 
    WHERE product_category = "Computers";
"""

print("\nThe total price of all computers in the `products` table:")
execute_query_and_display_rows(query)