# Kardelen Gel - 181805057

print("CALCULATOR")
print("   ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
print("    ")

def addition(a, b):
   return a + b

def subtraction(a, b):
   return a - b

def multiplication(a, b):
   return a * b

def division(a, b):
   return a / b

while True:
    transaction=input(" Please, select the transaction number which you want to do: ")

    if transaction == "1":
        number1=int(input("First number:"))
        number2=int(input("Second number:"))
        try:
            print(number1, "+", number2, "=", addition(number1, number2))
        except ValueError:
            print("Please, only enter numbers!")

    elif transaction == "2":
        number1=int(input("First number:"))
        number2=int(input("Second number:"))
        try:
            print(number1, "-", number2, "=", subtraction(number1, number2))
        except ValueError:
            print("Please, only enter numbers!")

    elif transaction == "3":
        number1=int(input("First number:"))
        number2=int(input("Second number:"))
        try:
            print(number1, "*", number2, "=", multiplication(number1, number2))
        except ValueError:
            print("Please, only enter numbers!")

    elif transaction == "4":
        number1=int(input("First number:"))
        number2=int(input("Second number:"))
        try:
            print(number1, "/", number2, "=", division(number1, number2))
        except ValueError:
            print("Please, only enter numbers!")
        except ZeroDivisionError:
            print("You cannot divide numbers by zero!")

    elif transaction == "5":
        print("The program has ended.")
        break

    else:
        print("Invalid choice!")

