# from practice_scopes_hiding_functions1 import *  # importing all the attributes in this file
import practice_scopes_hiding_functions1
# from practice_scopes_hiding_functions1 import add  # using from import
sum1 = 50
# total = add()
# multiplication = mult()
# print(multiplication)
total = practice_scopes_hiding_functions1.add()  # calling the function defined in add module
# print(total)
# sum1 = 50
total = sum1 + total
print(total)