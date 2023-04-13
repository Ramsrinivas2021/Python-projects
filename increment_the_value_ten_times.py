# writing the python program to extract the integers from the moxed data text file using for loop

f = open("increment_the_value_ten_times.txt", "r")  # Open the file in read mode
# Initialize an empty list to hold the modified lines
incremented_values = []
    # Iterate over each line in the file
for line in f:                
        # Split the line into individual words
        words = line.split(',')
        if words[1].isdigit(): # Check if the second word (which should be an integer) can be converted to an integer
                integer =int(words[1]) + 5   #converted word to integer and adding  5 to each integer value then assigned to integer variable
                incremented_values.append(integer) #appending the integer result to incremented_values [] list
                
f.close()
f = open("increment_the_value_ten_times_output.txt", "w")  # open increment_the_value_ten_times_output.txt in write mode
for num in incremented_values:
 f.write(str(num)+ '\n')   # writing the result to increment_the_value_ten_times_output.txt file
print("File 'increment_the_value_ten_times_output.txt' has been created!")  # print file has been created
f.close()  
