Name = str(input("Enter Name: "))
Hometown = str(input("Enter Hometown: "))
Age = input("Enter Age: ")
#this line of code asks for the users information for biography

Dictionary = {"Name" : Name,
              "Hometown" : Hometown,
              "Age" : Age}
#this line of code stores the information thats been put in by the user from the previous line of code

while True: 
    if Age.isdigit() == True:
        break
    else:
        print("Enter A Digit!")
        Age = input("Enter Age: ")
#this line of code checks the age entered by the user is valid



print(f"Username : {Dictionary["Name"]} \nHometown : {Dictionary["Hometown"]} \nAge : {Dictionary["Age"]}")
#this line of code outputs the final biography
