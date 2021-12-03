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



#sign up code merger

print("Hello welcome to One Bloodline:-")


# signup steps
# function main programming
# we are done
def signup():
    global result
    username = input("Enter Username: ")
    email = input("Enter email id: ")
    number = input("Enter Mobile Number: ")
    password = input("Enter New Password: ")
    password1 = input("Retype New Password: ")

    bloodgroup = input()
    pincode = input()
    address = input()
    city = input()
    state = input()
    adhaar = input()

    if password == password1:
        signup_data = [username, address, adhaar, number, email, bloodgroup, city, state, pincode]
        add_user = ("INSERT INTO blood "
                    "(name,address, adhaar_no,contact_no,email_id,bloodgroup,city,state,pincode) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);")
        data_user = (
        add_user[0], add_user[1], add_user[2], add_user[3], add_user[4], add_user[5], add_user[6], add_user[7],
        add_user[8])
        mycursor.execute(add_user, data_user)
    else:
        print("Try Again! password didn't match")
        signup()

# execution of functions
signup()
print("signup process is  working fine.(only for debugging purpose)")
mydb.commit()


#signin page(fully working and tested)
def signin():
    global result,passcheck
    username = str(input("Enter Username:"))
    password = str(input("Enter New Password:"))
    #data of user is stored here
    result = [username, password]
    ID = 1
    passcheck= ("SELECT password FROM auth "
                "WHERE username='"+username+"'")
    mycursor.execute(passcheck,username)
    passwd= str(mycursor.fetchone())
    password1= re.sub('[^A-Za-z0-9]+', '', passwd)
    # print(passwd)
    # print(password1)
    # print(passcheck)
    if password1 == password:
        print("success")
        token1=jwt_token.token(username,ID)
        # print(token1)

    else:
        print("Wrong password")
#execution of functions
signin()
mydb.commit()
# print(result)
print("signin process is  working fine.(only for debugging purpose)")


