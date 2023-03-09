#include "sparke_base_IK.hpp"
#include "base_transformations.hpp"
#include <iostream>
#include <Eigen/Dense>
#include <array>

//0.10807106781186547, 0.11, -0.18384776310850237

/*
theta1: 0.0
theta2: 0.7853981633974481
theta3: 1.5707963267948968
X Pos: 0.10807106781186548
Y Pos: 0.11
Z Pos: -0.18384776310850237
theta1: 0.0
theta2: 0.7853981633974481
theta3: 1.5707963267948968
X Pos: 0.10807106781186548
Y Pos: -0.11
Z Pos: -0.18384776310850237
theta1: 0.0
theta2: 0.7853981633974481
theta3: 1.5707963267948968
X Pos: -0.09392893218813454
Y Pos: 0.11
Z Pos: -0.18384776310850237
theta1: 0.0
theta2: 0.7853981633974481
theta3: 1.5707963267948968
X Pos: -0.09392893218813454
Y Pos: -0.11
Z Pos: -0.18384776310850237
*/

int main()
{
    SparkeBase testSparke = SparkeBase();
    array<float, 4> xArray = {
        0.11,
        0.10807106781186548,
        -0.09392893218813454,
        -0.09392893218813454
    };
    array<float, 4> yArray = {
        0.11,
        -0.11,
        0.11,
        -0.11
    };
    array<float, 4> zArray = {
        -0.18384776310850237,
        -0.18384776310850237,
        -0.18384776310850237,
        -0.18384776310850237
    };
    Eigen::Matrix<float, 4, 4> Tm = create_base_transformation(0,0,0,0,0,0);
    array<float, 12> angles = testSparke.get_angles_from_trajectory(Tm,xArray,yArray,zArray);
    for(int i = 0; i<12; i++)
    {
        std::cout << angles[i] << std::endl;
    }
    return 0;
}