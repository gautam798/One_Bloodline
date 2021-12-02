import mysql.connector


#code for connecting sql databse with python for fetching and analysing it
#auth details
mydb= mysql.connector.connect(host="3.110.22.36", user='manager', passwd='Atharva@54321', database='sys')

#just added variable to make code readable.
mycursor = mydb.cursor()
#you can copy this sent and add your own query.
mycursor.execute("select * from blood")
#fetch funtion has been used there are many more option. refer documentation.
result = mycursor.fetchall()

#loop for printing out data . result can be changed to any varaible
for i in result:
    print(i)
