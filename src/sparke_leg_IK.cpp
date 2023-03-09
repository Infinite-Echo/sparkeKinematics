#include <Eigen/Dense>
#include <iostream>
#include <cmath>
#include "leg_transformations.hpp"
#include "base_transformations.hpp"
#include "sparke_leg_IK.hpp"

SparkeLeg::SparkeLeg(int leg_id)
{
    get_dirs(leg_id);
    t_01 = create_T01(0);
    t_12 = create_T12(0);
    t_23 = create_T23(0);
}

SparkeLeg::~SparkeLeg()
{

}

void SparkeLeg::update_Tb0(Eigen::Matrix<float, 4, 4> Tm)
{
    t_b0 = create_Tb0(Tm, x_dir, y_dir);
}

void SparkeLeg::solve_angles(Eigen::Matrix<float, 4, 4> Tm, float x_ee,
                                                     float y_ee, float z_ee)
{
    update_Tb0(Tm);
    solve_theta1(y_ee, z_ee);
    solve_theta3(x_ee, z_ee);
    solve_theta2(x_ee, y_ee);
}

void SparkeLeg::solve_theta1(float y_ee, float z_ee)
{
    float y0, z0, c, b, thetaA, thetaB;
    y_ee = abs(y_ee);
    z_ee = abs(z_ee);
    y0 = abs(t_b0(1,3));
    z0 = abs(t_b0(2,3));
    c = sqrt((pow((z_ee-z0), 2)) + (pow((y_ee-y0), 2)));
    b = sqrt((pow(c,2))-(pow(LEN_1,2)));
    thetaA = atan2(abs(z_ee - z0), abs(y_ee-y0));
    thetaB = atan2(b, LEN_1);
    theta1 = thetaB - thetaA;
}

void SparkeLeg::solve_theta3(float x_ee, float z_ee)
{
    float x1, z1, x1_ee, z1_ee, a, b;
    Eigen::Matrix<float,4,4> t_b1 = get_tb1();
    x1 = abs(t_b1(0,3));
    z1 = abs(t_b1(2,3));
    x1_ee = x_ee - x1;
    z1_ee = z_ee - z1;
    a = pow(x1_ee, 2) + pow(z1_ee, 2) - pow(LEN_2, 2) - pow(LEN_3, 2);
    b = -2 * LEN_2 * LEN_3;
    theta3 = acos(a/b);
}

void SparkeLeg::solve_theta2(float x_ee, float z_ee)
{
    float x1, z1, x1_3, z1_3, alpha, beta, a, b, c;
    Eigen::Matrix<float,4,4> t_b1 = get_tb1();
    x1 = abs(t_b1(0,3));
    z1 = abs(t_b1(2,3));
    x1_3 = abs(x_ee - x1) * -1;
    z1_3 = z_ee - z1;
    alpha = atan2(z1_3, x1_3);
    c = sqrt(pow(x1_3, 2) + pow(z1_3, 2));
    a = pow(LEN_3, 2) - pow(LEN_2, 2) - pow(c, 2);
    b = -2*LEN_2*c;
    beta = acos(a/b);
    theta2 = alpha - beta;
}

Eigen::Matrix<float, 4, 4> SparkeLeg::get_tb1()
{
    t_01 = create_T01(theta1);
    Eigen::Matrix<float,4,4> t_b1 = t_b0 * t_01;
    return t_b1;
}

void SparkeLeg::get_dirs(int leg_id)
{
    if (leg_id==1)
    {
        x_dir = 1;
        y_dir = 1;
    } 
    else if (leg_id == 2)
    {
        x_dir = 1;
        y_dir = -1;
    }
    else if (leg_id == 3)
    {
        x_dir = -1;
        y_dir = 1;
    }
    else if (leg_id == 4)
    {
        x_dir = -1;
        y_dir = -1;
    }
}
