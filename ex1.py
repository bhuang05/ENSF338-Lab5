import sys

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]


#function created with help from ChatGPT
def evaluate(expression):
    stack = Stack()
    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        elif char == '(':
            continue
        elif char in ['+', '-', '*', '/']:
            stack.push(char)
        elif char == ')':
            operand = stack.pop()
            operand2 = stack.pop()
            operator = stack.pop()
            if operator == '+':
                stack.push(operand2 + operand)
            elif operator == '-':
                stack.push(operand2 - operand)
            elif operator == '*':
                stack.push(operand2 * operand)
            elif operator == '/':
                stack.push(operand2 // operand)
    return stack.pop()
    
arguments = sys.argv[1:]
expression = ' '.join(arguments)
result = evaluate(expression)
print(result)
