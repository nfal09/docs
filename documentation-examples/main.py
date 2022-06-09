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
    SELECT product_category FROM products GROUP BY product_category;
"""

print("\nUnique `product_categories`:")
execute_query_and_display_rows(query)

query = """
    SELECT product_category, COUNT(*) AS num_products_per_category 
    FROM products 
    GROUP BY product_category;
"""

print("\nNumber of products per category:")
execute_query_and_display_rows(query)