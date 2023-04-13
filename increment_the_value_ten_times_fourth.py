# writing the python program to extract the integers from the mixed data text file using re.findall() function

import re

with open('increment_the_value_ten_times.txt') as file:  # Open the file in read mode
    integers = []  # Create an empty list to store the integer values
    for line in file:
        # Use a regular expression to find all integer values in the line
        matches = re.findall(r'\d+', line)
        for match in matches:
            integer = int(match) +5  # converting integer string to integer and add 5 to integer list
            integers.append(integer)  # Append the integer to the list
    print(integers)  # Print the list of integer values


    f = open("increment_the_value_ten_times_fourth_output.txt", "w")  # open increment_the_value_ten_times_fourth_output.txt in write mode
for num in integers:
 f.write(str(num)+ '\n')   # writing the result to increment_the_value_ten_times_fourth_output.txt file
print("File 'increment_the_value_ten_times_fourth_output.txt' has been created!")  # print file has been created