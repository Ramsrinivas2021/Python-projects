f = open("increment_the_value_ten_times.txt", "r")   # Open the file in read mode
for line in f:     # using for loop to iterate over the each line of the file
        integers = []  # Initialize an empty list to hold the modified lines
        for word in line.split(','):    # Split the line into individual words 
            if word.isdigit():          # Check if the second word (which should be an integer) can be converted to an integer
                integer = int(word)     #converted word to integer is assigned to integer variable
                integer += 5            # adding  5 to each integer value
                integers.append(integer)   #  appending the integer result to integers [] list
        print(integers)

        f = open("increment_the_value_ten_times_first_output.txt", "a")  # open increment_the_value_ten_times_first_output.txt in write mode
        for integer in integers:
             f.write(str(integer)+ '\n')   # writing the result to increment_the_value_ten_times_output.txt file
print("File 'increment_the_value_ten_times_first_output.txt' has been created!")  # print file has been created
f.close()  