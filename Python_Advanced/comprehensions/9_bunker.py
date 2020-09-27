all_items = {categ:{} for categ in input().split(", ")}
n = int(input())
for i in range(n):
    tokens = input().split(" - ")
    category = tokens[0]
    item_name = tokens[1]
    info = tokens[2].split(";")
    quantity = info[0].split(":")
    quantity = int(quantity[1])
    quality = info[1].split(":")
    quality = int(quality[1])
    if category in all_items.keys():
        if item_name not in all_items[category]:
            all_items[category][item_name] = [0,0]
        all_items[category][item_name][0] += quantity
        all_items[category][item_name][1] += quality

count_of_items = []
quality_sum = []
[[(count_of_items.append(v[0]), quality_sum.append(v[1])) for v in value.values()] for value in all_items.values()]
print(f"Count of items: {sum(count_of_items)}")
categories_count = len([key for key in all_items.keys()])
average_quality = sum(quality_sum)/categories_count
print(f"Average quality: {average_quality:.2f}")
[print(f"{key} -> {', '.join(value)}")for key,value in all_items.items()]