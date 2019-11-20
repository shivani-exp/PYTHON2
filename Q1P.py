from __future__ import generators
import mysql.connector

def ResultIter(cursor, arraysize = 1000 ):
    while True:
        results = cursor.fetchmany(arraysize)
        if not results:
            break
        for result in results:
            yield result

mydb = mysql.connector.connect (
  host = "localhost",
  user = "root" ,
  port = "3306" ,
  database  = "student"
)
cursor = mydb.cursor()
cursor.execute('select * from mydb')

for result in ResultIter(cursor):
    print(result)

