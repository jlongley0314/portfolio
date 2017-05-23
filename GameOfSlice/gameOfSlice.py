#############################################################################################################
#############################################################################################################
##
## CS 101
## Program #2
##
## Jaremy Longley
## jlongley0314@gmail.com
##
## PROBLEM : We would like to play a game that provides the user with a random set of slices
##           and strings and they must provide the correct slice of the string.  The difficulty
##           of the slice and the length of the string will be determined by a difficulty setting provided
##           by the user (from 1-3).
## 
## ERROR HANDLING:
##      -Warn user they must have input greater than 0 for variable rounds
##      -Warn user they must enter "y, yes, n, or no" for variable run_again
##
#############################################################################################################
#############################################################################################################

# Import some modules
import random
import string

welcome = "Welcome to the GAME OF SLICE"
print("{:-^77s}".format(welcome))

# Prompt user for number of rounds and runs error handling for no-int values    
while True:
    rounds = input("\nHow many rounds would you like to run (1-20): ")
    try:
        rounds = int(rounds)
        while rounds < 1 or rounds > 20:
            rounds = input("\nPlease give me an integer from (1-20): ")
            try:
                rounds = int(rounds)
            except TypeError:
                print("\nYou didn't give me an integer")
        break
    except ValueError:
        print("\nYou didn't give me an integer")
       
# Set difficulty to user response
difficulty = input("\nHow difficult would you like the string to be? 1. Easy, 2. Medium, 3. Hard: ")

# Check for malicious difficulty input
while True:
    try:
        difficulty = int(difficulty)
        break
    except ValueError:
        difficulty = input("\nPlease enter an integer 1, 2, or 3: ")  
while difficulty < 1 or difficulty > 3:
    difficulty = int(input("\nPlease enter an integer 1, 2, or 3: "))

while True:
    # Easy difficulty
    if difficulty == 1:
        correct_answers = 0
        print("\nYour string will be easy!\n")
        while rounds > 0:
            
            # Build up the random string (5 letters)
            rand_str = ""
            for integer in range(1,6):
                rand_str += random.choice(string.ascii_letters)
                
            # Build the slice of that string
            slice_start = random.randint(0,2)
            slice_end = random.randint(3,5)       
            
            # What is the correct answer?
            correct = rand_str[slice_start:slice_end]
            
            # format the whole statement
            if slice_end == 5:
                slice_end = None

            # Check for values of None and print the slice statements
            if slice_end == None:
                sentence_beginning = "\nWhat is the slice of '".strip()
                string_slice = "'[{}::] ==> ".strip().format(slice_start)
                answer = input(sentence_beginning + rand_str + string_slice + " ")
            else:
                sentence_beginning = "\nWhat is the slice of '".strip()
                string_slice = "'[{}:{}:] ==> ".strip().format(slice_start,slice_end)
                answer = input(sentence_beginning + rand_str + string_slice + " ")

            rounds -= 1

            # Check user's answer against the correct answer
            if answer == correct:
                print("\nCorrect, the word was:", correct)
            else:
                print("\nSorry, but the correct answer was:", correct)

    # Medium Difficulty
    if difficulty == 2:
        correct_answers = 0
        print("\nYour string will be medium difficulty!\n")
        while rounds > 0:
            
            # Build up the random string (5 letters)
            rand_str = ""
            for integer in range(1,8):
                rand_str += random.choice(string.ascii_letters)
                
            # Build the slice of that string
            slice_start = random.randint(0,3)
            slice_end = random.randint(4,7)       
            
            # What is the correct answer?
            correct = rand_str[slice_start:slice_end]
            
            # format the whole statement
            if slice_end == 7:
                slice_end = None

            # Check for values of None and print the slice statements
            elif slice_end == None:
                sentence_beginning = "\nWhat is the slice of '".strip()
                string_slice = "'[{}::] ==> ".strip().format(slice_start)
                answer = input(sentence_beginning + rand_str + string_slice + " ")
            else:
                sentence_beginning = "\nWhat is the slice of '".strip()
                string_slice = "'[{}:{}:] ==> ".strip().format(slice_start,slice_end)
                answer = input(sentence_beginning + rand_str + string_slice + " ")

            rounds -= 1

            # Check user's answer against the correct answer
            if answer == correct:
                print("\nCorrect, the word was:", correct)
            else:
                print("\nSorry, but the correct answer was:", correct)

    #Hard Difficulty
    if difficulty == 3:
        print("\nYour string will be hard!\n")
        while rounds > 0:
            correct_answers = 0
            
            # Build up the random string (10 letters)
            rand_str = ""
            for integer in range(1,11):
                rand_str += random.choice(string.ascii_letters)
                
            # Build the slice of that string
            slice_start = random.randint(0,5)
            slice_end = random.randint(6,10)
            slice_step = 1

            # 25% chance slice_start is negative
            if random.randint(1,4) == 1:
                slice_start = random.randint(-10,-5)

            # 25% chance slice_end is negative
            if random.randint(1,4) == 1:
                slice_end = random.randint(-4,0)

            #25% chance slice step is reversed, if so intherchange slice_start and slice_end           
            if random.randint(1,4) == 1:
                slice_step = -1
                slice_start,slice_end = slice_end, slice_start

            #20% chance slice step is -2 or 2, if -2 interchange slice_start and slice_end
            random_number = random.randint(1,5)    
            if random_number == 1:
                slice_step = -2
                slice_start,slice_end = slice_end, slice_start
            elif random_number == 2:
                slice_step = 2

            #set slice_end, slice_start and slice_step to their default variables
            if slice_start == -10:
                slice_start = None
            elif slice_end == 10:
                slice_end = None

            # Cathc any slice errors
            if slice_start == -5 and slice_end == 6:
                slice_step == None
                                
            # What is the correct answer?
            correct = rand_str[slice_start:slice_end:slice_step]
            
            # Check for values of None and print the slice statements
            if slice_start == None:
                sentence_beginning = "\nWhat is the slice of '".strip()
                string_slice = "'[:{}:{}] ==> ".strip().format(slice_end,slice_step)
                answer = input(sentence_beginning + rand_str + string_slice + " ")
            elif slice_end == None:
                sentence_beginning = "\nWhat is the slice of '".strip()
                string_slice = "'[{}::{}] ==> ".strip().format(slice_start,slice_step)
                answer = input(sentence_beginning + rand_str + string_slice + " ")
            elif slice_end == None and slice_start == None:
                sentence_beginning = "\nWhat is the slice of '".strip()
                string_slice = "'[::{}] ==> ".strip().format(slice_step)
                answer = input(sentence_beginning + rand_str + string_slice + " ")    
            else:
                sentence_beginning = "\nWhat is the slice of '".strip()
                string_slice = "'[{}:{}:{}] ==> ".strip().format(slice_start,slice_end,slice_step)
                answer = input(sentence_beginning + rand_str + string_slice + " ")

            rounds -= 1

            #Check user's answer against the correct answer
            if answer == correct:
                print("\nCorrect, the word was:", correct, "\n")
            else:
                print("\nSorry, but the correct answer was:", correct, "\n")


    # Check to see if user wants to play again
    if rounds == 0:
        # Check to see if the user wants to run the program again
        run_again = input("Would you like to play again? ")
        
        # check for acceptable response
        if run_again.upper() in ("Y","YES","N","NO"):
            acceptable = True
        else:
            acceptable = False
            
        # malicious content checker       
        while acceptable == False:
            print("Error: please enter a valid response")
            run_again = input("\nWould you like to play again? ")
            if run_again.upper() in ("Y","YES","N","NO"):
                acceptable = True
            else:
                acceptable = False

        # if response is yes, initial variable are reset and the program restarts              
        if run_again.upper() in ("Y","YES"):
            while True:
                rounds = input("\nHow many rounds would you like to run (1-20): ")
                try:
                    rounds = int(rounds)
                    while rounds < 1 or rounds > 20:
                        rounds = input("\nPlease give me an integer from (1-20): ")
                        try:
                            rounds = int(rounds)
                        except TypeError:
                            print("\nYou didn't give me an integer")
                    break
                except ValueError:
                    print("\nYou didn't give me an integer")

        # Set difficulty to user response
            difficulty = input("\nHow difficult would you like the string to be? 1. Easy, 2. Medium, 3. Hard: ")

            while True:
                try:
                    difficulty = int(difficulty)
                    break
                except ValueError:
                    difficulty = input("\nPlease enter an integer 1, 2, or 3: ")  
            while difficulty < 1 or difficulty > 3:
                difficulty = int(input("\nPlease enter an integer 1, 2, or 3: "))
            
         # if response is no, program terminates
        elif run_again.upper() in ("N","NO"):
            print("\nThank you for playing the GAME OF SLICE.")
            break
