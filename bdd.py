import mysql.connector
import logging
from main import *



logging.basicConfig(filename = "db_learning.log", 
                    level= logging.DEBUG, 
                    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')

#print("init docker", docker())

class Table():

    def __init__(self):

        logging.info('[SQL] Connection with sql docker for docker video table: start')

        try:
            self.mydb = mysql.connector.connect (
            host="e_learning_db_1",
            user="root",
            database = "e_learning_db",
            password="toto",
            )
        except(mysql.connector.errors.InterfaceError, mysql.connector.errors.ProgrammingError):
            logging.warning('[SQL] Failed to connect to docker container')

        try:
            self.c = self.mydb.cursor()
        except AttributeError:
            logging.warning('[SQL] Failed to establish query, check syntax, will affect creation of table')

        logging.info('[SQL] Connection with sql connector : end')

        self.my_docker = docker()


    def create_docker_table(self):
    
        logging.info("[SQL] Creation docker table  : start")

        self.c.execute("DROP TABLE docker")
        self.c.execute("CREATE TABLE IF NOT EXISTS docker (id INTEGER AUTO_INCREMENT PRIMARY KEY , link VARCHAR(350) NOT NULL, title VARCHAR(350) NOT NULL, youtuber VARCHAR(350) NOT NULL, duration VARCHAR(30) NOT NULL, likes VARCHAR(350), theme VARCHAR(350))")

        logging.info("[SQL] Creation docker carpet : end")

    def file_docker_table(self):

        logging.info("[SQL] Insert data in docker table  : start")

        try:
            insert = "INSERT INTO docker (link, title, youtuber, duration, likes, theme) VALUES(%s, %s, %s, %s, %s, %s);"
            value = self.my_docker
            print('value of docker table', value)
            self.c.executemany(insert, value)

            self.mydb.commit()
        except Exception as e:
            logging.error('[SQL] ERROOOOR !! empty list, didnt fill docker table' +str(e))

        logging.info("[SQL] Insert data in docker table  : end")



my_table = Table()
my_table.create_docker_table()
my_table.file_docker_table()