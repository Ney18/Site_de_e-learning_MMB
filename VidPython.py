import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

PythonVid = ['https://www.youtube.com/watch?v=psaDHhZ0cPs','https://www.youtube.com/watch?v=rfscVS0vtbw','https://www.youtube.com/watch?v=DPaUCvNcHiM']

sql = "INSERT INTO 'dbxxx' (PythonVid) VALUES (%s)"
val = [
  ('https://www.youtube.com/watch?v=psaDHhZ0cPs'),
  ('https://www.youtube.com/watch?v=rfscVS0vtbw'),
  ('https://www.youtube.com/watch?v=DPaUCvNcHiM')]

