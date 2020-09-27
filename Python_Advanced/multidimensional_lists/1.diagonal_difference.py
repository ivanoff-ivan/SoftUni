N = int(input())
matrix = []
for _ in range(N):
    line = [int(x) for x in input().split()]
    matrix.append(line)

primary_diagonal_sum = 0
for i in range(N):
    primary_diagonal_sum += matrix[i][i]

secondary_diagonal_sum = 0
for i in range(N):
    j = N - i - 1
    secondary_diagonal_sum += matrix[i][j]

result = abs(primary_diagonal_sum - secondary_diagonal_sum)
print(result)