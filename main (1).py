#Import logo and clear function
from replit import clear
from art import l
#Add operation functions
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2
#Create a operation dictionary to save operation symbols
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
"""Create a calculator function that include for and while loops."""
def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 #When should_continue is True while loops will continue
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      #We call calculator funcion to clean and restart the calculator 
      calculator()
#You must remember that if we do not call the calculator function the code does not start
calculator()
