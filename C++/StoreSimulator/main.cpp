/*********************************************


Name: Jaremy Longley

Course: CS 201

Program: Program #7

Description: The MegaMicroMart (a subsidiary of Fly-By-Night Industries) 
	is planning their next Big Small-Box Store. They want to ensure good
	customer service, and you've been hired to do some simulations to
	advise them on how to set up their checkout lines. You will report
	your findings to an output file and write up a description of what
	they mean.

Inputs:	Three iput files

Outputs: One output file displaying my simulation findings

*********************************************/

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <math.h> 
#include <list>
using namespace std;

struct Customer
{
	int itemsInCart = 0;
	int timeArrived = 0;
	int timeStartedChkout = 0;
	int timeFinished = 0;
	int totalTimeWaiting = 0;

};

struct Register
{
	bool isIdle = true;	// true for register not in use
	bool isExpress = false; // check for express lane
	Customer customerCheckingOut;
	list<Customer> waitingList;
	int waiting = 0;
};

void regTypeOne(list<Customer> C, string testCase, ofstream& out, int listSize);
// Precondition: a list of customers has been built up and an output 
//		file has been opened
// Postcondition: the necessary data has been sent off to an output file

void regTypeTwo(list<Customer> C, string testCase, ofstream& out, int listSize);
// Precondition: a list of customers has been built up and an output 
//		file has been opened
// Postcondition: the necessary data has been sent off to an output file

void regTypeThree(list<Customer> C, string testCase, ofstream& out, int listSize);
// Precondition: a list of customers has been built up and an output 
//		file has been opened
// Postcondition: the necessary data has been sent off to an output file

int shortestWaitList(Register a[]);
// Precondition: an array of register objects has been built up
// Postcondition: the index of the shortest register is returned

int calculateCheckoutTime(Customer C, int time);
// Precondition: a customer has reached the checkout
// Postcondition: the time customer leaves the store has been calculated

void outputData(ofstream& out, int regType, string& testCase,
	int customersServed, int maxLineLength, int avgTimeWaiting,
	int maxWaitingTime, int timeRegistersIdle);
// Precondition: a registerType function has been ran and information 
//		has been collected
// Postcondition: the information has been output to an output file

int main()
{
	ifstream steadyIn, bigCrunchIn, bigTicketIn;
	ofstream fout;
	list<Customer> steadyState, bigCrunch, bigTickets;
	int readIn, count = 0;

	// Open files
	steadyIn.open("steadystate.txt"); bigCrunchIn.open("bigcrunch.txt");
	bigTicketIn.open("bigtickets.txt");
	fout.open("output.txt");
	while (steadyIn >> readIn)
	{
		Customer C;
		C.timeArrived = readIn;
		steadyIn >> C.itemsInCart;
		steadyState.push_back(C);
		count++;
	}
	regTypeOne(steadyState, "Steady State", fout, count);
	regTypeTwo(steadyState, "Steady State", fout, count);
	regTypeThree(steadyState, "Steady State", fout, count);
	count = 0;
	while (bigCrunchIn >> readIn)
	{
		Customer C;
		C.timeArrived = readIn;
		bigCrunchIn >> C.itemsInCart;
		bigCrunch.push_back(C);
		count++;
	}
	regTypeOne(bigCrunch, "Big Crunch", fout, count);
	regTypeTwo(bigCrunch, "Big Crunch", fout, count);
	regTypeThree(bigCrunch, "Big Crunch", fout, count);
	count = 0;
	while (bigTicketIn >> readIn)
	{
		Customer C;
		C.timeArrived = readIn;
		bigTicketIn >> C.itemsInCart;
		bigTickets.push_back(C);
		count++;
	}
	regTypeOne(bigTickets, "Big Tickets", fout, count);
	regTypeTwo(bigTickets, "Big Tickets", fout, count);
	regTypeThree(bigTickets, "Big Tickets", fout, count);

	return 0;
}


// RegisterType Functions

void regTypeOne(list<Customer> C, string testCase, ofstream& out, int listSize)
{
	int totalNumCustomers = listSize,
		totalWaitingTime = 0,
		timeRegistersIdle = 0,
		maxLineLength = 0,
		maxTimeInLine = 0,
		clockTick = 0,
		index;

	list<Customer> customersCompletedService;
	Register regArr[6];
	while (totalNumCustomers != customersCompletedService.size())
	{
		clockTick++;
		if (!C.empty() && C.front().timeArrived <= clockTick)
		{
			index = shortestWaitList(regArr);	// find the shortest register
			regArr[index].waitingList.push_back(C.front());
			C.pop_front();
			regArr[index].waiting++;
			if (regArr[index].waiting > maxLineLength)
				maxLineLength = regArr[index].waiting;
		}

		for (int i = 0; i <= 5; i++)
		{
			// A customer begins checking out
			if (regArr[i].waiting >= 1 && regArr[i].isIdle == true)
			{
				regArr[i].isIdle = false;
				regArr[i].customerCheckingOut = regArr[i].waitingList.front();
				regArr[i].waitingList.pop_front();
				regArr[i].customerCheckingOut.timeStartedChkout = clockTick;
				regArr[i].waiting--;
				regArr[i].customerCheckingOut.timeFinished +=
					calculateCheckoutTime(regArr[i].customerCheckingOut, 
					clockTick);
				// determine total time customer waited
				totalWaitingTime += regArr[i].customerCheckingOut.timeFinished -
					regArr[i].customerCheckingOut.timeStartedChkout;
				// determine the maximum time someone stood in line
				if (regArr[i].customerCheckingOut.timeStartedChkout -
					regArr[i].customerCheckingOut.timeArrived > maxTimeInLine)
				{
					maxTimeInLine = (regArr[i].customerCheckingOut.timeStartedChkout -
						regArr[i].customerCheckingOut.timeArrived);
				}

			}
			// Register is truly idle, no customers waiting
			else if (regArr[i].isIdle == true && regArr[i].waitingList.empty())
			{
				timeRegistersIdle++;
			}
			// A customer has completely finished at the store
			if (regArr[i].customerCheckingOut.timeFinished == clockTick)
			{
				customersCompletedService.push_back
					(regArr[i].customerCheckingOut);
				regArr[i].isIdle = true;
			}
		}
	}
	outputData(
		out,
		1,
		testCase,
		customersCompletedService.size(),
		maxLineLength,
		// simple round up function
		(totalWaitingTime + customersCompletedService.size() - 1) /
		customersCompletedService.size(),
		maxTimeInLine,
		timeRegistersIdle);
}
void regTypeTwo(list<Customer> C, string testCase, ofstream& out, int listSize)
{
	int totalNumCustomers = listSize,
		totalWaitingTime = 0,
		timeRegistersIdle = 0,
		maxLineLength = 0,
		maxTimeInLine = 0,
		clockTick = 0,
		index;

	list<Customer> customersCompletedService;
	Register regArr[6];
	regArr[0].isExpress = true;
	while (totalNumCustomers != customersCompletedService.size())
	{
		clockTick++;
		if (!C.empty() && C.front().timeArrived <= clockTick)
		{
			index = shortestWaitList(regArr);	// find the shortest register

			if (C.front().itemsInCart <= 10 && regArr[0].waiting <= 3 ||
				(regArr[0].waiting - 3 <= regArr[index].waiting))
			// items in cart 10 or less, and register has 3 or less people or
			// register has no more than 3 more customers than the shortest reg
			{
				// Customer enters express lane
				regArr[0].waitingList.push_back(C.front());
				C.pop_front();
				regArr[0].waiting++;
			}
			else
			{
				// Customer enters normal lane
				regArr[index].waitingList.push_front(C.front());
				C.pop_front();
				regArr[index].waiting++;
			}
		}

		for (int i = 0; i <= 5; i++)
		{
			if (regArr[i].waiting > maxLineLength)
				maxLineLength = regArr[i].waiting;
			// A customer begins checking out
			if (regArr[i].waiting >= 1 && regArr[i].isIdle == true)
			{
				regArr[i].isIdle = false;
				regArr[i].customerCheckingOut = regArr[i].waitingList.front();
				regArr[i].waitingList.pop_front();
				regArr[i].customerCheckingOut.timeStartedChkout = clockTick;
				regArr[i].waiting--;
				regArr[i].customerCheckingOut.timeFinished +=
					calculateCheckoutTime(regArr[i].customerCheckingOut,
					clockTick);
				// determine total time customer waited
				totalWaitingTime += regArr[i].customerCheckingOut.timeFinished -
					regArr[i].customerCheckingOut.timeStartedChkout;
				// determine the maximum time someone stood in line
				if (regArr[i].customerCheckingOut.timeStartedChkout -
					regArr[i].customerCheckingOut.timeArrived > maxTimeInLine)
				{
					maxTimeInLine = (regArr[i].customerCheckingOut.timeStartedChkout -
						regArr[i].customerCheckingOut.timeArrived);
				}

			}
			// Register is truly idle, no customers waiting
			else if (regArr[i].isIdle == true && regArr[i].waitingList.empty())
			{
				timeRegistersIdle++;
			}
			// A customer has completely finished at the store
			if (regArr[i].customerCheckingOut.timeFinished == clockTick)
			{
				customersCompletedService.push_back
					(regArr[i].customerCheckingOut);
				regArr[i].isIdle = true;
			}
		}
	}
	outputData(
		out,
		2,
		testCase,
		customersCompletedService.size(),
		maxLineLength,
		// simple round up function
		(totalWaitingTime + customersCompletedService.size() - 1) / 
		customersCompletedService.size(),
		maxTimeInLine,
		timeRegistersIdle);
}
void regTypeThree(list<Customer> C, string testCase, ofstream& out, int listSize)
{
	int totalNumCustomers = listSize,
		totalWaitingTime = 0,
		timeRegistersIdle = 0,
		maxLineLength = 0,
		maxTimeInLine = 0,
		clockTick = 0,
		index;

	list<Customer> customersCompletedService,
		waitingList;
	Register regArr[6];
	while (totalNumCustomers != customersCompletedService.size())
	{
		clockTick++;
		// Place customers all in one line to wait for a reg to open
		while (!C.empty())
		{ 
			if (C.front().timeArrived <= clockTick)
			{
				waitingList.push_back(C.front());
				C.pop_front();
			}
			else
				break;
		}
		for (int i = 0; i <= 5; i++)
		{
			// if register is empty and the waiting list has customers
			// send a customer to the empty register to checkout
			if (regArr[i].isIdle == true && !waitingList.empty())
			{
				regArr[i].customerCheckingOut = waitingList.front();
				waitingList.pop_front();
				regArr[i].isIdle = false;
				regArr[i].customerCheckingOut.timeStartedChkout = clockTick;
				regArr[i].customerCheckingOut.timeFinished = 
					calculateCheckoutTime(regArr[i].customerCheckingOut, clockTick);
				totalWaitingTime += regArr[i].customerCheckingOut.timeFinished -
					regArr[i].customerCheckingOut.timeStartedChkout;
				// determine the maximum time someone stood in line
				if (regArr[i].customerCheckingOut.timeStartedChkout -
					regArr[i].customerCheckingOut.timeArrived > maxTimeInLine)
				{
					maxTimeInLine = (regArr[i].customerCheckingOut.timeStartedChkout -
						regArr[i].customerCheckingOut.timeArrived);
				}
			}
			// Register is truly idle, no customers waiting
			else if (regArr[i].isIdle == true && waitingList.empty())
			{
				timeRegistersIdle++;
			}
			// If a customer finishes checking out
			if (regArr[i].isIdle == false && regArr[i].customerCheckingOut.timeFinished == clockTick)
			{
				customersCompletedService.push_back(regArr[i].customerCheckingOut);
				regArr[i].isIdle = true;
			}
		}
	}
	outputData(
		out,
		3,
		testCase,
		customersCompletedService.size(),
		maxLineLength,
		// simple round up function
		(totalWaitingTime + customersCompletedService.size() - 1) /
		customersCompletedService.size(),
		maxTimeInLine,
		timeRegistersIdle);
}
int calculateCheckoutTime(Customer C, int time)
{
	int checkoutTime = 0;
	// simple function for checkout time rounded up
	int checkoutTimeRounded = (C.itemsInCart + 3 - 1) / 3;
	checkoutTime += C.timeStartedChkout + checkoutTimeRounded + (rand() % 3);
	return (checkoutTime);
}
int shortestWaitList(Register a[])
{
	int shortest = 0;
	for (int i = 0; i <= 5; i++)
	{
		if (a[i].waitingList.size() <= a[shortest].waitingList.size())
		{
			shortest = i;
			if (a[shortest].isExpress == true)	
				// will not set shortest to express lane
				shortest++;
		}
	}	
	return shortest;
}
void outputData(ofstream& out, int regType, string& testCase,
	int customersServed, int maxLineLength, int avgTimeWaiting,
	int maxWaitingTime, int timeRegistersIdle)
{
	switch (regType)
	{
	case 1:
		out << "\n------------------------\n" << 
			" No Express Lane Used " << "\n------------------------" <<
			"\nTest Case: " << testCase
			<< "\nCustomers Served: " << customersServed
			<< "\nMaximum length of any line: " << maxLineLength
			<< "\nAverage length of time in line: " << avgTimeWaiting * 10 << " seconds"
			<< "\nMaximum length of time in line: " << (maxWaitingTime + 6 - 1) / 6 << " minutes"
			<< "\nTotal amount of time registers were idle: " << timeRegistersIdle / 6 << " minutes"
			<< "\n" << endl;
		break;
	case 2:
		out << "\n------------------------\n" <<
			 "Express Lane Used" << "\n------------------------" <<
			"\nTest Case: " << testCase
			<< "\nCustomers Served: " << customersServed
			<< "\nMaximum length of any line: " << maxLineLength
			<< "\nAverage length of time in line: " << avgTimeWaiting * 10 << " seconds"
			<< "\nMaximum length of time in line: " << (maxWaitingTime + 6 - 1) / 6 << " minutes"
			<< "\nTotal amount of time registers were idle: " << timeRegistersIdle / 6 << " minutes"
			<< "\n" << endl;
		break;
	case 3:
		out << "\n------------------------\n" <<
			"Single Line Method" << "\n------------------------" <<
			"\nTest Case: " << testCase
			<< "\nCustomers Served: " << customersServed
			<< "\nMaximum length of any line: " << maxLineLength
			<< "\nAverage length of time in line: " << avgTimeWaiting * 10 << " seconds"
			<< "\nMaximum length of time in line: " << (maxWaitingTime + 6 - 1) / 6 << " minutes"
			<< "\nTotal amount of time registers were idle: " << timeRegistersIdle / 6 << " minutes"
			<< "\n" << endl;
		break;
	default:
		out << "Error" << endl;
		break;
	}
}
