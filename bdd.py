import mysql.connector
import logging
from main import *
import time


logging.basicConfig(filename="db_learning.log",
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')

#print("init docker", docker())


class Table():

    def __init__(self):
        time.sleep(1)
        self.query_specify = None

        logging.info(
            '[SQL] Connection with sql docker for docker video table: start')

        try:
            self.mydb = mysql.connector.connect(
                host="e_learning_db_1",
                user="root",
                database="e_learning_db",
                password="toto",
            )
        except(mysql.connector.errors.InterfaceError, mysql.connector.errors.ProgrammingError):
            logging.warning('[SQL] Failed to connect to docker container')

        try:
            self.c = self.mydb.cursor()
        except AttributeError:
            logging.warning(
                '[SQL] Failed to establish query, check syntax, will affect creation of table')

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
            logging.error(
                '[SQL] ERROOOOR !! empty list, didnt fill docker table' + str(e))

        logging.info("[SQL] Insert data in docker table  : end")

    def create_table(self, query):
        self.query_specify = f'CREATE TABLE IF NOT EXISTS content_yt_{query} (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, lien VARCHAR (2000), titre VARCHAR (100), videaste VARCHAR(100), duree VARCHAR (100), vue INT, theme VARCHAR(100));'

    def insert_data(self, query, query_plus):
        self.query_specify = f'INSERT INTO content_yt_{query} (lien, titre, videaste, duree, vue, theme) VALUES ( %s, %s, %s, %s, %s, %s)'
        try:
            self.mycursor = self.myconn.cursor()
            self.mycursor.executemany(self.query_specify, query_plus)
        except mysql.connector.Error as err:
            logging.error(err)
            exit()

    def select_from_db(self, tablename):
        self.mycursor = self.myconn.cursor(dictionary=True)
        self.query_specify = f'SELECT * FROM content_yt_{tablename};'
        self.mycursor.execute(self.query_specify)
        result = self.mycursor.fetchall()
        return result

    def __disconnect__(self):
        self.myconn.commit()
        self.myconn.close()

    def execute_query(self, callback_func, query):
        try:
            self.mycursor = self.myconn.cursor()
            callback_func(query)
            self.mycursor.execute(self.query_specify)
        except mysql.connector.Error as err:
            logging.error(err)
            exit()


my_table = Table()
my_table.create_docker_table()
my_table.file_docker_table()
