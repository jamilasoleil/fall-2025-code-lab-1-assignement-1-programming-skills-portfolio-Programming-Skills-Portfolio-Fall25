
password = "12345"
#this line of code declares set password


count = 5
print(f"You have: {count} tries")
#this line of code declares the number of tries available to the user

while count > 0: #this line of code checks if the attempt was valid
    setpassIN = input("Enter Password: ") #this line of code asks the user to input the password


    if setpassIN == password: 
        print("Correct Password!")
        break #this line of checks if the password is valid
    else: #this line of code checks if the password is invalid
        count -= 1
        print("Incorrect Password")
        print(f"You have: {count} tries") 
        if count > 0 :
            print ("Try Again")
        if count == 0 :
            print("No more Tries")
            print("Locking...")