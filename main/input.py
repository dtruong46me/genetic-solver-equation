
# Reverse Polish Notation
def reverse_polish_notation(tokens: list) -> list:

    priority = {'+': 1,'-': 1,'/': 2,'*': 2,'^': 3,'**': 3}

    output = []
    stack = []

    for token in tokens:
        assert type(token) == str

        if token == 'x':
            output.append(token)

        if token.isdigit() or (token[0]=='-' and token[1:].isdigit()) or '.' in token:
            output.append(token)

        if token in ('sin', 'cos', 'tan', 'cot', 'log', 'ln', 'sqrt'):
            stack.append(token)

        if token in "+-/^**":
            while len(stack) != 0 and (stack[-1] in '+-/^**') and priority.get(token, 0) <= priority.get(stack[-1], 0):
                output.append(stack.pop())
            
            stack.append(token)

        if token == "(":
            stack.append(token)

        if token == ")":
            while len(stack) != 0 and stack[-1] != '(':
                output.append(stack.pop())
            
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()

            if len(stack) != 0 and stack[-1] in ('sin', 'cos', 'tan', 'cot', 'log', 'ln', 'sqrt'):
                output.append(stack.pop())
            

    while len(stack) != 0:
        output.append(stack.pop())

    return output


# Get token list from the expression
def tokenize(expression: str) -> list:

    tokens = []
    curr_token = ""

    for char in expression:
        if char.isdigit() or char.isalpha() or char == '.':
            curr_token += char

        else:
            if curr_token:
                tokens.append(curr_token)
            
            if char.strip():
                tokens.append(char)
            
            curr_token = ""
    
    if curr_token:
        tokens.append(curr_token)

    return tokens
