command = input()
nums = list(map(int, input().split()))
if command == "Odd":
    odd_nums = list(filter(lambda x: x % 2 != 0, nums))
    result = sum(odd_nums) * len(nums)
elif command == "Even":
    even_nums = list(filter(lambda x: x % 2 == 0, nums))
    result = sum(even_nums) * len(nums)

print(result)

