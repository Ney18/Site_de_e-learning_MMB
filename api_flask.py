from flask import Flask, render_template, jsonify, request
from flask_cors import CORS 
import mysql.connector
import logging



conn = mysql.connector.connect(
    user= 'root',
    password= 'toto',
    host= 'db',
    database= 'e_learning_db'
)


sql_query = conn.cursor(dictionary=True)
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
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

@app.route('/time_video', methods=['GET'])
def duration_video():
    time_video = request.args.get('time')

    sql_query.execute(f'SELECT CONVERT(duration, TIME), title, youtuber FROM data_videos WHERE duration <= "%{time_video}%"')
    output = sql_query.fetchall()
    return jsonify(output)

#app.route('/')
    
docker()


@app.route('/')
def index():
    return message


@app.route('/create_table/<tablename>')
def create_table(tablename):
    global message
    db_learn = Table()
    try:
        db_learn.execute_query(db_learn.create_table, tablename)
        message = 'SUCCESS'
    except:
        message = 'impossible to create table'
        app.logger.error('impossible to create table')
    db_learn.__disconnect__()
    return redirect('/')


@app.route('/insert_data/<tablename>')
def insert_data(tablename):
    global message
    db_learn = Table()
    try:
        if tablename == 'js':
            db_learn.insert_data(tablename, JsScrap().data)
        elif tablename == 'python':
            db_learn.insert_data(tablename, PythonScrap().data)
        message = 'SUCCESS'
    except:
        print('impossible to insert data')
        message = 'ERROR'
    db_learn.__disconnect__()
    return redirect('/')


@app.route('/api/query_data/<query>')
def get_elearn_list(query):
    global message
    try:
        db_learn = Table()
        data_learn = db_learn.select_from_db(query)
        db_learn.__disconnect__()
        return jsonify(data_learn)
    except:
        message = 'ERROR'
        return redirect('/')


@app.route('/page_data/<theme>')
def page_data(theme):
    return render_template('index.html')