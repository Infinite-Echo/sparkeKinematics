#include "sparke_base_IK.hpp"
#include "base_transformations.hpp"
// #include "sparke_leg_IK.hpp"
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
    SparkeLeg testLeg1 = SparkeLeg(1);
    SparkeLeg testLeg2 = SparkeLeg(2);
    SparkeLeg testLeg3 = SparkeLeg(3);
    SparkeLeg testLeg4 = SparkeLeg(4);

    SparkeBase testSparke = SparkeBase();
    array<float, 4> xArray = {
        0.10807106781186548,
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
    testLeg1.solve_angles(Tm, xArray[0], yArray[0], zArray[0]);
    testLeg2.solve_angles(Tm, xArray[1], yArray[1], zArray[1]);
    testLeg3.solve_angles(Tm, xArray[2], yArray[2], zArray[2]);
    testLeg4.solve_angles(Tm, xArray[3], yArray[3], zArray[3]);

    std::cout << testLeg1.theta1 << std::endl;
    std::cout << testLeg1.theta2 << std::endl;
    std::cout << testLeg1.theta3 << std::endl;
    
    std::cout << testLeg2.theta1 << std::endl;
    std::cout << testLeg2.theta2 << std::endl;
    std::cout << testLeg2.theta3 << std::endl;

    std::cout << testLeg3.theta1 << std::endl;
    std::cout << testLeg3.theta2 << std::endl;
    std::cout << testLeg3.theta3 << std::endl;

    std::cout << testLeg4.theta1 << std::endl;
    std::cout << testLeg4.theta2 << std::endl;
    std::cout << testLeg4.theta3 << std::endl;

    // array<float, 12> angles = testSparke.get_angles_from_trajectory(Tm,xArray,yArray,zArray);
    // for(int i = 0; i<12; i++)
    // {
    //     std::cout << angles[i] << std::endl;
    // }
    return 0;
}