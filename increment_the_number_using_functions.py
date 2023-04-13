def read_integers_from_file (inputfile, outputfile):  # defines a function called read_integers_from_file that takes two arguments: inputfile and outputfile
    integers = []   # initializes an empty list called integers that will be used to store the incremented integer values.
    with open("C:\Python Projects @ bava\increment_the_value_ten_times.txt", 'r') as f:  # opens this path file in read ony mode assigns to f
        for line in f:   # iterate over each line in the input file 
            words = line.split(',')  # split each line into a list of words using commas as the delimiter.
            for word in words:   # iterates over each word in the line,
                if word.isdigit():  #  the code checks whether it is a digit using the isdigit() method
                    incremented_value = int(word) + 5   #  If the word is a digit, it increments the value by 5 and assigns it to incremented_value
                    integers.append(int(incremented_value))  # appends the incremented value to the integers list.
    return integers    #  returns the integers list, which contains the incremented integer values.
# calls the inputfile and outputfile as arguments, and assigns the returned list of integers to the variable integers.
integers = read_integers_from_file("C:\Python Projects @ bava\increment_the_value_ten_times.txt",  "C:\Python Projects @ bava\increment_the_value_using_functions_output.txt")
print(integers)  # prints the list of incremented integer values
with open("C:\Python Projects @ bava\increment_the_value_using_functions_output.txt", 'w') as f:  # opens the output file ("C:\Python Projects @ bava\increment_the_value_using_functions_output.txt") in write mode assigns it to f
        # ensures that the file is properly closed when the code inside the with block is done executing.
        for integer in integers:  # iterates over each integer in the integers list,
            f.write(str(integer) + '\n')  #converts the integer value into a string then writes the argument string to the file by next write to start on a new line.