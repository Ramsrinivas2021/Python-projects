# from practice_on_variable_scope import *  # importing all the attributes in this file
import practice_on_variable_scope
from practice_on_variable_scope import _add  # using from import
# sum1 = 50
total = add()
# total = practice_on_variable_scope._add()  # calling the function defined in add module
print(total)
sum1 = 50
total = sum1 + total
print(total)