#this is testing page don't push or pull this

#main program
#imported necesaary modules
from __future__ import print_function
import mysql.connector
import jwt_token
import re
from mysql.connector import (connection)

#mysql config
config = {
        'user': 'manager',
        'password': 'Atharva@54321',
        'host': '3.110.22.36',
        'database': 'sys',
        'raise_on_warnings': True
    }
mydb = mysql.connector.connect(**config)
# just added variable to make code readable.
mycursor = mydb.cursor()

def urgent():
  z = input("You have opted for Blood Reciever.\nPlease enter your blood group according to the options: \na. A+\nb. A-\nc. B+\nd. B-\ne. AB+\nf. AB-\ng. O+\nh. O-\nOption- ")
  if z == 'a':
          print("You can recieve blood from: A+, A-, O+, O-")
          global blood
          blood = ["A+ve", "A-ve", "O+ve", "O-ve"]

  elif z == 'b':
          print("You can recieve blood from: A+, O-")
          blood = ["A+ve", "O-ve","null","null"]


  elif z == 'c':
          print("You can recieve blood from: B+, B-, O+, O-")
          blood = ["B+ve", "B-ve", "O+ve", "O-ve"]


  elif z == 'd':
          print("You can recieve blood from: B-, O-")
          blood = ["B-ve", "O-ve","null","null"]


  elif z == 'e':
          print("You can recieve blood from: All Blood Types")
          blood = ["A+ve", "A-ve", "B+ve", "B-ve", "AB+ve", "AB-ve", "O+ve", "O-ve"]


  elif z == 'f':
          print("You can recieve blood from: A-, B-, AB-, O-")
          blood = ["A-ve", "B-ve", "AB-ve", "O-ve"]


  elif z == 'g':
          print("You can recieve blood from: O+, O-")
          blood = ["O+ve", "O-ve","null","null"]


  elif z == 'h':
          print("You can recieve blood from: O- Only")
          blood = ["O-ve","null","null","null"]

  else:
          print("Invalid Input")


urgent()
# print(blood[0])
length = len(blood)
print(length)
urgent_query=("SELECT name,id from blood "
              "WHERE bloodgroup= %s OR bloodgroup= %s OR bloodgroup= %s OR bloodgroup= %s")
data_query=[blood[0],blood[1],blood[2],blood[3]]
print(data_query)
mycursor.execute(urgent_query, data_query)

final_Data= mycursor.fetchall()
# final_Data= mycursor.fetchmany(2)
print(final_Data)

# for i in final_Data:
#     print(i)