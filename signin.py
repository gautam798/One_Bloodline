
print("Hello welcome to One Bloodline:-")
#signin steps
#function main programming
def signin():
    global result
    username = input("Enter Username/E-mail/Mobile-number: ")
    password = input("Enter New Password: ")
    result = [username,password]

#execution of functions
signin()
print(result)
print("signin process is  working fine.(only for debugging purpose)")

print(result[1])
