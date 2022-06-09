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
    SELECT AVG(product_price) AS average_product_price FROM products;
"""

print("\nAverage cost of all products:")
execute_query_and_display_rows(query)

query = """
    SELECT COUNT(*) as total_products FROM products;
"""

print("\nTotal number of products:")
execute_query_and_display_rows(query)

query = """
    SELECT product_name || " $" || MAX(product_price) AS most_expensive_product 
    FROM products;
"""

print("\nMost expensive product:")
execute_query_and_display_rows(query)

query = """
    SELECT product_name || " $" || MIN(product_price) AS least_expensive_product 
    FROM products;
"""

print("\nLeast expensive product:")
execute_query_and_display_rows(query)

query = """
    SELECT SUM(product_price) AS total_cost_all_products FROM products;
"""

print("\nTotal cost of all products:")
execute_query_and_display_rows(query)
