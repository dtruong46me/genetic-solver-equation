
import math


def is_numeric(token):
    try:
        float(token)
        return True
    
    except ValueError:
        return False
    
def perform_operation(a, b, operator: str):
    if operator == '+':
        return a + b
    
    if operator == '-':
        return a - b
    
    if operator == '*':
        return a * b
    
    if operator == '/':
        if b == 0:
            raise ValueError("Division by Zero")
        return a / b
    
    if operator == '**' or operator == '^':
        return a ** b

def perform_trigonometric_function(a, function: str):
    if function == 'sin':
        return math.sin(a)
    
    if function == 'cos':
        return math.cos(a)
    
    if function == 'tan':
        return math.tan(a)
    
    if function == 'cot':
        return 1 / math.tan(a)

# Evaluation function
def evaluate(output: list, x_value):
    stack = []
    
    for e in output:
        assert isinstance(e, str)

        if e == 'x':
            stack.append(x_value)
        
        if is_numeric(token=e):
            stack.append(float(e))

        # Basic Operation
        if e in "+-*/**^":
            b = float(stack.pop())
            a = float(stack.pop())

            result = perform_operation(a, b, operator=e)
            stack.append(result)

        # Trigonometric function
        if e in ('sin', 'cos', 'tan', 'cot'):
            a = float(stack.pop())

            result = perform_trigonometric_function(a, function=e)
            stack.append(result)
        
        # Logarit
        if e in ('log', 'ln'):
            if e == 'log':
                base = float(stack.pop())
                a = float(stack.pop())
                if a < 0:
                    raise ValueError("Math Domain Error!")

                result = math.log(a, base)
            
            if e == 'ln':
                a = float(stack.pop())
                result = math.log(a, math.e)
            
            stack.append(result)

        # Square root
        if e == 'sqrt':
            a = float(stack.pop())
            if a < 0:
                raise ValueError("Square root of negative number!")
            
            result = math.sqrt(a)
            stack.append(result)

    return stack[0]

