
import mysql_connector

x = input("\nAre you a Blood Donor or a Blood Reciever?\nType 'd' for Blood Donor or 'r' for Blood Reciever\nOption- ")
if x == 'd':
  y = input("You have opted for Blood Donor.\nPlease enter your blood group according to the options: \na. A+\nb. A-\nc. B+\nd. B-\ne. AB+\nf. AB-\ng. O+\nh. O-\nOption- ")
  if y == 'a':
   print("You can donate blood to: A+, AB+")
  elif y == 'b':
    print("You can donate blood to: A+, A-, AB+, AB-")
  elif y == 'c':
    print("You can donate blood to: B+, AB+")
  elif y == 'd':
    print("You can donate blood to: B+, B-, AB+, AB-")
  elif y == 'e':
    print("You can donate blood to: AB+")
  elif y == 'f':
    print("You can donate blood to: AB+, AB-")
  elif y == 'g':
    print("You can donate blood to: A+, B+, AB+, O+, ")
  elif y == 'h':
    print("You can donate blood to: All Blood Types")
  else:
      print("Invalid Input")

if x == 'r':
  z = input("You have opted for Blood Reciever.\nPlease enter your blood group according to the options: \na. A+\nb. A-\nc. B+\nd. B-\ne. AB+\nf. AB-\ng. O+\nh. O-\nOption- ")
  if z == 'a':
   print("You can recieve blood from: A+, A-, O+, O-")
  elif z == 'b':
    print("You can recieve blood from: A+, O-")
  elif z == 'c':
    print("You can recieve blood from: B+, B-, O+, O-")
  elif z == 'd':
    print("You can recieve blood from: B-, O-")
  elif z == 'e':
    print("You can recieve blood from: All Blood Types")
  elif z == 'f':
    print("You can recieve blood from: A-, B-, AB-, O-")
  elif z == 'g':
    print("You can recieve blood from: O+, O-")
  elif z == 'h':
    print("You can recieve blood from: O- Only")
  else:
      print("Invalid Input")

mysql_connector.test()