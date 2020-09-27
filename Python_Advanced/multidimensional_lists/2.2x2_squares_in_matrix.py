(rows_count, cols_count) = [int(x) for x in input().split()]
matrix = []
for i in range(rows_count):
    row = [x for x in input().split()]
    matrix.append(row)

count = 0
for i in range(rows_count-1):
    for j in range(cols_count-1):
        symbol = matrix[i][j]
        if matrix[i+1][j] == symbol:
            if matrix[i][j+1] == symbol:
                if matrix[i+1][j+1] == symbol:
                    count += 1

print(count)