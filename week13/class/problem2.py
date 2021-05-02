
# starting with 1 and 2 we're....
# 

fib = []
total = 3
first = 1
second = 2

fib.append(first)
fib.append(second)

# For loop: iterating over collection
next_sequence_number = 0

while True: 
   next_sequence_number = first + second
   if next_sequence_number >= 4000000:
       break
   print(": ", next_sequence_number)
   first = second
   second = next_sequence_number
   if next_sequence_number % 2 == 0:
        # total = total + x
        total += next_sequence_number
  
print(total)
    # total = sum(all_numbers)
