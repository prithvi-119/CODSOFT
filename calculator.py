#python program for calculator
 
def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    return num1 / num2

number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))

print("Please select a operation:\n" \
      "1. Addition\n" \
      "2. Substraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
       )
select = int(input("select a operation from 1,2,3,4 : "))

if select == 1:
    print(number1, "+", number2, "= ", \
          add(number1,number2))
    
elif select == 2:
     print(number1, "-", number2, "= ", \
          sub(number1,number2))
     
elif select == 3:
    print(number1, "*", number2, "= ", \
          multiply(number1,number2))
    
elif select == 4:
     print(number1, "/", number2 , "= ", \
            divide(number1,number2))
     
else:
    print ("Invalid  operation! Pls select again")