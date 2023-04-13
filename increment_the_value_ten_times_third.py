# writing the python program to extract the integers from the mixed data text file using conditional statements

f = open("increment_the_value_ten_times.txt", "r")  # Open the file in read mode
integers = []  # Create an empty list to store the integer values
for line in f:
        integer = ''  # Create an empty string to store the integer value
        for char in line:
            if char.isdigit():
                integer += char  # Add the digit to the integer string
            elif integer:
                integers.append(int(integer)+5)  # If this is true, it appends the integer value of integer +5 to the integers list
                integer = ''  # Reset the integer string
        if integer:
            integers.append(int(integer)+5)  # Convert the integer string to an integer and add 5 to integer list then append to the list (in case the line ends with an integer)
        print(integers)  #  # Print the list of integer values incremented by 5

        f = open("increment_the_value_ten_times_third_output.txt", "w")  # open increment_the_value_ten_times_third_output.txt in write mode
        for integer in integers:
             f.write(str(integer)+ '\n')   # writing the result to increment_the_value_ten_times_output.txt file
print("File 'increment_the_value_ten_times_third_output.txt' has been created!")  # print file has been created
f.close()  