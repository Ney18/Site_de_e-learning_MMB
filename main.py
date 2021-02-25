from docker_scrap import *
from js_scrap import *
#from file_db import *

#print("hello")

logging.basicConfig(level=logging.DEBUG,
                    filename="main_learning.log",
                    format='%(asctime)s : %(levelname)s : %(message)s')



def docker():
    docker_class = VideoDocker()
    docker_class.docker_title()
    docker_class.docker_link()
    docker_class.docker_youtuber()
    docker_class.docker_duration()
    docker_class.docker_vue()
    docker_class.docker_theme()
    #print(docker_class.docker_zip())

    return docker_class.docker_zip()

docker()