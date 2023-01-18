import sympy as sym
import math as m

# % L1 = 0.055
# % L2 = 0.125
# % L3 = 0.135
# % W/2 = 0.055
# % L/2 = 0.101

def solve_for_angles(Tm, x_ee, y_ee, z_ee):
    Tb0 = create_Tb0(Tm)
    y0 = Tb0[1,3]
    z0 = Tb0[2,3]
    print(f'y0: {y0}')
    print(f'z0: {z0}')
    y03 = y_ee - y0
    z03 = z_ee - z0
    print(f'y03: {y03}')
    print(f'z03: {z03}')
    q1 = m.atan2(z03, y03)
    # t01 = create_T01(theta1)
    # Tb1 = Tb0 * t01
    # Tb2 = Tb1 * t12
    # Tb3 = Tb2 * t23
    return q1

def create_base_to_ee_transformation(Tm, x_ee, y_ee, z_ee):
    theta1, theta2, theta3 = sym.symbols('theta1, theta2, theta3')
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
    legBase = sym.Matrix([
        [1, 0, 0, baseLength/2],
        [0, 1, 0, baseWidth/2],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])
    Tb0 = Tm * legBase
    return Tb0

def create_T01(theta1):
    len1 = 0.055
    t01 = sym.Matrix([
        [1, 0, 0, 0],
        [0, sym.cos(theta1), -sym.sin(theta1), len1*sym.cos(theta1)],
        [0, sym.sin(theta1), sym.cos(theta1), -len1*sym.sin(theta1)],
        [0, 0, 0, 1],
    ])
    return t01

def create_T12(theta2):
    len2 = 0.125
    t12 = sym.Matrix([
        [sym.cos(theta2), 0, -sym.sin(theta2), -len2*sym.cos(theta2+(sym.pi/4))],
        [0, 1, 0, 0],
        [sym.sin(theta2), 0, sym.cos(theta2), -len2*sym.sin(theta2+(sym.pi/4))],
        [0, 0, 0, 1],
    ])
    return t12

def create_T23(theta3):
    len3 = 0.135
    t23 = sym.Matrix([
        [sym.cos(theta3), 0, -sym.sin(theta3), len3*sym.cos(theta3+(sym.pi/4))],
        [0, 1, 0, 0],
        [sym.sin(theta3), 0, sym.cos(theta3), -len3*sym.sin(theta3+(sym.pi/4))],
        [0, 0, 0, 1],
    ])
    return t23