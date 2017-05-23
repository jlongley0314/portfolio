#############################################################################################################
#############################################################################################################
##
## CS 101
## Program #2
##
## Jaremy Longley
## jlongley0314@gmail.com
##
## PROBLEM : In this assignment we’ll track luggage through an airline from Kansas City, (MCI) to Honolulu
## (HNL).
##
## ALGORITHM : 
##      1. Create variable rounds
##      2. Check if rounds > 0
##      3. while rounds > 0, run loop to check for probability of luggage destination
##      4. Print out probability and ask user if they would like to run again
## 
## ERROR HANDLING:
##      -Warn user they must have input greater than 0 for variable rounds
##      -Warn user they must enter "y, yes, n, or no" for variable run_again
##
#############################################################################################################
#############################################################################################################


import random

# checking the total number of rounds the user would like to run
rounds = int(input("How many rounds do you want to run: "))

# check if the user wants the full details run, this will be used later (ln 149)
outputDetails = input("\nDo you want to output details Y//YES//N//NO: ")
# check for acceptable response
if outputDetails.upper() in ("Y","YES","N","NO"):
    acceptable = True
else:
    acceptable = False
# malicious content checker       
while acceptable == False:
    print("\nError: please enter a valid response")
    outputDetails = input("\nDo you want to output details Y//YES//N//NO: ")
    if outputDetails.upper() in ("Y","YES","N","NO"):
        acceptable = True
    else:
        acceptable = False

# checking for malicious input
while rounds < 1:
    print("Please enter an integer greater than 0")
    rounds = int(input("How many rounds do you want to run in order to check the probability of your luggage \
being on time: \n"))

# Initializing total_rounds (the total number of rounds run),
# destination (the airport the luggage travels through),
# luggage being on time (whether the hops are <= 2),
# and the maximum hops that occur
total_rounds = 0
destination = "MCI -> "
on_time = 0
max_hops = 0

# This block of code will run as long as the luggage is not in HNL
while destination != "HNL": 
    hops = 0 
    randomNumber = random.randint(1,100)
    # sets destination back to MCI every time loop runs
    destination = "MCI -> "                    
    detailed_list = "MCI -> "
    while rounds > 0:

        # initialize hops (check how many airports luggage travels through)
        # and detailed_list (visualize the order of luggage for the user)
        if destination == "MCI -> ":
            randomNumber = random.randint(1,100)
            # check to see if luggage hops to LVS
            if randomNumber <= 40:     
                hops += 1
                destination = "LVS -> "
                detailed_list += destination
            # check if luggage hops to SEA                
            elif randomNumber <= 70:   
                hops += 1
                destination = "SEA -> "
                detailed_list += destination
            # luggage hops to HNL    
            else:                               
                hops += 1
                destination = "HNL"
                detailed_list += destination

        # if luggage travels to LVS               
        while destination == "LVS -> ":
            randomNumber = random.randint(1,100)
            # luggage hops back to MCI
            if randomNumber <= 30:      
                hops += 1
                destination = "MCI -> "
                detailed_list += destination
            # luggage hops to SEA               
            elif randomNumber <= 80:    
                hops += 1
                destination = "SEA -> "
                detailed_list += destination
            # luggage in HNL               
            else:                                
                hops += 1
                destination = "HNL"
                detailed_list += destination

        # if luggage travels to SEA
        while destination == "SEA -> ":
            randomNumber = random.randint(1,100)
            # luggage back to MCI
            if randomNumber <= 1:      
                hops += 1
                destination = "MCI -> "
                detailed_list += destination
            # luggage back to LVS               
            elif randomNumber<= 70: 
                hops += 1
                destination = "LVS -> "
                detailed_list += destination
            # luggage to HNL
            else:                                
                hops += 1
                destination = "HNL"
                detailed_list += destination

        # if luggage travels to HNL (our desired destination)
        if destination == "HNL" and rounds >= 1:
            rounds -= 1
            total_rounds += 1
            # check to see if HNL is the second airport the luggage traveled to,
            # this means luggage was on time
            if hops <= 2:   
                on_time += 1
            if hops > max_hops:
                max_hops = hops
            # utilize the output details checker from ln 44   
            if outputDetails.upper() in ("Y","YES"):
                print("Trial",total_rounds,":  ",detailed_list)    
            # reset destination and hops to initial values so the luggage tracker can be restarted
            destination = "MCI -> "
            hops = 0
            detailed_list = destination

    # When luggage finally arrives at HNL, we will check the
    # probability of the luggage being on time and we will run
    # a few statements telling the user the total number of trials run
    # and the total number of times luggage was on time
    probability_on_time = (on_time/total_rounds) * 100      
    print("\nThe luggage was on time to HNL", probability_on_time, "% of the time.")
    print("\nThe max hops that occured was", max_hops,"hops.")
    print("\nThe total number of times luggage was on time", on_time, "time(s).")
    print("\nThere was a total of", total_rounds,"trial(s) run.")

    # Check to see if the user wants to run the program again
    run_again = input("\nWould you like to run the program again? ")
    
    # check for acceptable response
    if run_again.upper() in ("Y","YES","N","NO"):
        acceptable = True
    else:
        acceptable = False
    # malicious content checker       
    while acceptable == False:
        print("Error: please enter a valid response")
        run_again = input("\nWould you like to run the program again? ")
        if run_again.upper() in ("Y","YES","N","NO"):
            acceptable = True
        else:
            acceptable = False

    # if response is yes, initial variable are reset and the program restarts              
    if run_again.upper() in ("Y","YES"):
        rounds = int(input("\nHow many rounds do you want to run in order to check the probability of your luggage \
being on time: "))
        while rounds < 1:
            print("Please enter an integer greater than 0")
            rounds = int(input("\nHow many rounds do you want to run in order to check the probability of your luggage \
being on time: "))
        destination = "MCI -> "
        on_time = 0
        total_rounds = 0
        # check if the user wants the full details run, this will be used later (ln 149)
        outputDetails = input("\nDo you want to output details Y//YES//N//NO: ")
        # check for acceptable response
        if outputDetails.upper() in ("Y","YES","N","NO"):
            acceptable = True
        else:
            acceptable = False
        # malicious content checker       
        while acceptable == False:
            print("\nError: please enter a valid response")
            outputDetails = input("\nDo you want to output details Y//YES//N//NO: ")
            if outputDetails.upper() in ("Y","YES","N","NO"):
                acceptable = True
            else:
                acceptable = False
        continue
    # if response is no, program terminates
    elif run_again.upper() in ("N","NO"):
        print("\nThank you for using the luggage simulator. Have a nice flight!")
        break
   


        
        
            
                
                    
                    
                
        
        
        
    
