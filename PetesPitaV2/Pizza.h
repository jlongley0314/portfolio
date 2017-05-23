//
//  Pizza.h
//  Program3
//

#include "MenuItem.h"

class Pizza: public MenuItem
{
public:
    Pizza() { size = small, crustType = thin; }
    // Setters
    void setSize(char S);
    void setCrustType(char C);
    void setModifications(string M);
private:
    enum size{ small, medium, large, family };
    enum crustType{ thin, thick, stuffed };
    string modification[5];
};