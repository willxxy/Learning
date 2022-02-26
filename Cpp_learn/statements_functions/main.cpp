#include <iostream> 


int addnum(int first_parameter, int second_parameter){

    int result = first_parameter + second_parameter;

    return result; 

}


int main(){

    int first_number {6}; // statement 
    int second_number {5};

    std::cout << "First Number: " << first_number << std::endl;
    std::cout << "Second Number: " << second_number << std::endl;


    int sum = first_number + second_number;
    std::cout << "Sum: " << sum << std::endl;

    sum = addnum(first_number, second_number);

    std::cout << "Sum: " << sum << std::endl;


    sum = addnum(40, 43);
    std::cout << "Sum: " << sum << std::endl;

    std::cout << "Sum: " << addnum(3, 55) << std::endl;

    return 0;

    
}