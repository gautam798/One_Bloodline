
print("Hello welcome to One Bloodline:-")
#signup steps
#function main programming
#we are done
def signup():
    global result
    username = input("Enter Username: ")
    email = input("Enter email id: ")
    number = input("Enter Mobile Number: ")
    password = input("Enter New Password: ")
    password1 = input("Retype New Password: ")

    bloodgroup =input()
    pincode=input()
    address=input()
    city=input()
    state=input()
    adhaar=input()

    if password==password1:
        signup_data = [username,address,adhaar,number,email,bloodgroup,city,state,pincode]
        add_user = ("INSERT INTO blood "
                      "(name,address,adhaar_no,contact_no,email_id,bloodgroup,city,state,pincode) "
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);")
        data_user = (add_user[0],add_user[1],add_user[2],add_user[3],add_user[4],add_user[5],add_user[6],add_user[7],add_user[8])
        cursor.execute(add_user, data_user)
    else :
        print("Try Again! password didnt match")
        signup()
#execution of functions
signup()
print(result)
print("signup process is  working fine.(only for debugging purpose)")
