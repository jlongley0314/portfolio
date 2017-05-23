/*********************************************
 
 
 Name:	Jaremy Longley
 
 Course:    CS201
 
 Program:	Program 1
 
 Due Date:	6/13/2016
 
 Description:	Create a program that asks user to
    enter a value to get the square root of.
    The program runs the value through the Babylonian 
    algorithm and checks how close this
    is to the actual square root.
 
 Inputs:	user Number
            iterations
            run again
 
 Outputs:	"What number would you like to find the square root of?"
            "How many iterations?"
            Square Root from babylonian algorithm
            Square Root from square root function
            "Would you like to run again (Y/N)?"
 
 
 Algorithm:	
 1. Create a function to ask user for number they would like to 
    find the square root of.
    a. Loop until user gives a number greater than 0.
 
 2. Create a function to ask user for number of iterations they 
    would like the program to run.
    a. Loop until the user gives a number between 0 and 100,000.
 
 3. Create a function to carry out the Babylonian algorithm.
    a. Set e == 1 (first estimate)
    b. Set x == the users input from 1.
    c. For iterations 1 to user input from 2.
    d. If x/e == e
        1. Return e
        2. Exit algorithm
    e. Else
        1. e = average of x and x/e
    f. Return to step d
 
 4. Report actual square root value vs. value from 3.
 
 5. Ask user to run again or quit.
    a. If user wants to run again, return to 1.
    b. If user quits, exit program.
 
 
 *********************************************/

#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int getNumber(string prompt);
//Passes a prompt asking the
//user for number to find the square root of
//Loops until user gives a number greater than 0

int getIteration(string prompt);
//Passes a prompt asking the user for number
//of iterations they want to run
//Loops until a number is given between 0 and 100,000

int babylAlgor(int num1, int num2);
//Sends the two numbers through the Babylonian algorithm
//Uses the first to estimate the square root value
//Uses the second to determine the number of iterations
//to run


int main()
{
    int userNumber, iterations, sqrRootEstimate;
    char runAgain;
    
    while (true)
    {
        
        userNumber = getNumber("What number do you want to find the square root of? ");
        iterations = getIteration("\nHow many iterations of the Babylonian Algorithm would you like to run?");
        sqrRootEstimate = babylAlgor(userNumber, iterations);    // Find the Babylonian algorithm square Root
        
        cout << "Babylonian Algorithm: " << sqrRootEstimate << endl;
        cout << "Square Root: " << sqrt(userNumber);
        
        cout << "\nWould you like to run program again (Y/N)?" << endl;
        cin >> runAgain;
        if (runAgain == 'n' || runAgain == 'N')
        {
        
            break;
        
        }
        
    }
    
    
    return 0;
}


int getNumber(string prompt)
{
    int num;
    
    while (true)
    {
    
        cout << prompt << endl;
        cin >> num;
        
        if (num > 0)
        {
            
            return num;
            
        }
        else
        {
        
            cout << "Please enter a number greater than 0." << endl;
        
        }
    
    }
}


int getIteration(string prompt)
{

    int iteration;
    
    while (true)
    {
    
        cout << prompt << endl;
        cin >> iteration;
        
        if ((iteration > 0) && (iteration <= 100000))
        {
        
            return iteration;
            
        }
        else
        {
        
            cout << "Please enter a number between 1 and 100,000." << endl;
        
        }
    
    }
}


int babylAlgor(int num1, int num2)
{
    int estimate = 1;
    int userNumb = num1;
    
    for (int iteration = 0; iteration < num2; iteration++)
    {                                                           // Run this function until the number of iterations
                                                                // are met or the correct number is found
        if ((userNumb/estimate) == estimate)                    // Check if estimate is the square root
        {
        
            return estimate;
            
        }
        else
        {
        
            estimate = (userNumb + (userNumb/estimate))/2;      // Get the average of userNumb and userNumb/estimate
        
        }
        
    }
    return estimate;                                            // Returns the estimate once the iteration limit has ended
}










