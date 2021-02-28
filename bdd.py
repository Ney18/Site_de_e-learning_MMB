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
            database = "e_learning_db",
            user='root',
            )
        except Exception as e:
            logging.warning('[SQL] Failed to connect to docker container' + str(e))

        try:
            self.c = self.mydb.cursor()
        except AttributeError:
            logging.warning('[SQL] Failed to establish query, check syntax, will affect creation of table')

        logging.info('[SQL] Connection with sql connector : end')

        self.my_docker = docker()
        self.my_javaScript = js()
        self.my_python = python()



    def create_table(self):
    
        logging.info("[SQL] Creation data_videos table  : start")
        self.c.execute("DROP TABLE data_videos")
        self.c.execute("CREATE TABLE IF NOT EXISTS data_videos (id INTEGER AUTO_INCREMENT PRIMARY KEY , link VARCHAR(350) NOT NULL, title VARCHAR(350) NOT NULL, youtuber VARCHAR(350) NOT NULL, duration VARCHAR(30) NOT NULL, likes VARCHAR(350), theme VARCHAR(350))")

        logging.info("[SQL] Creation data_videos table : end")


    def file_table(self):

        logging.info("[SQL] Insert data in data_videos table  : start")

        try:
            insert = "INSERT INTO data_videos (link, title, youtuber, duration, likes, theme) VALUES(%s, %s, %s, %s, %s, %s);"
            value = self.my_docker
            self.c.executemany(insert, value)

            self.mydb.commit()
        except Exception as e:
            logging.error('[SQL] ERROOOOR !! empty list, didnt fill docker columns' +str(e))




        try:
            insert = "INSERT INTO data_videos (link, title, youtuber, duration, likes, theme) VALUES(%s, %s, %s, %s, %s, %s);"
            value = self.my_javaScript
            self.c.executemany(insert, value)

            self.mydb.commit()
        except Exception as e:
            logging.error('[SQL] ERROOOOR !! empty list, didnt fill javaScript column' +str(e))




        try:
            insert = "INSERT INTO data_videos (link, title, youtuber, duration, likes, theme) VALUES(%s, %s, %s, %s, %s, %s);"
            value = self.my_python

            self.c.executemany(insert, value)

            self.mydb.commit()
        except Exception as e:
            logging.error('[SQL] ERROOOOR !! empty list, didnt fill python colone' +str(e))

        
        logging.info("[SQL] Insert data in data_videos table  : end")

    


my_table = Table()
my_table.create_table()
my_table.file_table()