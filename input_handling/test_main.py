# big_text = "sin(x) + 5^x - log((x^2 + 1)*5, (x^2 + 1)) + cos(x) - log((x+1), 5)"
# print(big_text.find("log"))
# text = "log((x^2 + 1)*5, (x^2 + 1))"
# new_text= text[4:-1]
# print(new_text.split(","))

"""
import re
big_text = "sin(x) + 5^x - log((x^2 + 1)*5, (x^2 + 1)) + cos(x) - log((x+1), 5)"
log_expressions = re.findall(r'log\([^)\*,]*\)', big_text)

if log_expressions:
    for log_expression in log_expressions:
        print(log_expression)
else:
    print("No 'log' expression found in big_text.")
"""
# import re

# big_text = "sin(x) + 5^x - log((x^2 + 1)*5, (x^2 + 1)) + cos(x) - log((x+1), 5)"
# log_expressions = re.findall(r'log\([^)]*\)', big_text)

# if log_expressions:
#     print(log_expressions)
# else:
#     print("No 'log' expressions found in big_text.")

# import re

# big_text = "sin(x) + 5^x - log((x^2 + 1)*5 - (x+1), (x^2 + 1)) + cos(x) - log((x+1), 5)"
# new_text = big_text.replace(")", "")
# print(new_text)
# print()
# log_expressions = re.findall(r'log\([^)]+\)[^)]+', big_text)

# if log_expressions:
#     print(log_expressions)
# else:
#     print("No 'log' expressions found in big_text.")
'''
import re

def find_logarithms(expression):
    logarithm_pattern = r'log\((.*?)\, (.*?)\)'
    logarithms = re.findall(logarithm_pattern, expression)

    return [f"log({args[0]}, {args[1]})" for args in logarithms]

# Biểu thức toán học đầu vào
input_expression = "sin(x) + 5^x - log((x^2 + 1)*5 - (x+1) -3 + e^x , abs(x+1) - 5) + cos(x) - log(x+1, 5 + e)"
    
res = find_logarithms(input_expression)
print(res)
print()
for i in res:
    print(i[4:].split(","))
'''

from utils import Utils
x = "sin(x) + 5^x - log((x^2 + 1)*5 - (x+1) -3 + e^x , abs(x+1) - 5) + cos(x) - log(x+1, 5 + e)"
y = [i for i in x]

util = Utils()
log_list = []
while True:
    res = ''
    par = ''
    idx = x.find('log')
    if idx == -1:
        break
    while True:
        res += y[idx]
        if y[idx] == '(' or y[idx] == ')':
            par += y[idx]

        if util.check_match(par):
            break
        y.pop(idx)

    log_list.append(res)
    

print(log_list)


# "0123456789"
