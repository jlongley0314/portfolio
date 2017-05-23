########################################################################
##
## Stock Price Analysis
## Jaremy Longley
## jlongley0314@gmail.com
##
## PROBLEM : This program will take in information from a user about dates they bought
##          and sold stock, iterate through a stock file, and output a portfolio detailing
##          bought price, sold price, money made, etc.
##
## ALGORITHM :
# define function convert_to_stocklist()
#     stock_list = []
#     company_list = []
#     convert_file = open("stocklist.csv", "r")
#     for line_str in convert_file
#         line_str = line_str.strip()
#         stock, company = line_str split on the (",")
#         append stock to stock_list
#         append comany to company_list
#     remove index 0 and 1 (since they just say "Stock" and "Name")
#     return stock_list, company_list
#
# define function correct_input(prompt, stock_list)
#     while True
#         user_input = input(prompt)
#         if user_input.upper in stock_list or user_input.upper == "QUIT"
#             return user_input
#         else
#             print("Could not find the stock ", user_input,".")
#
# define function correct_date(prompt)
#     while True
#         date_input = input(prompt)
#         try
#             validate_input = validate date_input (convert to datetime usage)
#             return date_input
#         except ValueError (datetime validation should throw a value error if malicious input is entered)
#             print warning
#
# define valid_date_span(purchase_date, sale_date)
#     if purchase_date < sale_date (convert to datetime usage)
#         warn user sale date is greater than purchase date
#         return True
#     else
#         return False
#
# define valid_shares(prompt)
#     while True
#         try
#             shares_number = int(input(prompt))
#             if stock_number <= 0:
#                 warn user value must be greater than 0
#             else
#                 return shares_number
#         except ValueError
#             warn user value must be integer greater than 0
#
# define stock_portfolio(stock_name, bought_date, sold_date, shares, company_name)
#     stock_file = open_stock_file(stock_name)
#
#     Check if bought_date not in stock_file and sold_date not in stock_file
# 	print(“Could not locate the start date of ”, bought_date)
# 	print(“Could not locate the end date of ”, sold_date)
#        return (does not give a return value so it exits function)
#     elif just bought_date not in stock_file
# 	print(“Could not locate the start date of ”, bought_date)
# 	return (does not give a return value so it exits function)
#     elif just sold_date not in stock_file
# 	print(“Could not locate the end date of ”, sold_date)
#        return (does not give a return value so it exits function)
#     else both bought and sold_date are in stock_file
# 	total_shares = split_ratio_calculate(stock_file, shares, bought_date, sold_date)
# 	total_price, bought_price, sold_price = total_price_calculate(stock_file, bought_date, sold_date, shares, total_shares)
#     	print("Our", company_name, "(" + stock_name + ") Portfolio")
# 	print the nicely formatted output of the bought and sold date, share number, price and total price
# 	stock_file.close()
#
# define open_stock_file(stock_name)
#     file_name = stock_name.upper() + ".csv"
#     return open(file_name, “r”)
#
# define make_company_name(stock_name, stock_list, company_list)
#     for stock_name.upper in stock_list
#         index = stock_list.index()
#         company_name = company_list[index]
#         return company_name
#
# define split_ratio_calculate(in_file, shares, bought_date, sold_date)
#     shares_total = shares
#
#     for line_str in in_file
# 	date,open,high,low,close,volume,ex_dividend,split_ratio = line_str split on (“,”)
# 	if date >= bought_date and date <= sold_date
# 		shares_total *= split_ratio
# 	else
# 		continue
#     return shares_total
#
# define total_price_calculate(in_file, bought_date, sold_date, shares, ending_shares)
#     for line_str in in_file
# 	date,open,high,low,close,volume,ex_dividend,split_ratio = line_str split on (“,”)
# 	if date == bought_date
# 		start_price = open * shares
#         elif date == start_date
# 		end_price = close * ending_shares
#     total_price = end_price - start_price
#     return total_price, start_price, end_price
#
# program_run = True
# while program_run
#     stock_list, company_list = convert_to_stocklist()
#     stock_input = correct_input("Enter the name of the stock purchased. Enter quit to exit")
#     company_name = make_company_name(stock_input, stock_list, company_list)
#
#     if stock_input.upper() == "QUIT"
#         program_run = False
#     else
#         purchase_date = correct_date("Enter the stock purchase date")
#         sale_date = correct_date("Enter the date you sold the stock")
#         date_span = valid_date_span(purchase_date, sale_date)
#         if date_span == True
#             break
#         else
#             continue
#         shares_number = valid_shares("How many shares were purchased")
#         stock_portfolio(stock_input, purchase_date, sale_date, shares_number, company_name)
##
## ERROR HANDLING:
##      If any unusable input is enteres (for example a string when an integer should be entered)
##      I will ask the user to enter the correct information and continue asking until correct
##      information is entered
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#############
## Modules
#############


import datetime


#############
## Functions
#############


def convert_to_stocklist():

    """This function doesn't take in a value, but it converts the stock_list.csv file
    into a usable list of the stock names and the company name associated with that
    stock name"""

    stocklist_file = open("stocklist.csv", "r")

    stock_list = []
    name_list = []
    for line in stocklist_file:
        line = line.strip()
        if "Stock" in line:                                             # skip the first line
            continue
        line_list = line.split(",")
        stock_list.append(line_list[0])                                 # create one list for the stock names
        name_list.append(line_list[1])                                  # create one list for the company name
    stocklist_file.close()
    return stock_list, name_list


def correct_input(prompt, stock_list):

    """This function checks for the stock given by the user in the stock_list."""

    while True:
        user_input = input(prompt)
        if user_input.upper() in stock_list or user_input.upper() == "QUIT":
            return user_input
        else:
            print("Could not find the stock ", user_input, ".")


def correct_date(prompt):

    """This function checks for valid date input, if incorrect the user is warned and
    asked to enter date until correct date input is given."""

    while True:
        date_input = input(prompt)
        try:
            datetime.datetime.strptime(date_input, "%m/%d/%Y")          # Validates that the date is a correct date
            return date_input
        except ValueError:                                              # datetime module returns ValueError if not correct date format
            print("Incorrect date format. Please enter date as MM/DD/YYYY")


def valid_date_span(purchase_date, sale_date):

    """This function checks whether the purchase date is after the sale date
    Returns a True boolean value if it is, (which is used at functions runtime)
    and returns a False boolean value if the dates are in order logically."""

    purchase_date = datetime.datetime.strptime\
        (purchase_date,"%m/%d/%Y")                                      # convert dates into useable
    sale_date = datetime.datetime.strptime(sale_date,"%m/%d/%Y")        # datetime format

    if sale_date < purchase_date:                                       # If dates does not compare logically
        print("The sale date cannot be greater than the purchase date.")
        return True


def valid_shares(prompt):

    """Take in user input for amount of shares owned and checks to see if it is
    an integer greater than 0. If it is not an int greater than 0 it warns the user
    and forces the user to try again."""

    while True:

        try:
            shares_number = int(input(prompt))

            if shares_number <= 0:
                print("Amount of shares must be greater than 0")
            else:
                return shares_number

        except ValueError:
            print("Shares must be an integer greater than 0")


def open_stock_file(stock_name):

    """Takes in the users stock_input and converts it into the file name that
    contains the stock information for that company"""

    file_name = stock_name.upper() + ".csv"
    return open(file_name, "r")


def make_company_name(stock_name, stock_list, company_list):

    """Takes in the users stock_input and finds the full name of the company
    from the shortened stock name"""

    for name in stock_list:
        if name == stock_name.upper():
            index = stock_list.index(name)
            company_name = company_list[index]
    return company_name


def split_ratio_calculate(in_file, shares, bought_date, sold_date):

    """This will calculate how many times the shares are split over the course
    of time the user owned those shares."""

    shares_total = shares

    for line_str in in_file:
        if "Date" in line_str:                                          # skip the first line
            continue
        line_str = line_str.strip()
        line_list = line_str.split(",")
        if line_list[0] >= bought_date and line_list[0] <= sold_date:   # checks for the information within
                                                                        # the date range
            shares_total *= int(line_list[7])                           # multiply the shares by the split ratio
        else:
            continue
    return shares_total


def total_price_calculate(in_file, bought_date, sold_date, shares, ending_shares):

    """This function iterates through a given file and finds the price of shares at the start
    of the ownership period and the price of shares at the end of the ownership period (multiplied
    by the total ending shares).  The total price is returned, which is the ending price subtracted
    by what was spent at the beginning of the ownership period."""

    for line in in_file:
        if "Date" in line:                                              # skip the first line
            continue
        line = line.strip()
        line_list = line.split(",")
        if line_list[0] == bought_date:                                 # line_str date == bought_date
            open_price = float(line_list[1])
            start_price = open_price * shares                           # total price at the start of period
        elif line_list[0] == sold_date:                                 # line_str date == sold_date
            close_price = float(line_list[4])
            end_price = close_price * ending_shares                     # multiply the ending shares amount (after split_ratio)
                                                                        # by the closing cost of the share
    amount_made = end_price - start_price                               # amount made after factoring in amount spent
    return  amount_made, open_price, close_price, start_price, end_price


def valid_date_input(in_file, bought_date, sold_date):

    """Makes a set of the information from the stock file and checks
    for the bought_date and sold_date in that set. Returns warnings if not found"""

    line_set = set()
    for line in in_file:
        line_list = line.split(",")
        for element in line_list:
            line_set.add(element)

    if bought_date not in line_set and sold_date not in line_set:
        print("Could not locate the start date of", bought_date)       # Let user know that the dates
        print("Could not locate the end date of", sold_date)           # could not be found in the stock_file
        return False
    elif bought_date not in line_set:
        print("Could not locate the start date of", bought_date)       # Just bought_date not found
        return False
    elif sold_date not in line_set:
        print("Could not locate the end date of", sold_date)           # Just sold_date not found
        return False
    else:
        return True


def stock_portfolio(stock_file, stock_name, bought_date, sold_date, shares, company_name):

    """This is the main program function.  It takes in all of our stock information
    and outputs it into a functional and well formatted stock portfolio"""

    total_shares = \
        split_ratio_calculate(stock_file, shares, bought_date, sold_date)

    amount_made, open_price, close_price, bought_price, sold_price = \
        total_price_calculate(stock_file, bought_date, sold_date, shares, total_shares)

    print("Our", company_name, "(" + stock_name + ") Portfolio\n")
    print("{:<10} {:>10} {:>10} {:>10} {:>15}"\
            .format("Action", "Date", "Shares", "Price", "Total Price"))
    print("=" * 59)
    print("{:<10} {:>10} {:>10.1f} {:>10} {:>15}"\
            .format("Buy",bought_date, shares, open_price, bought_price))
    print("{:<10} {:>10} {:>10.1f} {:>10} {:>15}"\
            .format("Sold", sold_date, total_shares, close_price, sold_price))
    print("=" * 59)
    print("{:>59}".format(amount_made))
    stock_file.close()


############
## Main Body
############


stock_list, company_list = convert_to_stocklist()

# Sentinel to continuously loop through program
program_run = True
while program_run:
    stock_input = correct_input("Enter the name of the stock purchased. Enter quit to exit ==> ", stock_list)

    if stock_input.upper() == "QUIT":
        program_run = False

    else:
        company_name = make_company_name(stock_input, stock_list, company_list)
        purchase_date = correct_date("Enter the date you purchased the shares ==> ", )
        sale_date = correct_date("Enter the date the shares were sold ==> ")
        date_span = valid_date_span(purchase_date, sale_date)

        if date_span == True:                                           # returns a True if the span of dates does not work logically
            continue                                                    # returns nothing if the span works

        shares_number = int(valid_shares("How many shares were purchased ==> "))
        stock_file = open_stock_file(stock_input)

        if valid_date_input(stock_file, purchase_date, sale_date) == False:
            continue
        else:
            stock_portfolio(stock_file, stock_input, purchase_date, sale_date, shares_number, company_name)













