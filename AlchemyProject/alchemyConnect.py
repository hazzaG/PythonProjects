import mysql.connector as sql
from alchemySQLpass import *

try:
    dbCon = sql.connect(host ="localhost", user="Alchemy", database ="alchemy", password=dbPass)
    dbCursor = dbCon.cursor(prepared=True)
          
    print("Connection successful")
   
except sql.errors.Error as e:
    print(f"DB failed because: {e}") 
