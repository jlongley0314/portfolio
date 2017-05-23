#include "Pizza.h"

bool Pizza::ReadData(istream& in)
{
    
	// Read in data until the # to indicate end of order
    while ((in >> pizzas) != -1)                    // -1 indicates the end of the file
	{
        price = 0;
        
        //if (pizzas == '#')                          // Figure out what to do when I read the '#'
        
		int index, count = 0;

		in >> bread;
		while ((in >> toppingName[index]) != "*")
		{
			index++;
			count++;
		}
        toppingNumber = count;                      // ToppingNumber will be updated to the number
                                                    // iterations in the previous loop
		if ((in >> chips) < 0)
			cout << "Chips can't be less than 0.";
			return false;
		if ((in >> candy) < 0)
			cout << "Candy can't be less than 0.";
			return false;
		if ((in >> drinks) < 0)
			cout << "Drinks can't be less than 0.";
			return false;
        
        price += GetPrice();
        
        Pizza::WriteData(ostream& out);             // Send all of this data to the WriteData function
                                                    // before reading the next order
	}
    
    return in.good();

}

bool Pizza::WriteData(ostream& out)
{
    int index = 0;
    
    out << pizzas << '\n' << bread << '\n';
    while (index != toppingNumber - 1)              // Print the toppings to the outfile as long as the
    {                                               // there are toppings in the array to print
        
        cout << toppingName[index] << endl;
        index++;
        
    }

}