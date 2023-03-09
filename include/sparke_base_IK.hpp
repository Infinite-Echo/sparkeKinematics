#include <Eigen/Dense>
#include <iostream>
#include <cmath>
#include <array>
#include "sparke_leg_IK.hpp"
using std::array;
class SparkeBase
{
    private:
        SparkeLeg fl_leg = SparkeLeg(1);
        SparkeLeg fr_leg = SparkeLeg(2);
        SparkeLeg bl_leg = SparkeLeg(3);
        SparkeLeg br_leg = SparkeLeg(4);
    public:
        SparkeBase();
        ~SparkeBase();
        array<float,12> get_angles_from_trajectory(Eigen::Matrix<float,4,4> Tm,
            array<float,4> x_end_effectors, array<float,4> y_end_effectors, 
            array<float,4> z_end_effectors);
};