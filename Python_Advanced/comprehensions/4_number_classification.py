line = [int(x) for x in input().split(", ")]
positive = ", ".join([str(x) for x in line if x >= 0])
negative = ", ".join([str(x) for x in line if x < 0])
even = ", ".join([str(x) for x in line if x % 2 == 0])
odd = ", ".join([str(x) for x in line if x % 2 != 0])
print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")