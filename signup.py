
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
    if password==password1:
        result = [username,email,number,password]
    else :
        print("Try Again! password didnt match")
        signup()
#execution of functions
signup()
print(result)
print("signup process is  working fine.(only for debugging purpose)")
