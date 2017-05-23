########################################################################
##
## Movie Review Sentiment Analysis
## Jaremy Longley
## jlongley0314@gmail.com
##
## PROBLEM : Read through a movie review file and a wordlist (provided by user)
##          and be able to find the score for each word based on the review
##          rating in order to analyse the sentiment behind the word.
##
## ALGORITHM :
##
# MENU_1 = “””
# 			Python Sentiment Analysis
#
# 	1. Get sentiment…
# 	Q. Quit
#
# ”””
#
# MENU_2 = “””
# 		Sort Options
# 	1. Sort by Avg Ascending
# 	2. Sort by Avg Descending
# 	3. Sort by Standard Deviation Ascending
# 	4. Sort by Standard Deviation Descending
#
# ”””
#
#
# define average_scores(takes in a dictionary)
#
#     	"takes in a dictionary of words and scores and averages
#     	the list of scores, makes sure to round the average"
#
# 	word_average_dict = empty dict
#
# 	for every value of the key, value pair from the dictionary
# 		word_score_list = value of the key,value pair (the scores) from dictionary param
# 		avg_score = sum of word_score_list values / length of
# 				word_score_list(number of elements)
# 		set the word as the key in the word_average_dict
# 		and the avg_score as that value
#
# 	return word_average_dict
#
#
# define standard_deviation(takes in two dictionaries)
#
#     	"takes in word_average_dict and word_and_score dictionary
# 	and computes the standard deviation of the words from the averages
# 	and all the scores they’ve been given”
#
# 	std_dev_dict = empty dict
#
# 	for word in word_and_score dict keys
# 		std_dev_list = empty list
# 		word_score_list = value of the key,value pair (the scores)
# 				from word_and_score dictionary
# 		if word in word_average_dictionary
# 			average_score = value of the key, value pair
# 				(the average) from the word_average_dict
# 		for score in word_score_list
# 			append (score - average_score)^2 to std_dev_list
#
# 		std_dev = sum all values from std_dev_list and divide by number of elements
# 		add the word to the std_dev_dict as the key and
# 		the std_dev as the value of that key
#
#     	return std_dev_dict
#
#
# define correct_input function (takes in a prompt, list)
#
#     	"takes in a prompt asking the user what he or she would like to do
#     	and then checks to see if the user input is in the list of values provided,
# 	if malicious input is entered, the function continues to ask the user for input"
#
# 	while True
#
# 		user_input = users input from the prompt param
#
# 		if user_input is in list
# 			return user_input
#
#
# define read_wordlist function(takes in a prompt)
#
#     "takes in a prompt asking user what file with words to score
#     they would like to open, checks for the file entered and either sends the open
#      file off to the file_to_set function or (if an error occurs)
#      continues to ask the user for a file to open,
#      eventually returning the set of words from the wordlist"
#
#     while True
#         word_list_file = input(prompt)
#         try opening the user input file
#             wordlist_set = file_to_set(word_list_file)
# 	     close wordlist_file
#
#             return the wordlist set
#
#         except FileNotFoundError
#             warn user to enter a correct filename, and return to the top
#
#
# define wordlist_to_set function(takes in an input_file)
#
#     "takes in the opened word_list file and converts the lines of the file to
#     an easily passed around set of the all the words, returns this set"
#
#     wordlist_file = input_file
#     create an empty set
#
#     for line in wordlist_file
#         clean line
#         add line to empty set
#
#     return the wordlist_set
#
#
# define read_through_reviews function(takes in no value for the param)
#
#     "reads through the rotten tomatoes reviews and creates a dictionary of the lines,
#     returns the dictionary of the rotten tomatoes reviews, closes the file"
#
#     open movie_review_file
#     read through the file and create a list of all the lines
#     create an empty movie_review dictionary
#
#     for each element in the list
#         split the element and add the number at index 0 (the score) as the
#         dictionary key with the rest of the element as the dictionary value
#
#     close movie_review_file
#     return the movie_review_dictionary
#
#
# define create_word_score_dict function(takes in a set,
#                        and a dictionary)
#
#     "for every word in the wordlist set, checks for that word against the
#     movie_review dictionary values.  When a match is found, it adds
#     the dictionaries key (the movies score) to another dictionary of all the words
#     and their associated reviews"
#
#     word_and_score_dictionary = empty dictionary
#
#     for word in wordlist_set
#         for word in movie_review dictionary values
# 		if word in movie_review dictionary == word in wordlist_set
# 			the key from the movie_review dictionary (the score itself)
# 			is appended to a list of the scores as the dict value
# 			and the word becomes the key
#
#     return word_and_score_dictionary
#
#
# define create_display_dictionary(takes in 3 dictionaries)
#
# 	“Takes in the average score dict, the standard deviation dict
# 	and the words_and_scores dict creates a dict where the word
# 	is the key, the number of occurrences (length of value
# 	from words_and_scores dict key,value pair) is the first index of the value,
# 	the avg score of that word is the second index of the value ,
# 	and the standard deviation of that word  is the final index of the value”
#
# 	initialize display_dict to an empty dictionary
#
# 	for word in key of words_and_scores dict
# 		total_occurences = length of that words value(total occurrences of that word)
#
# 		for word in key of average_score dict
# 			if word in average_score dict == word in words_and_scores
# 				avg_score = that words value
#
# 		for word in key of std_deviation dict
# 			if word in std_deviation dict == word in words_and_scores
# 				std_deviation = that words value
#
# 		dispaly_tup = tuple of that words occurrence, avg_score and std_deviation
#
# 		set the the word to the key of display_dict and set that key’s
# 			value to the display_tup
#
# 	return display_dict
#
#
# define results_avg_ascending function(takes in dictionary)
#
# 	“Takes in display dictionary, iff the user wants the results output
# 	as the average score ascending this function outputs that”
#
# 	Display a nicely formatted table of the Word(key), Occurrence(value index 0),
# 	Avg Score(value index 1), and Stand Dev(value index 2),
# 	with the words ascending by the average score
#
#
# define results_avg_descending function(takes in dictionary)
#
# 	“Takes in display dictionary, if the user wants the results output as the average score
# 	descending this function outputs that”
#
# 	Display a nicely formatted table of the Word(key), Occurrence(value index 0),
# 	Avg Score(value index 1), and Stand Dev(value index 2),
# 	with the words descending by the average score
#
#
# define results_stand_dev_ascending function(takes in dictionary)
#
# 	“Takes in display dict, if the user wants the results output as the
# 	stand deviation ascending this function outputs that”
#
# 	Display a nicely formatted table of the Word(key), Occurrence(value index 0),
# 	Avg Score(value index 1), and Stand Dev(value index 2),
# 	with the words ascending by the Std Dev
#
#
# define results_stand_dev_descending function(takes in dictionary)
#
# 	“Takes in display dict, if the user wants the results output
# 	as the stand deviation descending this function outputs that”
#
# 	Display a nicely formatted table of the Word(key), Occurrence(value index 0),
# 	Avg Score(value index 1), and Stand Dev(value index 2),
# 	with the words descending by the Std Dev
#
#
#
# program_run = True
#
# while program_run
#
# 	print(MENU_1)
#
# 	review_dict = read_through_reviews(no param)
# 	menu_1_input = correct_input(“What would you like to do”, [“1”, “Q”])
#
# 	if menu_1_input uppercased == “Q”:
# 		program_run = False
#
# 	wordlist_set = read_wordlist(“Enter the name of a file with words to score”)
# 	word_score_dict = create_word_score_dict function(wordlist_set, review_dict)
# 	avg_dict = average_scores(review_dict)
# 	std_dev_dict = standard_deviation(avg_dict, word_score_dict)
# 	display_dict = create_display_dictionary(word_score_dict, avg_dict, std_dev_dict)
#
# 	print(MENU_2)
# 	menu_2_input = correct_input(“Choose an option”, [“1”, “2”, “3”, “4”])
#
# 	if menu_2_input == “1”
# 		results_avg_ascending(display_dict)
## 	elif menu_2_input == “2”
## 		results_avg_descending(display_dict)
## 	elif menu_2_input == “3”
## 		results_stand_dev_ascending(display_dict)
## 	else
## 		results_stand_dev_descending(display_dict)
##
##
## ERROR HANDLING:
##      Any malicious data given, warn user and force them to use data
##      that fits with the program.
##
##
########################################################################


##############
## Menus
##############


MENU_1 = """

                    Python Sentiment Analysis

        1. Analyze sentiment for words in a file
        Q. Quit

"""

MENU_2 = """

                    Sort Options
        1. Sort by Average Ascending
        2. Sort by Average Descending
        3. Sort by Standard Deviation Ascending
        4. Sort by Standard Deviation Descending

"""

DISP_MENU = """

Word               Occurence    Avg Score      Std Dev
------------------------------------------------------
"""


#############
## Functions
#############


def read_reviews():

    """Takes in no params, reads through the rotten tomatoes reviews and creates a list of the lines,
    returns the list of the rotten tomatoes reviews, closes the file"""

    review_file = open("movieReviews.txt", "r")
    review_lst = review_file.readlines()                    # Create list of lines from the review
    review_file.close()

    return review_lst



def correct_input(prompt, list):

    """takes in a prompt asking the user what he or she would like to do
    	and then checks to see if the user input is in the list of values provided,
	if malicious input is entered, the function continues to ask the user for input"""

    while True:

        user_input = input(prompt)                          # Passes in a prompt to ask user

        if user_input.upper() in list:                        # Search for valid input from user
            return user_input

        else:
            print("Please enter correct input")


def read_wordlst(prompt):

    """takes in a prompt asking user what file with words to score
    they would like to open, checks for the file entered and either sends the open
    file off to the file_to_set function or (if an error occurs)
    continues to ask the user for a file to open,
    eventually returning the set of words from the wordlist"""

    while True:                                             # Loop through until correct input received

        try:
            wordlist_file = open(input(prompt), "r")        # gets file from user input
            word_set = set()                                # make empty set to store words from users wordlist file
            for line in wordlist_file:
                line = line.strip()
                word_set.add(line)                          # Builds up set word-by-word
            wordlist_file.close()

            return word_set

        except FileNotFoundError:
            print("File Not Found")


def create_word_score_dict(word_set, review_lst):

    """for every word in the wordlist set, checks for that word in the review_lst.
    When a match is found, it adds the list index[0] (the movies score) to a
    dictionary of all the words and their associated reviews"""

    word_score_dict = {}

    for word in word_set:                                   # Iterate through words from the set
        word_score_dict[word] = []                          # Sets the word as the key
        for review in review_lst:
            if word in review:                              # Checks for the word in the review
                word_score_dict[word].append(int(review[0]))     # Appends the score to the words value

    return word_score_dict



def create_avg_dict(word_score_dict):

    """Takes in the dicitonary of words and scores and averages
    the list of scores"""

    avg_dict = {}                                           # Will contain words as keys and the average as the value

    for key, value in word_score_dict.items():
        score_lst = value
        avg = sum(score_lst) / len(score_lst)               # Creates the average of each score from the dict values
        avg_dict[key] = avg                                 # Update new dictioanry with the word and average pair

    return avg_dict


def create_std_dev_dict(word_score_dict, avg_dict):

    """takes in word_average_dict and word_and_score dictionary
	and computes the standard deviation of the words from the averages
	and all the scores they’ve been given"""

    std_dev_dict = {}

    for word in word_score_dict.keys():                     # Takes word in the dictionary of words and scores
        scores_lst = word_score_dict[word]

        for word_2 in avg_dict.keys():                      # Takes word from the keys of the acerage score dictionary
            if word_2 == word:                              # Checks if the two words are equal (runs back through if not)
                avg = avg_dict[word]                        # The value of the dict is the average, sets this variable
                std_dev_lst = []

            for score in scores_lst:                        # Iterates through the scores in the list of all scores
                std_dev_lst.append((score - avg) ** 2)      # Computes the first part of the standard deviation,
                                                            # creates a list of these values

            std_dev = sum(std_dev_lst) / len(std_dev_lst) # finishes standard dev computation
            std_dev_dict[word] = std_dev                # sets the word to the key of the std_dev dict with the
                                                            # std dev as the value

    return std_dev_dict





def build_display_dict(word_score_dict, avg_dict, std_dev_dict):

    """Takes in the average score dict, the standard deviation dict
	and the words_and_scores dict creates a dict where the word
	is the key, the number of occurrences (length of value
	from words_and_scores dict key,value pair) is the first index of the value,
	the avg score of that word is the second index of the value ,
	and the standard deviation of that word  is the final index of the value"""

    display_dict = {}

    for word in word_score_dict.keys():
        total_occurences = len(word_score_dict[word])       # total occurences of a certain word in the review

        for word_2 in avg_dict.keys():
            if word_2 == word:                              # word from avg_dict is the same
                avg_score = avg_dict[word_2]                # word from the word_score_dict

        for word_3 in std_dev_dict.keys():
            if word_3 == word:                              # word from std_dev_dict is the same
                std_dev = std_dev_dict[word_3]              # word from the word_score dict

        display_tup = (total_occurences, avg_score, std_dev) # create a tuple with the occurences, avg,
                                                             # and std dev

        display_dict[word] = display_tup                    # build up dictionary with word as key
                                                            # and display_tup as the value
    return display_dict



def disp_results_avg_asc(display_dict):

    """Takes in display dictionary, iff the user wants the results output
	as the average score ascending this function outputs that, return nothing"""

    # Create list of display values sorted by averages in ascending order
    avg_asc_lst = sorted(display_dict.values(), \
                        key = lambda value: value[1])

    # Iterate through avg_asc_lst
    for tup in avg_asc_lst:
        for word in display_dict.keys():
            # if the tuple at the index of the list is equal to the tuple value of the display dict
            if display_dict[word] == tup:
                # Print well displayed table
                print("{:<15} {:>12} {:>12.4f} {:>12.4f}"\
                     .format(word, tup[0], tup[1], tup[2]))


def disp_results_avg_desc(display_dict):

    """Takes in display dictionary, if the user wants the results output as the average score
	descending this function outputs that, returns nothing"""

    # Create list of display values sorted by averages in descending order
    avg_desc_lst = sorted(display_dict.values(), \
                         key = lambda value: value[1], \
                         reverse = True)

    # Iterate through avg_desc_lst
    for tup in avg_desc_lst:
        for word in display_dict.keys():
            # if the tuple at the index of the list is
            # equal to the tuple value of the display dict
            if display_dict[word] == tup:
                # Print well displayed table
                print("{:<15} {:>12} {:>12.4f} {:>12.4f}" \
                      .format(word, tup[0], tup[1], tup[2]))


def disp_results_std_asc(display_dict):

    """Takes in display dict, if the user wants the results output as the
	stand deviation ascending this function outputs that, returns nothing"""

    # Create list of display values sorted by std dev in ascending order
    std_asc_lst = sorted(display_dict.values(), \
                         key=lambda value: value[2])

    # Iterate through std_asc_lst
    for tup in std_asc_lst:
        for word in display_dict.keys():
            # if the tuple at the index of the list is
            # equal to the tuple value of the display dict
            if display_dict[word] == tup:
                # Print well displayed table
                print("{:<15} {:>12} {:>12.4f} {:>12.4f}" \
                      .format(word, tup[0], tup[1], tup[2]))


def disp_results_std_desc(display_dict):

    """Takes in display dict, if the user wants the results output
	as the stand deviation descending this function outputs that, returns nothing"""

    # Create list of display values sorted by std dev in desc order
    std_desc_lst = sorted(display_dict.values(), \
                         key=lambda value: value[2], \
                          reverse = True)

    # Iterate through std_desc_lst
    for tup in std_desc_lst:
        for word in display_dict.keys():
            # if the tuple at the index of the list is
            # equal to the tuple value of the display dict
            if display_dict[word] == tup:
                # Print well displayed table
                print("{:<15} {:>12} {:>12.4f} {:>12.4f}" \
                      .format(word, tup[0], tup[1], tup[2]))

################
## MAIN PROGRAM
################


program_run = True

while program_run:

    print(MENU_1)

    review_dict = read_reviews()
    menu_1_input = correct_input("==> ", ["1", "Q"])

    if menu_1_input.upper() == "Q":                         # Terminate program (I'll be back)
        break

    word_set = read_wordlst("Enter the name of a file with words to score ==> ")
    word_score_dict = create_word_score_dict(word_set, review_dict)
    avg_dict = create_avg_dict(word_score_dict)
    std_dev_dict = create_std_dev_dict(word_score_dict, avg_dict)
    display_dict = build_display_dict(word_score_dict, avg_dict, std_dev_dict)

    print(MENU_2)
    menu_2_input = correct_input("==> ", ["1", "2", "3", "4"])

    print(DISP_MENU)

    if menu_2_input == "1":
        disp_results_avg_asc(display_dict)

    elif menu_2_input == "2":
        disp_results_avg_desc(display_dict)

    elif menu_2_input == "3":
        disp_results_std_asc(display_dict)

    else:
        disp_results_std_desc(display_dict)


