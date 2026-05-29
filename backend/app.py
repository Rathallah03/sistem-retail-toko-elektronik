from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db_config = {
    'host': '192.168.56.11',
    'user': 'retail_user',
    'password': 'password123',
    'database': 'retail_db'
}

@app.route('/api/products', methods=['GET'])
def get_products():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    conn.close()

    return jsonify(products)
    
@app.route('/api/products', methods=['POST'])
def add_product():

    data = request.json

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = """
    INSERT INTO products
    (nama_produk, kategori, harga, stok)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            data['nama_produk'],
            data['kategori'],
            data['harga'],
            data['stok']
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Produk berhasil ditambahkan"
    })
    
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM products WHERE id = %s",
        (product_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Produk berhasil dihapus"
    })
    
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):

    data = request.json

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = """
    UPDATE products
    SET
        nama_produk = %s,
        kategori = %s,
        harga = %s,
        stok = %s
    WHERE id = %s
    """

    cursor.execute(
        query,
        (
            data['nama_produk'],
            data['kategori'],
            data['harga'],
            data['stok'],
            product_id
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Produk berhasil diperbarui"
    })
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)