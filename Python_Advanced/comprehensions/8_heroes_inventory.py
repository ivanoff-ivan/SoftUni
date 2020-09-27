heroes = {hero:{} for hero in input().split(", ")}
while True:
    tokens = input().split("-")
    name = tokens[0]
    if name == "End":
        break
    item = tokens[1]
    cost = int(tokens[2])
    if item not in heroes[name]:
        heroes[name][item] = cost

[print(f"{key} -> Items: {len(value.keys())}, Cost: {sum(value.values())}") for key,value in heroes.items()]