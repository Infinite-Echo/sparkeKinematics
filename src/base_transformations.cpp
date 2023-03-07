#include <Eigen/Dense>
#include <iostream>
#include <cmath>
#include "base_transformations.hpp"

Eigen::Matrix<float, 4, 4> create_base_transformation(float x_base, float y_base, float z_base,
                                                      float roll, float pitch, float yaw)
{
    Eigen::Matrix<float, 4, 4> rotxyz = create_rotxyz(roll, pitch, yaw);
    Eigen::Matrix<float, 4, 4> Tbase = create_base_translation(x_base, y_base, z_base);
    Eigen::Matrix<float, 4, 4> Tm = rotxyz*Tbase;
}

Eigen::Matrix<float, 4, 4> create_base_translation(float x_base, float y_base, float z_base)
{
    Eigen::Matrix<float, 4, 4> Tbase;
    Tbase << 1, 0, 0, x_base,
             0, 1, 0, y_base,
             0, 0, 1, z_base,
             0, 0, 0, 1;
    return Tbase;
}

Eigen::Matrix<float, 4, 4> create_rotxyz(float roll, float pitch, float yaw)
{
    Eigen::Matrix<float, 4, 4> rotx = create_rotx(roll);
    Eigen::Matrix<float, 4, 4> roty = create_roty(pitch);
    Eigen::Matrix<float, 4, 4> rotz = create_rotz(yaw);
    Eigen::Matrix<float, 4, 4> rotxyz = (rotx*roty)*rotz;
    return rotxyz;
}

Eigen::Matrix<float, 4, 4> create_rotx(float roll)
{
    Eigen::Matrix<float, 4, 4> rotx;
    rotx << 1, 0, 0, 0,
            0, std::cos(roll), -std::sin(roll), 0,
            0, std::sin(roll), std::cos(roll), 0,
            0, 0, 0, 1;
    return rotx;
}

Eigen::Matrix<float, 4, 4> create_roty(float pitch)
{
    Eigen::Matrix<float, 4, 4> roty;
    roty << std::cos(pitch), 0, -std::sin(pitch), 0,
            0, 1, 0, 0,
            std::sin(pitch), 0, std::cos(pitch), 0,
            0, 0, 0, 1;
    return roty;
}

Eigen::Matrix<float, 4, 4> create_rotz(float yaw)
{
    Eigen::Matrix<float, 4, 4> rotz;
    rotz << std::cos(yaw), -std::sin(yaw), 0, 0,
            std::sin(yaw), std::cos(yaw), 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1;
    return rotz;
}