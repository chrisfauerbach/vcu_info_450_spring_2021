

MAX_NUMBER = 999
MIN_NUMBER = 10

# have a collection
# have two collections  (1-99) (1-99)
def is_palindrome(n):
    number_string = str(n)
    reversed_string = number_string[::-1]

    if reversed_string == number_string:
        return True

    return False
    # if len(number_string) % 2 == 1:
    #    return False

    # 131
    # 1001
    # 9555 5559
    half_length = round(len(number_string) /  2)
   #  print("Half: ", half_length)
    first_half = number_string[0:half_length] 
    # print(first_half)

    second_half = number_string[-half_length:]
   #  print(second_half)
    new_second_half = second_half[::-1]
   #  print(new_second_half)

    
    if first_half == new_second_half:
        return True

    return False

 


print(is_palindrome(131))
print(is_palindrome(1221)) 
print(is_palindrome(11))
print(is_palindrome(12345))
# sys.exit(1)


max_number = 0
for x in range(MIN_NUMBER,MAX_NUMBER+1):
    for y in range(MIN_NUMBER, MAX_NUMBER + 1):
        # print(x, ": ", y)
        prod = x * y
        if is_palindrome(prod):
            if prod > max_number:
                max_number = prod
                

print("MAX: ", max_number)