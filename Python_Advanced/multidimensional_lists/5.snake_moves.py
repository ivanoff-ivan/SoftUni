(rows_count,cols_count) = [int(x) for x in input().split()]
snake = [char for char in input()]
char_counter = 0
matrix = []
for i in range(rows_count):
    current_row = []
    for j in range(rows_count + 1):
        if char_counter >= len(snake):
            char_counter = 0
        current_row.append(snake[char_counter])
        char_counter += 1
    matrix.append(current_row)

for i in range(len(matrix)):
    if i % 2 != 0:
        matrix[i] = [x for x in reversed(matrix[i])]

for row in matrix:
    print("".join(row))
