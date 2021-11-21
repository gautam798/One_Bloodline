import mysql.connector


#code for connecting sql databse with python for fetching and analysing it
<<<<<<< HEAD
mydb = mysql.connector.connect(host="localhost",user='gautam',passwd='gautam123',database='accounts') #auth details
=======
mydb = mysql.connector.connect(host="localhost",user='',passwd='',database='test') #auth details databse (blood_db,auth_db)
>>>>>>> 17c29ea6e46c8cb4f4eaf4f081d6d9068edc8e76
mycursor= mydb.cursor()    #just added variable to make code readable.
mycursor.execute("select * from income") #you can copy this sent and add your own query.
result =mycursor.fetchall()  #fetch funtion has been used there are many more option. refer documentation.

#loop for printing out data . result can be changed to any varaible
for i in result:
    print(i)
