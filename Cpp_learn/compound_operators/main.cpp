#include <iostream> 


int main(){

int value {45};

std::cout << "the value is : " << value << std::endl;

std::cout << std::endl;
value +=5;
std::cout << " the value is (after +=5): " << value << std::endl;

std::cout << std::endl;
value -= 5;
std::cout << "the value is (after -=5: " << value << std::endl;

std::cout <<std::endl;
value *= 2;
std::cout << "the value is (after *=2: " << value << std::endl;

std::cout <<std::endl;
value /= 3;
std::cout << "the value is (after /=3: " << value << std::endl;

std::cout <<std::endl;
value %= 11;
std::cout << "the value is (after %=11: " << value << std::endl;

return 0;    
}