# link -- https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1

"""
Let's take two examples:

Left-associative operators (like +, -, *, /):

Expression: a + b + c
Grouping: (a + b) + c (evaluated from left to right)
Postfix: ab+c+
Right-associative operators (like ^):

Expression: a ^ b ^ c
Grouping: a ^ (b ^ c) (evaluated from right to left)
Postfix: abc^^
In our conversion algorithm, associativity affects when we pop operators from the stack:

For left-associative operators: When we see an operator with equal precedence, we pop the stack (because we want to evaluate the previous operation first)
For right-associative operators: When we see an operator with equal precedence, we don't pop the stack (because we want to evaluate the later operation first)
"""

def InfixToPostfix(s: str) -> str:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    right_assoc = {'^'}
    stack = []
    result = ""
    i = 0 
    while i < len(s):
        if s[i].isalnum():
            result += s[i]
        elif s[i] == "(":
            stack.append(s[i])
        elif s[i] == ")":
            while stack and stack[-1] != "(":
                result += stack.pop()
            if stack and stack[-1] == "(":
                stack.pop()
        else:
            while (stack and stack[-1] != "(" and 
                  (precedence[stack[-1]] > precedence[s[i]] or
                   (precedence[stack[-1]] == precedence[s[i]] and s[i] not in right_assoc))):
                result += stack.pop()
            stack.append(s[i])
        i+=1
    while stack:
        result+=stack.pop()
    return result

if __name__=='__main__':
    s = 'hmAq^(7-4)'
    print(InfixToPostfix(s))
    




