#include <iostream> 

int main(){
    
    //Braced Initializers
    //Variable may contain random garbage value. WARNING
    
    int elephant_count; //gives garbage value

    int lion_count{}; // initializes to zero

    int dog_count {10}; // initializes to 10

    int cat_count {15}; // initializes to 15

    //can use expression as initalizer

    int domesticated_animals { dog_count + cat_count };

    //
    //int new_num{doesnt_exist}; //doesnt_exist has not been declared

    //int narrowing_conversion {2.9}; //error 

    std::cout << "Elephant count: " << elephant_count << std::endl;
    std::cout << "Lion count: " << lion_count << std::endl;
    std::cout << "Dog count: " << dog_count << std::endl;
    std::cout << "Cat count: " << cat_count << std::endl;
    
    std::cout << "Domesticated animal count: " << domesticated_animals << std::endl;
    

    //Functional Initialization
    
    int apple_count(5);
    int orange_count(10);
    int fruit_count (apple_count + orange_count);
    //int bad_intialization ( doesnt_exist3 + doesnt_exist4);

    //information lost. less safe than braced initalizers

    int narrowing_conversion_function(2.9); //will store a two instead of 2.9

    std::cout << "Apple count: " << apple_count << std::endl;

    std::cout << "Orange count: " << orange_count << std::endl;

    std::cout << "Fruit count: " << fruit_count << std::endl;

    std::cout << "Narrowing conversion: " << narrowing_conversion_function << std::endl;
    

    //Assignment Notation

    int bike_count = 2;
    int truck_count = 7;
    int vehicle_count = bike_count + truck_count;
    int narrowing_conversion_assignment = 2.9; //still chops off .9 

    std::cout << "Bike count: " << bike_count << std::endl;
    std::cout << "Truck count: " << truck_count << std::endl;
    std::cout << "Vehicle count: " << vehicle_count << std::endl;
    std::cout << "Narrowing conversion: " << narrowing_conversion_assignment << std::endl;



    //check size with sizeof

    std::cout << "size of int: " << sizeof(int) << std::endl; //returns 4 bytes
    std::cout << "size of truck_count: " << sizeof(truck_count) << std::endl; //returns 4 bytes

    return 0;
}