from flask import Flask, render_template
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
