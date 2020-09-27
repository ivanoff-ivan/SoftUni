line = input().split()
[print(word) for word in line if len(word) % 2 == 0]