#include <iostream> 
#include <iomanip>

//1 byte = 8 bits
//float - 4 bytes
//double - 8 bytes
//long double - 12 bytes

int main(){
    
    float number1 {1.12345678901234567890f}; //need to write the f
    double number2 {1.12345678901234567890};
    long double number3 {1.12345678901234567890L}; //need to write the L


    //Print out sizes

    std::cout << "size of float: " << sizeof(float) << std::endl; // precision: 7
    std::cout << "size of double: " << sizeof(double) << std::endl; // precision: 15
    std::cout << "size of long double: " << sizeof(long double) << std::endl; // precision: 20


    //Precision
    std::cout << std::setprecision(20); //control precision from std::cout from <iomanip>
    std::cout << "numeber 1 is: " << number1  << std::endl; //7 digits
    std::cout << "number 2 is: " << number2 << std::endl; //15'ish digits
    std::cout << "number 3 is: " << number3 << std::endl; //15+ digits

    //float problems: the precision is usually too limited
    //for a lot of applications
    double number4 {192400023.0}; //error: narrowing conversion

    std::cout << "number4: " << number4 << std::endl;

    //scientific notation

    double number5 {192400023};
    double number6 {1.92400023e8};
    double number7 {1.924e8};       //can eomit 0023
                                    //for simplicity if our application allows
    double number8 {0.00000000003498};
    double number9 {3.498e-11}; // multiply with 10 exp(-11)

    std::cout << "number5 is: " << number5 << std::endl;
    std::cout << "number6 is: " << number6 << std::endl;
    std::cout << "number7 is: " << number7 << std::endl;
    std::cout << "number8 is: " << number8 << std::endl;
    std::cout << "number9 is: " << number9 << std::endl;


    //infinity and nan
    std::cout << std::endl;
    std::cout << "infinity and NaN" << std::endl;
    double number10{-5.6}; // if positive you get positive infinity
    double number11{}; //initialized to 0
    double number12{}; //initialized to 0

    //infinity
    double result{number10 / number11};
    
    std::cout << number10 << "/" << number11 << " yields " << result << std::endl;
    std::cout << result << " + " << number10 << " yields " << result + number10 << std::endl;

    //NaN
    result = number11 / number12;

    std::cout<< result << "/" << number12 << "=" << result << std::endl;

    return 0;
}