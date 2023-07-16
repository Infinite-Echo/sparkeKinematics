// #include "sparke_base_IK.hpp"
// #include "base_transformations.hpp"
// #include "sparke_leg_IK.hpp"
#include "base_transformations.hpp"
#include <iostream>
#include <Eigen/Dense>
#include <chrono>
// #include <array>

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
    auto start_time = std::chrono::high_resolution_clock::now();
    
    for (int i = 0; i < 10; ++i) {
        Eigen::Matrix<float, 4, 4> Tm = create_base_transformation(5,1,5,1,5,1);
        std::cout << "Transformation " << i+1 << ":\n" << Tm << std::endl;
    }
    
    auto end_time = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time);

    std::cout << "Start time was " << std::chrono::time_point_cast<std::chrono::milliseconds>(start_time).time_since_epoch().count() << " milliseconds." << std::endl;
    std::cout << "End time was " << std::chrono::time_point_cast<std::chrono::milliseconds>(end_time).time_since_epoch().count() << " milliseconds." << std::endl;
    std::cout << "Total duration was " << duration.count() << " milliseconds." << std::endl;

    return 0;
}