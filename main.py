from flask import Flask, request, render_template, jsonify, redirect
from flask_cors import CORS
from bdd import *
import requests
from setup_logger import logging
from docker_scrap import *
from js_scrap import *
#from file_db import *

# print("hello")
app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG,
                    filename="main_learning.log",
                    format='%(asctime)s : %(levelname)s : %(message)s')

message = ''


@app.route('/')
def index():
    return message


@app.route('/create_table/<tablename>')
def create_table(tablename):
    global message
    db_learn = BDD()
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
        db_learn.insert_data(tablename, JsScrap().data)
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
def page_datat(theme):
    return render_template('page_data_js.html', theme=theme)


def docker():
    docker_class = VideoDocker()
    docker_class.docker_title()
    docker_class.docker_link()
    docker_class.docker_youtuber()
    docker_class.docker_duration()
    docker_class.docker_vue()
    docker_class.docker_theme()
    # print(docker_class.docker_zip())

    return docker_class.docker_zip()


docker()
