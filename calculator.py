print("Calculator")
print("Selct the operation you want to perform")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
choice=int(input("Enter your choice: "))
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
if choice==1:
    print("Result: ",num1+num2)
elif choice==2:
    print("Result: ",num1-num2)
elif choice==3:
    print("Result: ",num1*num2)
elif choice==4:
    if num2==0:
        print("Invalid: Division by zero not possible")
    else:
        print("Result: ",num1/num2)
elif choice==5:
    print("Exiting the calculator")
    exit()


