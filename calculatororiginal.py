# a calculator that can take 2 inputs and do addition, subtraction, divison, multiplication
#date - 11th June 2024

#v1


#take 2 inputs from user 

number1 = float(input("Enter first number"))
number2 = float(input("Enter second number"))

user_input = number1, number2 #storing the values given by the user in user_input

print(" You have given", number1, "and", number2)

#asking user to select there operation

print("Select your operation")
print("1 - Addition")
print("2 - Division")
print("3 - Multiplication")
print("4 - Subtraction")

#defining what function will do 

Addition = (number1+number2)
Division = (number1/number2)
Multiplication = number1*number2
Subtraction = number2-number1

#asking user to input there option

operation_input = str(input("enter (1/2/3/4):"))

#checking and proceeding according to user input

if operation_input == "1":
    print("You have selected Addition as your operation")
    print("You result is", Addition)


if operation_input == "2":
    print("You have selected Division as your operation")
    print("You result is", Division)

if operation_input == "3":
    print("You have selected Multiplication as your operation")
    print("You result is", Multiplication)

if operation_input == "4":
    print("You have selected Subtraction as your operation")
    print("You result is", Subtraction)

else :
    print("please select the right value")


