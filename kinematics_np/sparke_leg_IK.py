import numpy as np
import leg_transformations as legtf
import base_transformations as basetf

class sparkeLeg():
    def __init__(self, leg_id):
        self.init_variables(leg_id)
        self.initialize_leg_transforms()

    def init_variables(self, leg_id):
        self.x_dir, self.y_dir = legtf.get_dirs(leg_id)
        self.len1 = 0.055
        self.len2 = 0.125
        self.len3 = 0.135

    def initialize_leg_transforms(self):
        self.t_01 = legtf.create_T01(0)
        self.t_12 = legtf.create_T12(0)
        self.t_23 = legtf.create_T23(0)

    def update_Tb0(self, Tm):
        self.t_b0 = legtf.create_Tb0(Tm, self.x_dir, self.y_dir)

    def solve_angles(self, Tm, x_ee, y_ee, z_ee):
        self.update_Tb0(Tm)
        self.solve_theta1(y_ee, z_ee)
        self.solve_theta3(x_ee, z_ee)
        self.solve_theta2(x_ee, z_ee)

    def solve_theta1(self, y_ee, z_ee):
        y0, z0 = self.t_b0[1, 3], self.t_b0[2, 3]
        c = np.sqrt(((z_ee-z0)**2) + ((y_ee-y0)**2))
        b = np.sqrt((c**2)-(self.len1**2))
        thetaA = np.arctan2((z_ee-z0), (y_ee-y0)*self.y_dir)
        thetaB = np.arctan2(-b, self.len1)
        theta1 = thetaB - thetaA
        self.theta1 = round(theta1, 4)

    def solve_theta3(self, x_ee, z_ee):
        t_b1 = self.get_tb1()
        x1, z1 = t_b1[0,3], t_b1[2,3]
        x1_ee = x_ee - x1
        z1_ee = z_ee - z1 #CHECK for which should be first
        a = (x1_ee**2) + (z1_ee**2) - (self.len2**2) - (self.len3**2)
        b = -2*self.len2*self.len3
        theta3 = (np.arccos(a/b)/2)
        self.theta3 = round(theta3, 4)

    def solve_theta2(self, x_ee, z_ee):
        t_b1 = self.get_tb1()
        x1, z1 = t_b1[0,3], t_b1[2,3]
        a = self.len3 * np.sin(self.theta3) * self.x_dir
        b = self.len3 * np.cos(self.theta3)
        x2 = abs(x_ee - a)
        z2 = abs(z_ee + b)
        x1_2 = x1 - x2
        z1_2 = z1 - z2
        theta2 = np.arctan2(z1_2, x1_2)
        self.theta2 = round(theta2, 4)

    def get_tb1(self):
        self.t_01 = legtf.create_T01(self.theta1)
        t_b1 = np.matmul(self.t_b0, self.t_01)
        return t_b1

# def main():
#     Tm = basetf.create_base_transformation(0, 0, 0, 0, 0, 0)
#     x_ee = 0.1080710678
#     y_ee = 0.11
#     z_ee = -0.1838477631
#     leg_test = sparkeLeg(1)
#     leg_test.solve_angles(Tm, x_ee, y_ee, z_ee)
#     print(f'theta1: {leg_test.theta1}')
#     print(f'theta2: {leg_test.theta2}')
#     print(f'theta3: {leg_test.theta3}')


# if __name__ == '__main__':
#     main()