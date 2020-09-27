nums = list(map(int, input().split()))

positives = sum(filter(lambda x: x > 0, nums))
negatives = sum(filter(lambda x: x < 0, nums))

print(f"{negatives}")
print(f"{positives}")

if abs(negatives) > positives:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")



