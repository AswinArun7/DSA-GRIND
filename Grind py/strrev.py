s = input("Enter a string: ")
stack = list(s)
reversed_str = ""

while stack:
    reversed_str += stack.pop()
print("Reversed string:", reversed_str)
