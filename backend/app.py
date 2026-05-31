from datetime import datetime
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
    
@app.route('/api/transactions', methods=['POST'])
def add_transaction():

    data = request.json

    product_id = data['product_id']
    qty = int(data['qty'])

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM products WHERE id = %s",
        (product_id,)
    )

    product = cursor.fetchone()

    if not product:

        conn.close()

        return jsonify({
            "message": "Produk tidak ditemukan"
        }), 404

    if qty > product['stok']:

        conn.close()

        return jsonify({
            "message": "Stok tidak mencukupi"
        }), 400

    subtotal = float(product['harga']) * qty

    cursor.execute(
        """
        INSERT INTO transactions
        (tanggal, total)
        VALUES (%s, %s)
        """,
        (
            datetime.now(),
            subtotal
        )
    )

    transaction_id = cursor.lastrowid

    cursor.execute(
        """
        INSERT INTO transaction_items
        (
            transaction_id,
            product_id,
            qty,
            subtotal
        )
        VALUES (%s, %s, %s, %s)
        """,
        (
            transaction_id,
            product_id,
            qty,
            subtotal
        )
    )

    cursor.execute(
        """
        UPDATE products
        SET stok = stok - %s
        WHERE id = %s
        """,
        (
            qty,
            product_id
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Transaksi berhasil"
    })
    
@app.route('/api/dashboard', methods=['GET'])
def dashboard():

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT COUNT(*) AS total_produk FROM products"
    )

    total_produk = cursor.fetchone()['total_produk']

    cursor.execute(
        "SELECT COUNT(*) AS total_transaksi FROM transactions"
    )

    total_transaksi = cursor.fetchone()['total_transaksi']

    cursor.execute(
        """
        SELECT
            IFNULL(SUM(total),0)
            AS total_penjualan
        FROM transactions
        """
    )

    total_penjualan = cursor.fetchone()['total_penjualan']

    conn.close()

    return jsonify({
        "total_produk": total_produk,
        "total_transaksi": total_transaksi,
        "total_penjualan": total_penjualan
    })
    
@app.route('/api/transactions', methods=['GET'])
def get_transactions():

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            t.id,
            p.nama_produk,
            ti.qty,
            ti.subtotal
        FROM transactions t
        JOIN transaction_items ti
            ON t.id = ti.transaction_id
        JOIN products p
            ON p.id = ti.product_id
        ORDER BY t.id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return jsonify(data)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)