a = int(input("Enter a number      :"))
b = int(input("Enter second number :"))
print("Which operation you would like to do....")
print("press 0 for addition")
print("press 1 for subtraction")
print("press 2 for multiplication")
print("press 3 for divison")

x = int(input("Give the digit :"))
if(x==0):
    sum = a+b
    print("Addition of both the numbers is :",sum)
elif(x==1):
    subtraction = a-b
    print("Subtraction of both the numbers is :",subtraction)
elif(x==2):
    multiplication = a*b
    print("Multiplication of both numbers is :",multiplication)
elif(x==3):
    division = a/b
    print("Division of both numbers is :",division)