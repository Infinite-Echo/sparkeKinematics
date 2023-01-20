import numpy as np

# % L1 = 0.055
# % L2 = 0.125
# % L3 = 0.135
# % W/2 = 0.055
# % L/2 = 0.101

def create_base_to_ee_transformation(Tm, x_ee, y_ee, z_ee, theta1, theta2, theta3):
    Tb0 = create_Tb0(Tm)
    t01 = create_T01(theta1)
    t12 = create_T12(theta2)
    t23 = create_T23(theta3)
    Tb1 = Tb0 * t01
    Tb2 = Tb1 * t12
    Tb3 = Tb2 * t23
    return Tb3

def create_Tb0(Tm):
    baseLength = 0.202
    baseWidth = 0.11
    legBase = np.matrix([
        [1, 0, 0, baseLength/2],
        [0, 1, 0, baseWidth/2],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])
    Tb0 = Tm * legBase
    return Tb0

def create_T01(theta1):
    len1 = 0.055
    t01 = np.matrix([
        [1, 0, 0, 0],
        [0, np.cos(theta1), -np.sin(theta1), len1*np.cos(theta1)],
        [0, np.sin(theta1), np.cos(theta1), -len1*np.sin(theta1)],
        [0, 0, 0, 1],
    ])
    return t01

def create_T12(theta2):
    len2 = 0.125
    t12 = np.matrix([
        [np.cos(theta2), 0, -np.sin(theta2), -len2*np.cos(theta2+(np.pi/4))],
        [0, 1, 0, 0],
        [np.sin(theta2), 0, np.cos(theta2), -len2*np.sin(theta2+(np.pi/4))],
        [0, 0, 0, 1],
    ])
    return t12

def create_T23(theta3):
    len3 = 0.135
    t23 = np.matrix([
        [np.cos(theta3), 0, -np.sin(theta3), len3*np.cos(theta3+(np.pi/4))],
        [0, 1, 0, 0],
        [np.sin(theta3), 0, np.cos(theta3), -len3*np.sin(theta3+(np.pi/4))],
        [0, 0, 0, 1],
    ])
    return t23