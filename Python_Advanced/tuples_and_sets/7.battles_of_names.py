N = int(input())
odd_set = set()
even_set = set()

for i in range(1, N + 1):
    name = input()
    the_sum = sum(ord(char) for char in name) // i
    
    if the_sum % 2 == 0:
        even_set.add(the_sum)
    else:
        odd_set.add(the_sum)    

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    union_values = odd_set.union(even_set)
    print(", ".join([str(x) for x in union_values]))   
elif odd_sum > even_sum:
    different_values = odd_set.difference(even_set)
    print(", ".join([str(x) for x in different_values]))  
else:
    symetric_values = odd_set.symmetric_difference(even_set)
    print(", ".join([str(x) for x in symetric_values]))