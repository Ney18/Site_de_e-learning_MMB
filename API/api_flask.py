from flask import Flask
import mysql.connector

config = {
    'user': 'root',
    'password': 'toto',
    'host': 'sql_learning',
    'port': '3307',
    'database': 'e_learning_db'
}

connection = mysql.connector.connect(**config)
app = Flask(__name__)


@app.route('/')
def index():
    return f'hello world : {connection}'


@app.route('/toto')
def hello():
    return 'bonjourno'
