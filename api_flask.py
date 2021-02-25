from flask import Flask, render_template, jsonify, request
from flask_cors import CORS 
import mysql.connector
import logging

config = {
    'user': 'root',
    'password': 'toto',
    'host': 'db',
    'database': 'e_learning_db'
}

connection = mysql.connector.connect(**config)
app = Flask(__name__)


@app.route('/')
def index():
    return f'hello world : {connection}'
    return render_template("index.html")


@app.route('/home')
def hello():
    return render_template("index.html")
