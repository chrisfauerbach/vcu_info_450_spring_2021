


def sum_all_multiples_3_5(n):
    all_numbers = []
    for x in range(n): 
        if x % 3 == 0 or x % 5 == 0:
            all_numbers.append(x)

    total = sum(all_numbers)

    return total
 
# O(n)

def sum_all_multiples_3_5_second(n):
    total = 0
    for x in range(n): 
        if x % 3 == 0 or x % 5 == 0:
            # total = total + x
            total += x

    # total = sum(all_numbers)

    return total
 



assert sum_all_multiples_3_5(10) == 23
 
assert sum_all_multiples_3_5(1000) == 233168