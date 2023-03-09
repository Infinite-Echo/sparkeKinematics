#include <Eigen/Dense>
#include <iostream>
#include <cmath>
#include <leg_transformations.hpp>

using std::cos;
using std::sin;

Eigen::Matrix<float, 4, 4> create_base_to_ee_transformation(Eigen::Matrix<float, 4, 4> Tm, 
                            float theta1, float theta2, float theta3, int leg_id, int x_dir, int y_dir)
{
    Eigen::Matrix<float, 4, 4> Tb0 = create_Tb0(Tm, x_dir, y_dir);
    Eigen::Matrix<float, 4, 4> t01 = create_T01(theta1);
    Eigen::Matrix<float, 4, 4> t12 = create_T12(theta2);
    Eigen::Matrix<float, 4, 4> t23 = create_T23(theta3);
    Eigen::Matrix<float, 4, 4> Tb1 = Tb0 * t01;
    Eigen::Matrix<float, 4, 4> Tb2 = Tb1 * t12;
    Eigen::Matrix<float, 4, 4> Tb3 = Tb2 * t23;
    return Tb3;
}

Eigen::Matrix<float, 4, 4> create_Tb0(Eigen::Matrix<float, 4, 4> Tm, int x_dir, int y_dir)
{
    const float baseLength = float(0.202 * x_dir);
    const float baseWidth = float(0.11 * y_dir);
    Eigen::Matrix<float, 4, 4> legBase;
    legBase << 1, 0, 0, baseLength/2,
               0, 1*y_dir, 0, baseWidth/2,
               0, 0, 1, 0,
               0, 0, 0, 1;
    Eigen::Matrix<float, 4, 4> Tb0 = Tm * legBase;
    return Tb0;
}

Eigen::Matrix<float, 4, 4> create_T01(float theta1)
{
    const float len1 = 0.055;
    Eigen::Matrix<float, 4, 4> t01;
    t01 << 1, 0, 0, 0,
           0, cos(theta1), -sin(theta1), len1*cos(theta1),
           0, sin(theta1), cos(theta1), -len1*sin(theta1),
           0, 0, 0, 1;
    return t01;
}

Eigen::Matrix<float, 4, 4> create_T12(float theta2)
{
    const float len2 = 0.125;
    Eigen::Matrix<float, 4, 4> t12;
    t12 << cos(theta2), 0, -sin(theta2), -len2*cos(theta2),
           0, 1, 0, 0,
           sin(theta2), 0, cos(theta2), -len2*sin(theta2),
           0, 0, 0, 1;
    return t12;
}

Eigen::Matrix<float, 4, 4> create_T23(float theta3){
    const float len3 = 0.135;
    Eigen::Matrix<float, 4, 4> t23;
    t23 << cos(theta3), 0, -sin(theta3), len3*cos(theta3),
           0, 1, 0, 0,
           sin(theta3), 0, cos(theta3), -len3*sin(theta3),
           0, 0, 0, 1;
    return t23;
}