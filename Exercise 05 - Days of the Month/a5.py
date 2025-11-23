Month = {1 : "January",
         2 : "Febuary",
         3 : "March",
         4 : "April",
         5 : "May",
         6 : "June",
         7 : "July",
         8 : "August",
         9 : "September",
         10 : "October",
         11 : "November",
         12 : "December"}
#this line of code declares a dictionary for the number of a month

Days = {1 : 31,
        2 : 28,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31}
#this line of code declares a dictionary for the days corresponding to a month

A = int(input("Number of the Month: "))
#this line of code asks for the number of the month

B = A in Month
#this line of code asks for the number of the day of the month

if B == True: 
    print(f"Your Month is Valid! \nMonth : {Month[A]} \nDays : {Days[A]}")
else: 
    print("This Month is not Valid!")
#this line of codde declares if the input is valid or invalid