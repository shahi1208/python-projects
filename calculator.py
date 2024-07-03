# Skills Utilized: Basic Python syntax, functions, user input/output, looping, recursion.


## Mistake correction.

# The operator recursion is solved. 
# This time you can enter multiple 
# invalid operators without the system 
# throwing any error.


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        print('ZeroDivisionError: Denominator cannot be zero')
        b = int(input('Enter a new value for Denominator:'))
        print()
        return div(a,b)
    return a/b

x = ''
def print_statements():
    print('Press Y to continue. X to terminate.')
    global x 
    x = input('X OR Y?').strip().upper()
    print()

sym = ['+','-','*','/']

print('Welcome to my calculator. Press Y to start.\n')

print_statements() 
while x=='Y':
    a = int(input('enter first value:'))
    print()
    print(f'Available operators- {sym}\n')
    op = input('enter an operator:').strip()
    print()

    # this func takes the operator and checks if its in sym list.
    def oper(op):
        if op not in sym: # if not asks the user to enter again.
            print(f'Invalid operator. Choose one among these {sym}\n')
            op = input('enter an operator:').strip()
            print()
            # using recursion to enter the function again 
            # in order to check if the operator is in sym list or not. 
            return oper(op)
        return op
    
    op = oper(op)

    b = int(input('enter second value:'))
    print()


    if op == '+':
        result=add(a,b)

    elif op == '-':
        result=sub(a,b)

    elif op == '*':
        result = mul(a,b)
        
    elif op == '/':
        result = div(a,b)

    print(result)  
    print_statements()
    print()

print('calculator is closed.')