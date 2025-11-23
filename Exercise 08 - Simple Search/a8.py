a = input("Enter Name 1: ").title()
b = input("Enter Name 2: ").title()
c = input("Enter Name 3: ").title()
d = input("Enter Name 4: ").title()
e = input("Enter Name 5: ").title()
f = input("Enter Name 6: ").title()
#this line of codes states the names given by the user

Names = (a, b, c, d, e, f)
#this line of codes stores the names given by the user

print(Names)
Search = input("Search Name: ").title()
#this line of code asks for the declared variable

if Search in Names:
    print(f"Name > {Search.title()} < : exists")
else:
    print("Name does not exist")
#this line of code validates the input given by the user
