line = input()
occurences = {}

for letter in line:
    if letter not in occurences.keys():
        occurences[letter] = 0
    occurences[letter] += 1

for key,value in sorted(occurences.items()):
    print(f"{key}: {value} time/s")