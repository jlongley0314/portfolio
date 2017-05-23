########################################################################
##
## Image Filters
## Jaremy Longley
## jlongley0314@gmail.com
##
## PROBLEM : Create a program that takes in a ppm file and allows the user
##          to change the picture into grayscale or vintage look.
##
## ALGORITHM : 
##  1) define function menu_option(options, valid_choices)
##     while True
##        print options
##        choice = input("Which option?")
##        if choice uppercase is in valid_choices
##            return choice
##        else
##            "bad input" -> go back to top of function loop
##
##  2) define function file_open(prompt, file_mode)
##    while True
##        try
##            in_file = open(input(prompt), file_mode)
##        except
##            Give user error message for occuring errors and repeat try except
##        lines_list = list of file lines
##        if lines_list[first line] == P3 and lines_list[second line] == 255
##            return open(in_file, file_mode)
##        elif line_list[first line] == P3 and lines_list[second line] != 255
##            warn user color depth must be 255
##        else
##            warn user that file first line should be P3
##        
##
##  3) define function grayscale(list, in_file, out_file):
##    index_value = 3
##    print(list[0], file=out_file)
##    print(list[1], file=out_file)
##    print(list[2], file=out_file)
##    while index_value <= len(list):
##        rgb_list = []
##        rgb_list.append(list[index_value])
##        rgb_list.append(list[index_value + 1])
##        rgb_list.append(list[index_value + 2])
##        grayscale_value = grayscale_calculate(rgb_list)
##        printgrayscale_value to out_file 3 times
##        index_value += 3
##    close in_file and out_file
##
##  4) define grayscale_calculate(list)
##    red = list[0]
##    green = list[1]
##    blue = list[2]
##    grayscale = 0.299 * int(red) + 0.587 * int(green) + 0.114 * int(blue)
##    return floor of grayscale
##
##  5) define function vintage(list, in_file, out_file):
##    index_value = 3
##    print(list[0], file=out_file)
##    print(list[1], file=out_file)
##    print(list[2], file=out_file)
##    while index_value <= len(list):
##        print(list[index_value], file=out_file) # red value
##        print(list[index_value + 1], file=out_file) # green value
##        print(floor of (list[index_value + 2] / 2), file=out_file) # blue value
##        index_value += 3
##    close in_file and out_file
##
##  6) define function file_write(in_file, out_file, user_choice)
##    create pixel_list = empty list
##    for line in in_file
##        pixel_list.append(clean(line))
##    if user_choice = "1"
##        grayscale(pixel_list, in_file, out_file)
##    else
##        vintage(pixel_list, in_file, out_file)
##
##  7) define clean function(line):
##	return stripped lines converted to integers
##
##
##  8) create menu
##  9) create set of choices
##
##  10) program_run = True
##  11) while program_run
##    user_choice = menu_option(menu, set of choices)
##    if user_choice == "1" or "2"
##        convert_file = file_open("File name", "r")
##        save_file = open(input("File to save to"), "w")
##        file_write(convert_file, save_file, user_choice)
##        Tell user file has been successfully saved
##
##    elif upper of user_choice == "Q":
##        program_run = False
## 
## ERROR HANDLING:
##      Warn user of bad input or bad file and force user to try again
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


import math


################
## Functions
################

def grayscale(in_file, out_file):
    
    """This function takes in a list of lines from an image file, prints the first three
    lines to an out_file and sends the RGB values through
    through a grayscale calculator and prints these to an out_file.
    This will constantly update the index of the line in order to get
    every RGB value from the in_file"""

    index_value = 3
    pixel_list = []
    for line in in_file:
        pixel_list.append(line.strip())
    # the following prints the first three lines
    # (the P3, the pixel depth, and the pixel ratio) to the out_file
    print(pixel_list[0], file=out_file)
    print(pixel_list[1], file=out_file)
    print(pixel_list[2], file=out_file)
    while index_value < len(pixel_list):
        rgb_list = []
        rgb_list.append(pixel_list[index_value])                          # get red value, append to empty list
        rgb_list.append(pixel_list[index_value + 1])                      # get green value, append to empty list
        rgb_list.append(pixel_list[index_value + 2])                      # get blue value, append to empty list
        grayscale_value = grayscale_calculate(rgb_list)
        # print the grayscale value to the out_file 3 times (once for eachrgb value)
        print(grayscale_value, file=out_file)
        print(grayscale_value, file=out_file)
        print(grayscale_value, file=out_file)
        index_value += 3
    in_file.close()
    out_file.close()


def grayscale_calculate(original_list):
    
    """Take in the original lists values at index 0, 1, and 2 (red, green, and blue values)
        and convert them into their grayscale values 0.299 * red + 0.587 * green + 0.114 * blue
        returns the grayscale value as the new value for red, green, and blue"""
    
    grayscale = 0.299 * int(original_list[0]) + 0.587 * int(original_list[1]) + 0.114 * int(original_list[2])
    return math.floor(grayscale)


def vintage(in_file, out_file):
    
    """Takes in a list, prints the first three values (the P3, the pixel depth and the pixel ratio)
       to the out_file, then prints every red and green value as is, and prints every blue value
       divided by 2 (for vintage look)"""

    index_value = 3
    pixel_list = []
    for line in in_file:
        pixel_list.append(line.strip())
    # the following prints the first three lines
    # (the P3, the pixel depth, and the pixel ratio) to the out_file
    print(pixel_list[0], file=out_file)
    print(pixel_list[1], file=out_file)
    print(pixel_list[2], file=out_file)
    while index_value < len(pixel_list):
        new_blue = math.floor(int(pixel_list[index_value + 2]) / 2)       # new blue value = old blue / 2
        print(pixel_list[index_value], file=out_file)                     # red value (stays the same)
        print(pixel_list[index_value + 1], file=out_file)                 # green value (stays the same)
        print(new_blue,file=out_file)
        index_value += 3
    in_file.close()
    out_file.close()


def file_open(prompt, file_mode):
    
    """Takes in the user-prompted file they wish to send through a filter and the read-only file mode,
       and runs the file through a try-except loop to make sure the file exists.  If the file exists,
       the function reads through the first two lines to make sure line 1 is "P3" and line 2 reads "255".
       If the file does not exist or the first two lines don't match, warn user and force to enter new file."""
    
    while True:
        try:
            verify = True
            while verify:
                user_input = input(prompt)
                input_file = open(user_input)
                verify = file_verify(input_file)
            return open(user_input, "r")
        except FileNotFoundError:
            print("ERROR: File not found. Please enter a valid file name.")
        except IOError:
            print("ERROR: General IOError. Please enter a valid file name.")

def file_verify(input_file):
    file_list = input_file.readlines()
    if file_list[0] != "P3\n":
        print("First line must read P3.")
        input_file.close()
        return True
    elif file_list[2] != "255\n":
        print("Third line must read 255.")
        input_file.close()
        return True
    else:
        return False

def menu_option(options, valid_choices):

    """This function takes in user input for menu item and checks for it within the valid_choices"""

    while True:
        print(menu)
        choice = input("==> ")
        if choice.upper() in valid_choices:
            return choice
        else:
            print("\nYou must enter a valid option (1, 2, or Q)")



##############
## Main Body
##############    

# available menu options            
menu = """                                                  

    Image Filters

1. Convert Image to GrayScale
2. Convert Image to Vintage
Q. Quit

"""

valid_choices = ["1", "2", "Q"]

program_run = True                                                  # sentinel to keep user in loop until program is completed

while program_run:

    user_choice = menu_option(menu, valid_choices)                  # validate user_choice
    
    if user_choice == "1" or user_choice == "2":
        convert_file = file_open("Enter a file you want to convert ==> ", "r") # validate file entered
        save_file = open(input("Enter the file you would like to save to ==> "), "w")
        if user_choice == "1":
            grayscale(convert_file, save_file)                      # send file through grayscale function
            print("\nYour file has been successfully saved.\n")
        else:
            vintage(convert_file, save_file)                        # send file through vintage function
            print("\nYour file has been successfully saved.\n")
    elif user_choice.upper() == "Q":
        print("\nProgram Terminated")
        program_run = False
        





        





