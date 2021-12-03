import mysql.connector

def test():
    # code for connecting sql databse with python for fetching and analysing it
    # auth details
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
    # you can copy this sent and add your own query.
    mycursor.execute("select * from blood")
    # fetch funtion has been used there are many more option. refer documentation.
    result = mycursor.fetchall()
    # loop for printing out data . result can be changed to any varaible
    for i in result:
        print(i)

def signup():
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
    # you can copy this sent and add your own query.
    mycursor.execute("select * from blood")
    # fetch funtion has been used there are many more option. refer documentation.
    result = mycursor.fetchall()

    # loop for printing out data . result can be changed to any varaible
    for i in result:
        print(i)


