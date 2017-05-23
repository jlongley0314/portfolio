########################################################################
##
## Amusement Park Tram Simulator
## Jaremy Longley
## jlongley0314@gmail.com
##
## PROBLEM : Create a basic simulation of a amusement park with trams picking up and
##             dropping off tourists at the amusement park.
##
## ALGORITHM :
##
##      Classes:
#
# Create Park Class(inherits from object)
#     define initialization(params = self, lots_total = default to 4, ttl_tourists = default to 10)
#         self.lots_total = lots_total
#         self.ttl_tourists = ttl_tourists
#         tourist_list = self.place_tourist(pass the ttl_tourists and the lots)
#         lots = self.create_parking_lot(pass the lots_total and the tourist_list)
#         tram = create a tram instance and send lots for the lots_list, keep
#             current_lot as default
#
#     define string representation (param = self)
#         return the string representation of the ParkingLot instances, nicely formatted,
#             along with the string representatin of the Tram instance formatted below the
#             ParkingLot the tram is currently at
#
#
#     define place_tourist method (params = self, tourists, lots)
#         tourist_list = empty list to be filled with tourist tuples
#         for person in range tourists
#             start_lot = random_number from 0 to lots - 1
#             destination = random_number from 0 to lots - 1 excluding start_lot
#             tourist = create tourist instance(pass start_lot, destination)
#             append the tourist to tourist_list
#         return tourist_list
#
#     define create_parking_lot method ( params = self, lots_total, lot_list, tourist_list)
#         lot_list = empty list to be filled with parking_lot instances
#         for lot in range lots_total
#             parking_lot = create a parking lot instance and pass it lot
#                 for the lot_number and tourist_list for the list of tourists
#             append the parking_lost instance to the lot_list so that the lot_list
#                 is a list of parking_lot instances that are then filled with tourist
#                 instances
#         return the lot_list
#
#
#     define step method (param = self)
#         call move method for tram
#
#
#
# Create ParkingLot Class(inherits from object)
#     define initialization(params = self, lot_number, tourist_list)
#         self.lot_number = lot_number
#         self.tourist_list = tourist_list
#         self.build_wait_list
#
#     define string representation (param = self)
#         return the lot_number and the number of tourists in the wait_list
#
#     define build_wait_list()
#         wait_list = empty list to be filled with tourists waiting
#         for tourist in tourist_list
#             if tourists start_lot (index[0]) == lot_number
#                 append tourist to wait_list to build up a list
#                 of tourist instances in the wait_list
#         return wait_list
#
#
# Create Tram Class(inherits from object)
#     define initialization(params = self, lots_list, current_lot = default to 0)
#         self.lots_list = lots_list
#         self.current_lot = current_lot
#         initialize direction = 1 (moving forward)
#         tram_list = empty list
#
#     define string representation (param = self)
#         return "T" with the length of the tram_list and an arrow
#             indicating the direction (">" for forward, "<" for backward)
#
#
#     define move method( params = self, lots, current_lot )
#         for tourist in lots at index[current_lot]
#             append tourist to tram_list
#
#         count = 0 (track how many tourist got off the tram)
#         for tourist in tram_list
#             if tourist.arrived( pass current lot number and tourist[1] as destination ) == True
#                 remove tourist from tram_list
#                 update count by 1
#
#         clear lot at index[current_lot]
#         if current_lot = lots at index[-1] (last lot)
#             direction = -1
#             decrement current_lot by direction
#         else
#             update current_lot by direction
#
#
# Create Tourist Class(inherits from object)
#     define initialization(params = self, lot_start, destination)
#         self.lot_start = lot_start
#         self.destination = destination
#         self.build_tourist_tup(lot_start, destination)
#
#     define string representation (param = self)
#         return tuple from build_tourist_tup method
#
#     define build_tourist_tup(params = self, lot_start, destination)
#         return tuple of lot_start and destination
#
#
#     define arrived attribute(parms = self, lot_number, destination)
#         if lot_number == destination
#             return True
#         else
#             return
#
#
# Functions:
#
# Create valid_choices function(Takes prompt and maximum params)
#     while True
#         user_input = ask for input from user using prompt
#         if user_input > 0 and user_input <= maximum
#             return user_input
#         else
#             warn user they must enter an int greater than 0 and less than maximum
#
#
#
# Main Body:
#
# lots_total = Run valid_choices function(sending prompt and 11 for maximum)
#
# tourist_number = Run this through valid_choices function
#     (sending prompt and 20 for maximum)
#
# Create Park instance and pass (lots_total and tourist_number)
#
# while True:
#     print string representation of the park instance
#     call the step method for the park instance
#     user_input = prompt user("Enter Q to quit")
#     if user_input == "Q" or "q":
#         break
#
##
## ERROR HANDLING:
##      Any input entered will be run through a function checking for valid choices.
##      If the content is not within the valid choices, the user will be forced to enter
##      something that is valid.
##
########################################################################

import random


############
## Classes
############


class Park(object):

    """My main them park class"""

    def __init__(self, lots_total : int, ttl_tourists : int):
        self.lots_total = lots_total
        self.ttl_tourists = ttl_tourists
        self.tourist_list = self.place_tourists(self.ttl_tourists, self.lots_total)
        self.lots = self.create_parking_lots(self.lots_total, self.tourist_list)
        self.tram = Tram(self.lots)                                 # Create and instance of Tram

    def __str__(self):
        buffer = ""
        count = 0
        while count <= len(self.lots) - 1:
            if count != 0:
                buffer += "=={}  ".format(self.lots[count])
            else:
                buffer += "{}  ".format(self.lots[count])
            count += 1
        return buffer

    def place_tourists(self, tourists, lots_total):

        """Randomly places each tourist in a Parking Lot waiting list"""
        tourist_list = []

        for person in range(tourists):
            start_lot = random.randint(0, lots_total - 1)           # Random starting location
            range1 = [r for r in range(0, start_lot)]               # Create list of available lots up to start_lot
            range2 = [r for r in range(start_lot + 1, lots_total - 1)]  # Create list of available lots after start_lot
            dest_lot = random.choice(range1 + range2)               # Choose random destination from the range
            tourist = Tourist(start_lot, dest_lot)                  # Create an instance of tourist
            tourist_list.append(tourist)                            # Build up tourist_list

        return tourist_list

    def create_parking_lots(self, lots_total, tourist_list):

        """Create an instance of the Parking Lot class and receive the wait_list from that instance"""

        lot_list = []

        for lot in range(lots_total):
            parking_lot = ParkingLot(lot, tourist_list)
            lot_list.append(parking_lot)                            # Build up a list of instances of ParkingLot

        return lot_list

    def step(self):

        """Calls tram.move()"""

        self.tram.move()
        self.tram.all_aboard()



class ParkingLot(object):

    """Individual Parking Lots"""

    def __init__(self, lot_number, tourist_list):
        self.lot_number = lot_number
        self.tourist_list = tourist_list
        self.wait_list = self.build_wait_list()

    def __str__(self):
        return "L{}({})".format(self.lot_number, len(self.wait_list))

    def __repr__(self):
        return self.__str__()

    def build_wait_list(self):
        wait_list = []
        for tourist in self.tourist_list:
            if tourist.tourist_tup[0] == self.lot_number:
                wait_list.append(tourist)                           # build up a list of the tourist instances waiting at that lot
        return wait_list



class Tram(object):

    """The Tram servicing the Park"""

    def __init__(self, lots_list, current_lot = 0):
        self.lots_list = lots_list
        self.current_lot = current_lot
        self.direction = 1                                          # initialize to moving forward
        self.tram_list = []                                         # empty list to be filled with tourist instances
        self.all_aboard()
        self.pickup_count = len(self.tram_list)
        self.drop_off_count = 0


    def __str__(self):
        if self.direction == 1:
            return "T({})>".format(len(self.tram_list))             # Should look like T(n)>, where
        else:
            return "<T({})".format(len(self.tram_list))             # Should look like <T(n), where

    def all_aboard(self):

        """Passengers climb aboard the tram and get taken out of the wait list of the parking lot instance"""

        self.pickup_count = 0                                       # count number of tourists picked up
        for tourist in self.lots_list[self.current_lot].wait_list:            # Tourists move from parking lot wait_list to the tram_list
            self.tram_list.append(tourist)
            self.pickup_count += 1
        self.lots_list[self.current_lot].wait_list.clear()          # Remove tourist instances from the parking lot wait_list

    def move(self):

        """Moves the tram to the next ParkingLot instance"""

        count = 0
        index = 0

        if self.current_lot == (len(self.lots_list) - 1):           # if the current_lot is the last lot
            self.direction = -1                                     # tram moves in opposite direction
            self.current_lot += self.direction
        else:
            self.current_lot += self.direction                      # move the tram forward or backward depending on direction

        self.drop_off_count = 0

        while index <= (len(self.tram_list) - 1):                   # iterate through tram_list with a while loop
            tourist = self.tram_list[index]
            if tourist.arrived(self.current_lot) == True:           # call arrived method for tourist instance
                self.tram_list.remove(tourist)                      # tourist has arrived, gets off the tram
                                                                    # if the tourist is removed, keep the index the same
                self.drop_off_count += 1                            # count number of tourists dropped off
            else:
                index += 1                                          # if tourist hasn't arrived, move along to the next tourist


class Tourist(object):

    """Individual Tourists waiting to be picked up and dropped off"""

    def __init__(self, lot_start, destination):
        self.lot_start = lot_start
        self.destination = destination
        self.tourist_tup = self.build_tourist_tup(lot_start, destination)

    def __str__(self):
        return "{}".format(self.tourist_tup)

    def __repr__(self):
        return self.__str__()

    def build_tourist_tup(self, lot_start, destination):

        """Builds a tuple displaying the lot the tourist starts in and his/her destination lot"""

        return (lot_start, destination)                             # creates a tuple of the lot_start and the destination

    def arrived(self, lot_number):

        """Checks to see if tourist is at their destination lot, returns True if yes, False if no"""

        if lot_number == self.destination:
            return True
        else:
            return False


##############
## Functions
##############


def valid_choices(prompt, max_val):

    """Verifies valid user input"""

    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 0 and user_input <= max_val:
                return int(user_input)
            else:
                print("Please enter an integer from 0 to {}".format(max_val))
        except ValueError:
            print("Please enter an integer from 0 to {}".format(max_val))

def park_status():

    """Create our park status display"""

    spacing = park.tram.current_lot * 9                             # set up the spacing that our tram print string sits in
    if park.tram.current_lot >= 10:                                 # spacing has to update since there is another digit added
        spacing += 1

    if len(park.tram.tram_list) >= 10:                              # spacing has to update since there is another digit added
        spacing += 1

    buffer = " " * spacing                                          # spaces in front of the printed tram

    display = """
Park Status

Tram picked up {} tourists.
Tram dropped off {} tourists.

{}
{}{:^3}
{}{}
        """.format(park.tram.pickup_count, park.tram.drop_off_count, park, buffer, "|", buffer, park.tram)
    return display

##############
## Main Body
##############


lots_total = valid_choices("Enter the total number of lots: ", 11)
tourist_number = valid_choices("Enter the total number of tourists in the park: ", 20)
park = Park(lots_total, tourist_number)
while True:
    park_display = park_status()
    print(park_display)
    user_input = input("Enter Q to quit ==> ")
    if user_input.upper() == "Q":
        break
    park.step()












