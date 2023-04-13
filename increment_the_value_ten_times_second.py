# writing the python program to extract the integers from the mixed data text file using conditional statements with out isdigit() method

f = open("increment_the_value_ten_times.txt", "r")  ## Open the file in read mode
integers = []  # Create an empty list to store the integer values
for line in f:  # for loop that iterates over each line in the file f
        integer = '' #initializes an empty string variable called integer, which will be used to store a sequence of digits from the current line.
        for char in line:   # for loop that iterates over each character in the current line of the file.
            if '0' <= char <= '9': #if statement checks if the current character is a digit between 0 and 9 
                integer += char  # If it is digit, it adds the character to the integer string
            elif integer:    # elif statement checks if the integer string is not empty, which indicates that a sequence of digits has just ended. 
                integers.append(int(integer)+5)  # If this is true, it appends the integer value of integer to the integers list
                integer = ''    # resets the integer string to an empty string.
        if integer:
            integers.append(int(integer)+5)   # This if statement checks if there are any remaining digits in the integer string after the end of the line. I
        print(integers)  # Print the list of integer values

        f = open("increment_the_value_ten_times_scond_output.txt", "w")  # open increment_the_value_ten_times_second_output.txt in write mode
        for integer in integers:
             f.write(str(integer)+ '\n')   # writing the result to increment_the_value_ten_times_second_output.txt file
print("File 'increment_the_value_ten_times_second_output.txt' has been created!")  # print file has been created
f.close()  