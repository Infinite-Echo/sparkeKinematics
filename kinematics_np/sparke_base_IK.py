from sparke_leg_IK import sparkeLeg
import numpy as np

class sparkeBase():
    def __init__(self):
        self.create_legs()

    def create_legs(self):
        self.fl_leg = sparkeLeg(1)
        self.fr_leg = sparkeLeg(2)
        self.bl_leg = sparkeLeg(3)
        self.br_leg = sparkeLeg(4)

    def get_angles_from_trajectory(self, Tm, x_end_effectors, y_end_effectors, z_end_effectors):
        self.fl_leg.solve_angles(Tm, x_end_effectors[0], y_end_effectors[0], z_end_effectors[0])
        self.fr_leg.solve_angles(Tm, x_end_effectors[1], y_end_effectors[1], z_end_effectors[1])
        self.bl_leg.solve_angles(Tm, x_end_effectors[2], y_end_effectors[2], z_end_effectors[2])
        self.br_leg.solve_angles(Tm, x_end_effectors[3], y_end_effectors[3], z_end_effectors[3])

        #note order is important
        joint_angles = np.array([
            self.fr_leg.theta3, self.fr_leg.theta2, self.fr_leg.theta1, 
            self.br_leg.theta3, self.br_leg.theta2, self.br_leg.theta1, 
            self.bl_leg.theta3, self.bl_leg.theta2, self.bl_leg.theta1, 
            self.fl_leg.theta3, self.fl_leg.theta2, self.fl_leg.theta1, 
            ])
        return joint_angles