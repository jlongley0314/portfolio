/*********************************************
 
 
 Name:	Jaremy Longley
 Course: CS 201
 Program:	Program 3
 Due Date:	06/27/2016
 
 Description:	Pete's Pizza has branched out 
    and now has a storefront location.
    1 order in 20 (randomly selected) gets a 
    20% discount. You have a data file
    containing a day's orders. Create a class 
    hierarchy of a base menuItem class and
    derived Pizza and Sandwich classes.  Read 
    in a days order to the specific class,
    apply the discount to a random order,
    and print put the results from the days
    orders.
 
 Inputs:	File to be read in.
 
 Outputs:	How many items of each type were sold?
    What were the total sales for each type?
    How many items were discounted?
    What was the total amount of all discounts given?
 
Algorithm:	
 
 1) Create base class MenuItem:
    a) declare a name (just declared in base class),
    with the ability to get   the name and set the name
    b) declare a description (just declared in base class),
    with the ability   to get and set the description
    c) declare a price (shared between base and derived)
    d) by default, set price to 0
 
 2) Create a class Pizza, inherited from MenuItem:
    a) declare a size (can be small/medium/large/family)
        i) price: $7 for small, $8 for medium, $10 for large,
        $12 for family
        ii) When size is set, price should be set respectively
    b) declare a crust type (can be thin/thick/stuffed):
        i) stuffed adds $1 more, should be added when type is declared
    c) Up to 5 modifications (no affect to price)
    d) Pizza should default to small size and thin crust
    e) be able to read in data in the following order
    (remember that each is on its own line, so read the whole line in):
        i) Name
        ii) Description
        iii) size
        iv) crust type
        v) up to 5 modifications (ends with '*', whether 5 or none)
        vi) dynamically set the price of the pizza as the data is
        read in
        vii) return true if read successfully
 
 3) Create a class Sandwich, inherited from MenuItem:
     a) declare a side item (chips/slaw/fries)
     b) all sandwiches cost $8
     c) be able to read in data in the following order
     (each item is on its own line):
        i) name
        ii) description
        ii) side item
        iv) return true if read successfully
     
 4) Create a function to apply a discount for selected items
     a) If rand() % 100 < 20, apply discount,
     otherwise return original price.
     b) either return original price or return discounted price
 5) Print:
     a) How many pizzas were sold
     b) How many sandwiches were sold
     c) total sales
     d) less discount
     c) net sales

 
 *********************************************/

#include <iostream>
using namespace std;

int main()
{
    
    return 0;
}
















