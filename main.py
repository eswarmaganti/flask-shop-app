from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
from MySQLdb.cursors import DictCursor
import os

# load the environment variables
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_DATABASE_DB = os.getenv('MYSQL_DATABASE_DB')


app = Flask(__name__)

app.config['MYSQL_USER'] = MYSQL_USER
app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD
app.config['MYSQL_DATABASE_DB'] = MYSQL_DATABASE_DB
app.config['MYSQL_HOST'] = MYSQL_HOST

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor(DictCursor)
    cursor.execute(''' SELECT * FROM shop.products ''')
    products =  cursor.fetchall()
    cursor.close()
    return render_template('index.html', products=products)

@app.route('/add_product', methods=["POST"])
def add_product():
    product_name = request.form.get('name')
    product_desc = request.form.get('description')
    product_price = request.form.get('price')

    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO shop.products (name, description, price) VALUES (%s,%s,%s)''', (product_name, product_desc, product_price))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for("index"))