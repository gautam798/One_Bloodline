# importing necessary modules

from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg


# starting with userinterface
root = Tk()
# size of file
root.geometry("1390x700")
# title of file
root.title("One-Bloodline")
#function for input validation
# def Take_input():
#     INPUT = usernamevalue.get()
#     print(INPUT)
#     if (INPUT == "gautam"):
#         Output.insert(END, 'Correct')
#     else:
#         Output.insert(END, "Wrong answer")


# label for python
label = Label(text="Welcome to One-Bloodline", bg="red", fg="white", font=(" comicsansms ", 19, "bold"))
label.pack(side="top", fill=X, padx=20, pady=12)
#image
image = Image.open("ONE.png")
photo = ImageTk.PhotoImage(image)

image_section = Label(image=photo)
image_section.pack(anchor="n")
# to get min size of main window
root.minsize(300, 300)
# to get maximuim size of main window
# root.maxsize(800, 600)

#function to buffer

def load():
    print("submiting form")

    print(f"{namevalue.get(), emailvalue.get(), numbervalue.get(), bloodvalue.get(), adhaarvalue.get()}")
    with open("records.TXT", "a") as f:
        f.write(f"\n{namevalue.get(), emailvalue.get(), numbervalue.get(), bloodvalue.get(), adhaarvalue.get()}")
        b = tmsg.showinfo("Congrats","Your Account Has Been Created Sucessfully")

#submit function
def submit():
    print("sucess")
    value = bloodvalue.get()
    pincode =pincodevalue.get()
    print(pincode)
    print(value)
    if value == "AB+":
        def a():
            print("Function AB+")
            a1 = tmsg.showinfo("Contact This Person", "Donar Name:Neel Kotnis\n Blood Group: AB+\n Number:9999999999")
        a()
    elif value == "B+":
        def b():
            print("Function B+")
            a2 = tmsg.showinfo("Contact This Person",
                               "Donar Name: Samiksha Palande\n Blood Group: B+\n Number:8888888888")
        b()
    elif value == "A+":
        def c():
            print("Function A+")
            a3 = tmsg.showinfo("Contact This Person",
                               "Donar Name: Gautam Suvarna\n Blood Group: A+\n Number:6767676767")
        c()
    elif value == "O+":
        def d():
            print("Function O+")
            a4 = tmsg.showinfo("Contact This Person", "Donar Name:Venus Solanki\n Blood Group: O+\n Number:9998765499")
        d()
    elif value == "O-":
        def e():
            print("Function O-")
            a5 = tmsg.showinfo("Contact This Person", "Donar Name:Pratham Tank\n Blood Group: O-\n Number:4444449999")
        e()
    elif value == "AB-":
        def f():
            print("Function AB-")
            a6 = tmsg.showinfo("Contact This Person", "Donar Name:Vans \n Blood Group: AB-\n Number:123456789")
        f()
    elif value == "B-":
        def g():
            print("Function B-")
            a7 = tmsg.showinfo("Contact This Person", "Donar Name: Prem Sangle\n Blood Group: B-\n Number:8887778888")
        g()
    elif value == "A-":
        def h():
            print("Function A-")
            a8 = tmsg.showinfo("Contact This Person",
                               "Donar Name: Sahil Wadwekar\n Blood Group: A-\n Number:7897776767")
        h()
    else:
        a = tmsg.showinfo("No Data", "Sorry we donnot have Any Person in your pincode")

#loggin
def login():
    b = tmsg.showinfo("Sorry","This feature is under Maintainance")


#right side frame
f2 =Frame(root,bg="grey", borderwidth=1,relief=SUNKEN)
f2.pack(anchor="ne",padx=50,side=TOP,pady=40)
label2 = Label(f2,text="Sign in",bg="black",fg="white",padx=160)
label2.grid(column=1)
# label1.pack(pady=240,padx=100,side="top")
#sign in
username = Label(f2, text="Enter Username:")
password = Label(f2, text="Enter password:")
username.grid(row=1)
password.grid(row=2)
usernamevalue = StringVar()
passwordvalue = StringVar()

usernameentry = Entry(f2, textvariable = usernamevalue,width=60)
passwordentry = Entry(f2, textvariable = passwordvalue,width=60)
usernameentry.grid(row=1, column=1)
passwordentry.grid(row=2, column=1)
b3 = Button(f2, fg="black",bg="white", text="Submit", command=login,padx=90)
b3.grid(column=1,row=4)

#signup column
# f3 =Frame(root,bg="grey", borderwidth=1,relief=SUNKEN)
# f3.pack(side=TOP,anchor="center")
label3 = Label(f2,text="Sign Up",bg="black",fg="white",width=30)
label3.grid(column=5,row=0)
# label1.pack(pady=240,padx=100,side="top")

label4 =Label(f2,text="OR",width=10,bg="black",fg="white")
label4.grid(column=4,row=3,padx=12)

Name = Label(f2, text="Enter Full Name:",width=30)
Email = Label(f2, text="Enter Your Email:",width=30)
Number = Label(f2, text="Enter Your Mobile Number:",width=30)
blood = Label(f2, text="Enter Your Blood Group:",width=30)
Adhaar = Label(f2, text="Enter Your Adhaar-card No:",width=30)
Name.grid(row=1,column=5)
Email.grid(row=2,column=5)
Number.grid(row=3,column=5)
blood.grid(row=4,column=5)
Adhaar.grid(row=5,column=5)

namevalue = StringVar()
emailvalue = StringVar()
numbervalue = StringVar()
bloodvalue = StringVar()
adhaarvalue = StringVar()

nameentry = Entry(f2, textvariable = namevalue,width=70)
emailentry = Entry(f2, textvariable = emailvalue,width=70)
numberentry = Entry(f2, textvariable = numbervalue,width=70)
bloodentry = Entry(f2, textvariable = bloodvalue,width=70)
adhaarentry = Entry(f2, textvariable = adhaarvalue,width=70)
nameentry.grid(row=1, column=6)
emailentry.grid(row=2, column=6)
numberentry.grid(row=3, column=6)
bloodentry.grid(row=4, column=6)
adhaarentry.grid(row=5, column=6)
b3 = Button(f2, fg="black",bg="white", text="Submit", command=load,padx=90)
b3.grid(column=6,row=6,pady=15)


#left side frame
f1 =Frame(root,bg="grey", borderwidth=1,relief=SUNKEN)
f1.pack(side=LEFT,anchor="n",pady=50,fill=X,padx=60)
label1 = Label(f1,text="Urgent Blood Requirement",bg="black",fg="white",width=60)
label1.grid(column=1)
# label1.pack(pady=240,padx=100,side="top")

pincode = Label(f1, text="Enter Pincode:",padx=33)
bloodgroup = Label(f1, text="Enter patient blood-group:")
pincode.grid(row=1)
bloodgroup.grid(row=2)
pincodevalue = StringVar()
bloodvalue = StringVar()

pincodeentry = Entry(f1, textvariable = pincodevalue,width=70)
bloodentry = Entry(f1, textvariable = bloodvalue,width=70)
pincodeentry.grid(row=1, column=1)
bloodentry.grid(row=2, column=1)
b2 = Button(f1, fg="black",bg="white", text="Submit", command=submit,padx=90)
b2.grid(column=1,row=3)

#display feature
# Display = Button(f1, height=2,
#                  width=20,
#                  text="Show",
#                  command=lambda: Take_input())
#
# Display.grid(column=4,row=1)

root.mainloop()
