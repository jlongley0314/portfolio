//
//  MenuItem.h
//  Program3
//

#pragma once

#include <iostream>
#include <string>
using namespace std;

class MenuItem
{
public:
    MenuItem() { price = 0.0; }
    // getters
    string GetName() const { return name; }
    string GetDescription() const { return description; }
    float GetPrice() const { return price; }
    // setters
    void setName(string N);
    void setDescription(string D);
protected:
    float price;    // This will be set by the child classes
private:
    string name;
    string description;
};
