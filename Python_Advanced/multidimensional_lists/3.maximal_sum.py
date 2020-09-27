(rows_count,cols_count) = [int(x) for x in input().split()]
matrix = []
for i in range(rows_count):
    row = [int(x) for x in input().split()]
    matrix.append(row)

best_sum = -99999999
best_submatrix = []
for row in range(rows_count-2):
    for col in range(cols_count-2):
        current_submatrix = []
        current_sum = 0
        row_counter = 0
        for r in range(row,row+3):
            current_submatrix.append([])
            for c in range(col,col+3):
                current_submatrix[row_counter].append(matrix[r][c])
                current_sum += matrix[r][c]
            row_counter += 1
        
        if current_sum > best_sum:
            best_sum = current_sum
            best_submatrix = current_submatrix

print(f"Sum = {best_sum}")
for row in best_submatrix:
    print(" ".join([str(x) for x in row]))