#include <Eigen/Dense>
#include <iostream>
#include <cmath>

Eigen::Matrix<float, 4, 4> create_base_transformation(float x_base, float y_base, float z_base,
                                                      float roll, float pitch, float yaw);

Eigen::Matrix<float, 4, 4> create_base_translation(float x_base, float y_base, float z_base);

Eigen::Matrix<float, 4, 4> create_rotxyz(float roll, float pitch, float yaw);

Eigen::Matrix<float, 4, 4> create_rotx(float roll);

Eigen::Matrix<float, 4, 4> create_roty(float pitch);

Eigen::Matrix<float, 4, 4> create_rotz(float yaw);