def my_function():
   print("IN MY FUNCTION")
   return 1

# x = my_function()
# print(x)
f = my_function
print(f)
new_x = f()
new_x = my_function()
print(new_x)
