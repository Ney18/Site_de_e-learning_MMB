from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from bdd import *
import mysql.connector
import pafy
import logging



conn = mysql.connector.connect(
    user= 'toto',
    password= 'pwd',
    host= 'db',
    database= 'e_learning_db'
)
c = conn.cursor()

sql_query = conn.cursor(dictionary=True)
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":

        link= request.form.get("video_data_link")
        my_theme= request.form.get("category")
        
      
        # url = pafy.new(link)
        # result = (url.title)
         

        c.execute("INSERT INTO data_videos (link, title, theme) VALUES(%s, %s);" (link, my_theme))
        conn.commit()

    return render_template("index.html")

@app.route('/database')
def my_db():
    sql_query.execute("SELECT * FROM data_videos")
    output = sql_query.fetchall()
    return jsonify(output)

@app.route('/video_theme', methods=['GET'])
def theme_video():
    video_theme = request.args.get('theme')

    sql_query.execute(f'SELECT * FROM data_videos WHERE theme LIKE "%{video_theme}%" ')
    output = sql_query.fetchall()
    return jsonify(output)


# @app.route('/1')
# def a():
#     var = "javaScript"
#     return render_template("test.html", var=var)

# @app.route('/2')
# def b():
#     var = "python"
#     return render_template("test.html", var=var)
