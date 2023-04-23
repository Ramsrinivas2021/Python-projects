# # Local scope: Variables that are declared inside a function have local scope. 
# # They can only be accessed within that function.

# def my_function():  # defined function here
#   x = 10 # x has local scope
#   print(x)

# my_function() # output: 10
# print(x) # NameError: name 'x' is not defined

# # Global scope: Variables that are declared outside of any function have global scope. 
# # They can be accessed anywhere in the code.
# x = 10 # x has global scope

# def my_function():
#   print(x)

# my_function() # output: 10
# print(x) # output: 10

# x = 10 # global variable

# def my_function():
#   x = 5 # local variable
#   print("Inside function: x =", x)

# my_function()
# print("Outside function: x =", x)


# # Enclosing scope: Variables that are declared in a nested function have enclosing scope. 
# # They can be accessed by any function that is nested within the outer function.
# def outer_function():
#   x = 10 # x has enclosing scope
#   def inner_function():
#     print(x)
#   inner_function()

# outer_function() # output: 10

# # Stack memory: This is where variables are stored when they are declared in a function. 
# # The memory for these variables is automatically released when the function returns.
# def my_function():
#   x = 10 # x is stored in stack memory
#   print(x)

# my_function() # output: 10

# # Heap memory: This is where objects and data structures are stored. 
# # Python's garbage collector automatically frees up memory that is no longer being used by the program.

# global x 
x = 4
y = 5
def my_func():
    x = 5
    #  sum
    sum1 = x + y
    print("Sum :",sum1)
    return sum1
abc = my_func()
print(abc)
total = sum1 + 10
print("Total:",total)