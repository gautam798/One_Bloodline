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

