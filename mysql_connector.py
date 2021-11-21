import mysql.connector


#code for connecting sql databse with python for fetching and analysing it
mydb = mysql.connector.connect(host="localhost",user='gautam',passwd='gautam123',database='accounts') #auth details
mycursor= mydb.cursor()    #just added variable to make code readable.
mycursor.execute("select * from income") #you can copy this sent and add your own query.
result =mycursor.fetchall()  #fetch funtion has been used there are many more option. refer documentation.

#loop for printing out data . result can be changed to any varaible
for i in result:
    print(i)
