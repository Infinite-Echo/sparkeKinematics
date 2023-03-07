#include "base_transformations.hpp"
#include <iostream>
#include <Eigen/Dense>

int main()
{
    std::cout << create_base_translation(2, 2, 1);
    std::cout << create_base_transformation(0, 0, 0, 2, 2, 1);
    return 0;
}