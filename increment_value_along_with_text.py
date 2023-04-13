# write a python program to extract all the integer values and add 5 to those integer and output should be mixed data with increneted integers

# Open the file in read mode
with open("increment_the_value_ten_times.txt", "r") as f:
    # empty list to hold the modified lines
    modified_lines = []
    # Iterate over each line in the file
    for line in f:
        # Split the line into individual words
        words = line.split(",")
        # Check if the second word (which should be an integer) can be converted to an integer
        if words[1].isdigit():
            # If it can be converted to an integer, add 5 to the integer value and convert back to a string
            new_value = str(int(words[1]) + 5)
            # Replace the old integer value with the new value in the line
            modified_line = f"{words[0]},{new_value},{words[2]}"
        else:
            # If the second word is not an integer, leave the line unchanged
            modified_line = line
        # Add the modified line to the list of modified lines
        modified_lines.append(modified_line)
            

# Open the file in write mode and write the modified lines
with open("increment_value_along_with_text_output.txt", "w") as f:
    f.writelines(modified_lines)

print("File 'increment_value_along_with_text_output.txt' has been created!!")  # print increment_value_along_with_text_output.txt file has been created