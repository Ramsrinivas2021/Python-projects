# requirement is to get the numeric value from the mixed data text file and increment that numeric value with 5
f = open("Read_only_number_to_increment.txt", "r")  ## Open the file in read mode
data = f.read()       # Read the first line of the file
print(data)
list = data.split(',')  # Split the line into a list of values using the comma separator
print(list)
num = int(list[1])  # Getting the second value from the list and converting it to an integer
print(num)
increment = num +5  # Increment the number with +5 and assigning it to increment variable
print(increment)
f = open("output1.txt", "a")  # open output1.txt in write mode
f.write(str(increment)+ '\n')   # writing the result to output1.txt file
print("File 'output1.txt' has been created!")  # print file has been created
f.close()                                       # close the file

print("-------------------------------------------------------------------------------------------------------------\n \"find second approach below\"")

# with open('Read_only_number_to_increment.txt', 'r') as f:
#     for line in f:
#         integer = ''
#         print(line)
#         for character in line:
#             if character.isdigit():
#                 integer += character
#                 print(integer)
#             elif integer:
#                 # Integer found, do something with it
#                 incremented_integer = int(integer) + 5
#                 print(incremented_integer)
#                 integer = ''
#         if integer:
#             # Integer found at end of line, do something with it
#             incremented_integer = int(integer) + 5
#             print(incremented_integer)



