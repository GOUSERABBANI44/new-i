import sys

#Calling functions for addtition, subtraction and multiplication
def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
#Ensuring the arguments with parameters

num1 = int(sys.argv[1])
operator = sys.argv[2]
num2 = int(sys.argv[3])

if operator == 'addition':
    output = add(num1, num2)
    print(output)
elif operator == 'subtraction':
    output = sub(num1, num2)
    print(output)
elif operator == 'multiplication':
    output = mul(num1, num2)
    print(output)
else:
    print("Enter the valid operator")        


