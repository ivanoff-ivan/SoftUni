line = [[y for y in x.split()] for x in reversed(input().split("|"))]
vector = ""
for element in line:
    for elem in element:
        vector += elem + " "
vector = vector.split()
print(' '.join(vector))