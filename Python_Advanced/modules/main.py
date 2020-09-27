from triangle import operations

tokens = input().split()
last = float(tokens[0])
last = 5.6
second_umber = float(tokens[2])
operation = tokens[1]
print(f"{operations(last, second_umber, operation):.2f}")