

def is_prime(incoming_number):
    # 13
    # 0, 1, 2, 3... 13?
    #  2 ... 12
    #  2 ... x  / 2 + 1
    for x in range(2, incoming_number // 2 + 1):
        if incoming_number  % x == 0:
            return False
      
    return True

def find_primes(list_of_numbers):
    primes = []
    for x in list_of_numbers:
        if is_prime(x):
            primes.append(x)

    return primes 

def find_factors(n):
    all_factors = [] # building this collection
    # from another collection:
    # range(1,n)
    for x in range(1,n):
        if n % x == 0:
            all_factors.append(x)
        # else:
    return all_factors

def find_max_prime(n):
     # from another collection:
    # range(1,n)
    max_prime = 0
    for x in range(1,n // 2 + 1):
        if n % x == 0 and is_prime(x) :
            max_prime = x
        # else:
    return max_prime

number = 13195 # 600851475143
all_factors = find_max_prime(number)
print("All factors: ", all_factors)
# all_prime_numbers = find_primes(all_factors)
# print("All primes: ", all_prime_numbers)
# max_prime = max(all_prime_numbers)
# print(max_prime)