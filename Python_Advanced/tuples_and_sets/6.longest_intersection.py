N = int(input())
best_len = 0
best_intersection = ""

for _ in range(N):
    ranges = input().split("-")
    first_start, first_end = [int(x) for x in ranges[0].split(",")]
    second_start, second_end = [int(x) for x in ranges[1].split(",")]
    first_range = set([x for x in range(first_start,first_end + 1)])
    second_range = set([x for x in range(second_start,second_end + 1)])
    intersection = first_range.intersection(second_range)

    if len(intersection) > best_len:
        best_intersection = intersection
        best_len = len(intersection)

best_intersection = [int(x) for x in best_intersection]
print(f"Longest intersection is {best_intersection} with length {best_len}")


