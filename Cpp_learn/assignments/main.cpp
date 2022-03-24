#include <iostream> 

int main(){
    
    int var1{123}; // Declare and initialize
    std::cout << "var1: " << var1 << std::endl;

    var1 = 55; // Assign
    std::cout << "var1: " << var1 << std::endl;

    std::cout << std::endl;

    std::cout << "------------------------" << std::endl;

    double var2 {44.55}; //declare and initialize
    std::cout <<"var2: " << var2 << std::endl;

    var2 = 90.99; // Assign
    std::cout << "var2: " << var2 << std::endl;

    std::cout << std::endl;

    std::cout << "------------------------" << std::endl;


    std::cout << std::endl;

    bool state{false}; //declare and initialize
    std::cout << std::boolalpha;
    std::cout << "state: " << state << std::endl;

    state = true; //Assign

    std::cout << "state: " << state << std::endl;

    //Auto type deduction (be careful)

    auto var3{333u}; //declare and initalize with type deduction
    
    var3 = -22; //assign negative number. DANGER! puts in garbage value

    std::cout << "var3: " << var3 << std::endl;

    return 0;



    return 0;

}