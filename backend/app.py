from flask import Flask, jsonify
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
