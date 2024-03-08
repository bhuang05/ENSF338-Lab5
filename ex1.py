import sys

class Stack:
    def __init__(self):
        self._items = []

    def push(self, val):
        self._items.append(val)

    def pop(self):
        if not self._items:
            return None
        else:
            return self._items.pop()
    
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
