N = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(N)]
first_diag = [matrix[i][i] for i in range(N)]
second_diag = [matrix[i][N-i-1] for i in range(N)]
print(f"First diagonal: {', '.join([str(x) for x in first_diag])}. Sum: {sum(first_diag)}")
print(f"Second diagonal: {', '.join([str(x) for x in second_diag])}. Sum: {sum(second_diag)}")