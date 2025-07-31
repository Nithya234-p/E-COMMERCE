from flask import Flask, jsonify
from flask_cors import CORS
import pyodbc

app = Flask(_name_)
CORS(app)

# SQL Server config
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=ecommerce;UID=sa;PWD=YourPasswordHere;TrustServerCertificate=yes'
)

@app.route('/api/products', methods=['GET'])
def get_products():
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price FROM products")  # modify as per your table
    rows = cursor.fetchall()

    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "price": row[2]
        })
    return jsonify(products), 200

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price FROM products WHERE id = ?", (product_id,))
    row = cursor.fetchone()

    if row:
        product = {"id": row[0], "name": row[1], "price": row[2]}
        return jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404

if _name_ == '_main_':
    app.run(debug=Tru
