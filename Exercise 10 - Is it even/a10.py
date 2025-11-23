#this line of code determines if the number given is odd or even
def OddEven(num):
    if num % 2 == 0: #this line of code checks if the number given is divisible by 2
        return "Number is Even" #this line of code returns as even
    else:
        return "Number is Odd" #this line of code returns as odd
#

a = int(input("Enter a number: "))
#this line of code asks the user to input a number
OddEven(a)

Output = OddEven(a)
print(Output)
#this line of code prints the returned value
