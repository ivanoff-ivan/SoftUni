n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    tokens = input().split()
    command = tokens[0]
    if command == "END":
        break
    row = int(tokens[1])
    col = int(tokens[2])
    value = int(tokens[3])
    if 0 <= row < n and 0 <= col < n:
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

matrix = [[str(x) for x in r]for r in matrix]
[print(f"{' '.join(r)}") for r in matrix]