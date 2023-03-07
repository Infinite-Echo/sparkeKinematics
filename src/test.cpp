#include "base_transformations.hpp"
#include "leg_transformations.hpp"
#include <iostream>
#include <Eigen/Dense>

//0.10807106781186547, 0.11, -0.18384776310850237

int main()
{
    Eigen::Matrix<float, 4, 4> Tm = create_base_transformation(0, 0, 0, 0, 0, 0);
    std::cout << create_base_to_ee_transformation(Tm, 0, M_PI/4, M_PI/2, 1);
    return 0;
}