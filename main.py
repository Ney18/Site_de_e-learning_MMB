from flask import Flask, request, render_template, jsonify, redirect
from flask_cors import CORS
from bdd import *
import requests
from setup_logger import logging
from docker_scrap import *
from js_scrap import *
from PythonScrap import *

# print("hello")
app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG,
                    filename="main_learning.log",
                    format='%(asctime)s : %(levelname)s : %(message)s')

message = ''


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

def js():
    my_js = JsScrap()
    

    return my_js.get_data()

def python():
    my_data = PythonScrap()
    return my_data.get_data()

python()
