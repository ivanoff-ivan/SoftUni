(rows,cols) = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append(input().split())

while True:
    line = input()
    if line == "END":
        break
    else:
        line = line.split()
        if line[0] != "swap":
            print("Invalid input!")
        else:
            line = line[1:len(line)]
            if len(line) == 4:
                (row1,col1,row2,col2) = [int(x) for x in line]
                if row1 < rows and row2 < rows and col1 < cols and col2 < cols:
                    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
                    for r in matrix:
                        print(" ".join(r))
                else:
                    print("Invalid input!")
            else:
                print("Invalid input!")