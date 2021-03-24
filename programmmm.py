#write a program to take a input from the user, ask the users age. if the age is below 15. print a message "you are a child." if the users age is greater then 50 and lesser then 40 print the message "you are adult." if the users age greater than print a message "you are old."
age=int(input("enter the age"))
if age<15:
    print("you are a child")
elif age>15 and age<=40:
    print("you are adult")
elif age>40:
    print("you are old")
