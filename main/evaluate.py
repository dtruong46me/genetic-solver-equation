
import math

def evaluate(output: list, x_value):

    stack = []
    
    for e in output:
        
        assert isinstance(e, str)

        if e == 'x':
            stack.append(x_value)
        
        if e.isdigit():
            stack.append(e)

        # Basic Operation
        if e in "+-/^**":
            a = float(stack.pop())
            b = float(stack.pop())

            if e == '+':
                c = b + a
            
            if e == '-':
                c = b - a
            
            if e == '*':
                c = b * a
            
            if e == '/':
                try:
                    c = b / a
                except:
                    print("Cannot divide 0!")
            
            if e == '**' or e == '^':
                c = b ** a
            
            stack.append(c)

        # Trigonometric function
        if e in ('sin', 'cos', 'tan', 'cot'):
            a = float(stack.pop())

            if e == 'sin':
                c = math.sin(a)
            
            if e == 'cos':
                c = math.cos(a)
            
            if e == 'tan':
                c = math.tan(a)
            
            if e == 'cot':
                try:
                    c = 1 / math.tan(a)
                except:
                    print("Cannot divide 0!")
            
            stack.append(c)

            # print("stack:", stack)
        
        # Logarit
        if e in ('log', 'ln'):
            if len(stack) == 2:
                base = float(stack.pop())
                a = float(stack.pop())

                c = math.log(a, base)
            
            if len(stack) == 1:
                a = float(stack.pop())

                if e == 'log':
                    c = math.log10(a)
                
                if e == 'ln':
                    c = math.log(a, math.e)
            
            stack.append(c)
            # print("stack:", stack)

    result = stack.pop()

    return result