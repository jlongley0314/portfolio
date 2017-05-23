#pragma once

#include <iostream>
#include <string>
using namespace std;

class Pizza
{

public:
    Pizza() { pizzas = 0,
              chips = 0,
              drinks = 0,
              candy = 0,
              price = 0,
              toppingNumber = 0,
              bread = ""; }
    
    // Getters
    int GetPizzas() const { return PizzasNum; }
    int GetChips() const { return ChipsNum; }
    int GetDrinks() const { return DrinksNum; }
    int GetCandy() const { return CandyNum; }
    string GetBread() const { return BreadType; }
    string GetTopping() const { return ToppingChoice; }
    float GetPrice() const { return TotalPrice; }
    
    // Setters
    void SetPizzas(int N);
    void SetChips(int N);
    void SetDrinks(int N);
    void SetCandy(int N);
    void SetToppingNumber(int T);
    void SetToppingName(string T);
    void SetTotalPrice(int Pizzas, int Chips, int Drinks, int Candy, string toppingArray[]);
    
    
    // I/O
    bool ReadData(istream& in);
    bool WriteData(ostream& out);
private:
    int pizzas;
    int chips, drinks, candy, toppingNumber;
    float price;
    string bread, toppingName[5];
    
    
};
