#include <Eigen/Dense>
#include <iostream>
#include <cmath>

Eigen::Matrix<float, 4, 4> create_base_to_ee_transformation(Eigen::Matrix<float, 4, 4> Tm, 
                            float theta1, float theta2, float theta3, int leg_id);

void get_dirs(int leg_id, int &x_dir, int &y_dir);

Eigen::Matrix<float, 4, 4> create_Tb0(Eigen::Matrix<float, 4, 4> Tm, int x_dir, int y_dir);

Eigen::Matrix<float, 4, 4> create_T01(float theta1);

Eigen::Matrix<float, 4, 4> create_T12(float theta2);

Eigen::Matrix<float, 4, 4> create_T23(float theta3);