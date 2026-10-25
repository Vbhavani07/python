string = input("Enter a string: ")
stack = list(string)
reversed_string = ""

while stack:
    reversed_string += stack.pop()

print("Reversed string:", reversed_string)