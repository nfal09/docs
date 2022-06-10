import sqlite3

con = sqlite3.connect("products-database.db")
sql = con.cursor()

query = """
    SELECT * FROM products;
"""

print("All products:")
result = sql.execute(query)
rows = result.fetchall()

for row in rows:
    print(row)


query = """
    INSERT INTO products (product_name, product_price, product_category) 
    VALUES ("mousepad", NULL, "Accessories");
"""

# This will throw an error
sql.execute(query)
con.commit()