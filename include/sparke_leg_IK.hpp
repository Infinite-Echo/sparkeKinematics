#include <Eigen/Dense>
#include <iostream>
#include <cmath>
#include "leg_transformations.hpp"
#include "base_transformations.hpp"

#define LEN_1   0.055
#define LEN_2   0.125
#define LEN_3   0.135

class SparkeLeg
{
    private:
        /* Variables */
        Eigen::Matrix<float, 4, 4> t_b0, t_01, t_12, t_23;
        float theta1, theta2, theta3;
        int x_dir, y_dir;

        /* functions */
        //Maybe put get dirs function in this class instead of legtf
        void update_Tb0(Eigen::Matrix<float, 4, 4> Tm);
        void solve_angles(Eigen::Matrix<float, 4, 4> Tm, float x_ee,
                                                     float y_ee, float z_ee);
        void solve_theta1(float y_ee, float z_ee);
        void solve_theta2(float x_ee, float z_ee);
        void solve_theta3(float x_ee, float z_ee);
        void get_dirs(int leg_id);
        Eigen::Matrix<float, 4, 4> get_tb1();
    public:
        SparkeLeg(int leg_id);
        ~SparkeLeg();
};