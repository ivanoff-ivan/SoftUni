line = {x: len(x) for x in input().split(", ")}
result = [f"{key} -> {value}" for key,value in line.items()]
print(", ".join(result))