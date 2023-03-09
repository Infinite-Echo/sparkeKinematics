#include <Eigen/Dense>
#include <iostream>
#include <cmath>
#include <array>
#include "sparke_base_IK.hpp"

SparkeBase::SparkeBase()
{
    
}

SparkeBase::~SparkeBase()
{

}

array<float,12> SparkeBase::get_angles_from_trajectory(Eigen::Matrix<float,4,4> Tm,
            array<float,4> x_end_effectors, array<float,4> y_end_effectors, 
            array<float,4> z_end_effectors)
{
    fl_leg.solve_angles(Tm, x_end_effectors[0], y_end_effectors[0], z_end_effectors[0]);
    fr_leg.solve_angles(Tm, x_end_effectors[1], y_end_effectors[1], z_end_effectors[1]);
    bl_leg.solve_angles(Tm, x_end_effectors[2], y_end_effectors[2], z_end_effectors[2]);
    br_leg.solve_angles(Tm, x_end_effectors[3], y_end_effectors[3], z_end_effectors[3]);

    array<float,12> joint_angles = {fr_leg.theta3, fr_leg.theta2, fr_leg.theta1,
                                    br_leg.theta3, br_leg.theta2, br_leg.theta1,
                                    bl_leg.theta3, bl_leg.theta2, bl_leg.theta1,
                                    fl_leg.theta3, fl_leg.theta2, fl_leg.theta1, };
    return joint_angles;
}