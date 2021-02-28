from docker_scrap import *
from js_scrap import *
from PythonScrap import *

# print("hello")


logging.basicConfig(level=logging.DEBUG,
                    filename="main_learning.log",
                    format='%(asctime)s : %(levelname)s : %(message)s')



#print('hello main' )
def docker():
    docker_class = VideoDocker()
    docker_class.docker_title()
    docker_class.docker_link()
    docker_class.docker_youtuber()
    docker_class.docker_duration()
    docker_class.docker_vue()
    docker_class.docker_theme()
    # print(docker_class.docker_zip())
    #print('hello docker')
    return docker_class.docker_zip()

docker()

def js():
    my_js = JsScrap()
    return my_js.get_data()
    

def python():
    my_data = PythonScrap()
    return my_data.get_data()

python()
