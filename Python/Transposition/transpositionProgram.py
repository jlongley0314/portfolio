########################################################################
##
## CS 101
## Program # 4
## Jaremy Longley
## jlongley0314@gmail.com
##
## PROBLEM : Your program will transpose and un­transpose lines from a file another file. The names of the
## file will be given by the user.
##
## ALGORITHM : 
##      1. Define an encode function
##      2. Define a decode function
##      3. Define a file-handling function
##      4. Define an error_handling function
##      5. Set run_program to True
##        7) While run_program        
##
##             a) Print menu labeled under transposition options, menu options include:
##                      I) 1. Encipher File
##                      II) 2. Decipher File
##                      III) Q. Quit
##
##             b) Prompt user for input of what option they wish to choose:
##                      I) run the user input through the error_handling function defined on line 5
##
##             c) If 1 is chosen:
##                      I) prompt user for file they would like to encipher:
##                              A) run the file name through the file_handling function from line 4
##                      II) prompt user for file they would like to write to
##                      III) run through the encipher function from line 2
##                      IV) give menu options again
##
##              d) If 2 is chosen:
##                      I) prompt user for file they would like to decode:
##                              A) run the file name through the file_handling function from line 4
##                      II) prompt user for the file they would like to write to
##                      III) run through the decipher function from line 3
##                      IV) give menu options again
##
##              c) If Q is chosen:
##                      I) terminate program
## 
## ERROR HANDLING:
##      Check that the user-entered file exists
##      When user is selecting from menu option, user can only choose 1, 2, or Q
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import math


#######################
##  Functions
#######################


# Encode Function
def transpose_string(original_string):
    """Take in a string from the user, transpose the string and return the transposed string"""
    original_string = original_string.strip()

    # Initialize useful variables
    even_index = ""
    odd_index = ""
    index = 0
    
    for char in original_string:
        # If the index of the character is odd
        if index % 2 == 1:
            odd_index += char
        # If the index of the character is even
        else:
            even_index += char
        index += 1
        
    # Concatenate even_index to odd_index, house in a new string    
    encoded_string = even_index + odd_index
    return encoded_string

# Decode Function
def decode_string(original_string):
    original_string = original_string.strip("\n")
    index = 0                                               # start at 0 index
    count = 0
    decoded_string = ""                                     # house the decoded string
    half_len_string = math.ceil((len(original_string)/2))   # determine the floor of half
                                                            # this will determine which characters were origianlly
                                                            # at odd indexes and which were at even indexes

    # Run if the total count is less than the length of the original string
    # Stop once the string runs out of characters to decode
    while count != len(original_string):
        if index < half_len_string:                         # checks the first half of the string    
            decoded_string += original_string[index]        # adds the letter at the index to the decoded string
            index += (half_len_string)                      # this will update the index to the next value
                                                            # to add to the decoded string, since all odd indexes
                                                            # from original string were moved to the end
                                                            # (which the end is now after half of the encoded string)
        else:
            decoded_string += original_string[index]        # add the letter at the index to the decoded string
            index -= (half_len_string - 1)                  # this will update the index to the next value
                                                            # to add to the decoded string
        count += 1

    return decoded_string

# Error-handling function
def error_handling(user_input):
    """checks for malicious content entered from user"""
    if menu_input.upper() not in ["1", "2", "Q"]:           # Checks for valid menu input within the options provided
        print("\nERROR: Please enter 1, 2, or Q")

# File_handling
def file_handling(menu_input):
    while True:
        if menu_input.upper() not in ["1", "2", "Q"]:       # Checks for valid menu input within the options provided
            menu_input = input("\nERROR: Please enter 1, 2, or Q: ")
        else:
            break
    
##########################
##  Main Program Body   
##########################


run_program = True                                          # Sentinel variable will run until not true

while run_program:
    
    # Print Menu options
    print("""
     Transposition Option:

    1. Encode File
    2. Decode File
    Q. Quit
    
          """)

    menu_input = input("What would you like to do? ")
    user_input = file_handling(menu_input)

    # Encode File
    if menu_input == "1":
        
        in_file = input("Enter a file to encode: ")         # Prompt user for file to read
        read_file = file_handling(in_file)                  # and run through file_handling() function

        output = input("File to write to: ")                      
        write_file = open(output, "w")                      # Get file to write encoded strings to

        for line in read_file:
            encoded_string = transpose_string(line)         # Get string to encode and run it through the
                                                            # encode_string function
            print(encoded_string, file=write_file)          # write the encoded_string to the output file
            
        print("File has been encoded.")
        read_file.close()
        write_file.close()


    # Decode File
    elif menu_input == "2":

        in_file = input("Enter a file to decode: ")         # Prompt user for file to read
        read_file = file_handling(in_file)                  # and run through file_handling() function

        output = input("File to write to: ")                # File to write decoded strings to
        write_file = open(output, "w")

        for original_string in read_file:
            new_string = decode_string(original_string)     # Run lines from file through the
                                                            # decode_string() function
            print(new_string, file=write_file)              # write the decoded strings to the output file

        print("File has been decoded.")
        read_file.close()
        write_file.close()

    else:                                                   # Quit program
        run_program = False
            

            







    
    
        
