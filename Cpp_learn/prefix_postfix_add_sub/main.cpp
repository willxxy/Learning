#include <iostream> 

int main(){
    
    int value {5};

    value = value + 1;
    std::cout << "the value is: " << value << std::endl;

    value = 5;
    value = value -1;
    std::cout << "the value is : " << value << std::endl;

    std::cout << "=====Postfix increment and decrement=======" << std::endl;

    value = 5;
    std::cout << "the value is (incrementing) : " << value++ << std::endl; //increment by one
    std::cout << "the value is " << value << std::endl;

    std::cout << std::endl;

    value = 5;

    std::cout <<"The value is (decrementing): " << value-- <<std::endl;
    std::cout << "the value is: " << value << std::endl;

    std::cout << "=====Prefix increment and decrement=======" << std::endl;

    value = 5;
    
    ++value;
    std::cout << "the value is (prefix++) :" << value << std::endl;

    value = 5;
    std::cout << " the value is (prefix++ in place) : " << ++value << std::endl;

    std::cout << std::endl;

    //Prefix : Decrementing

    value = 5;
    --value;
    std::cout << "the value is (predix--) : " << value << std::endl;

    value = 5;
    std::cout << "the value is (predix-- in place) : " << --value << std::endl;

    return 0;
}