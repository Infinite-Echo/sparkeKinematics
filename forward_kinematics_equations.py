import sympy as sym
import transformations as tf
import leg_transformations as legtf
import math as m

def print_home():
    Tm = tf.create_base_transformation(0, 0, 0, 0, 0, 0)
    Tb0 = legtf.create_Tb0(Tm)
    t01 = legtf.create_T01(0)
    t12 = legtf.create_T12(0)
    t23 = legtf.create_T23(0)
    Tb1 = Tb0 * t01
    Tb2 = Tb1 * t12
    Tb3 = Tb2 * t23
    print(f'X0: {Tb0[0,3]} | Y0: {Tb0[1,3]} | Z0: {Tb0[2,3]}')
    print(f'X1: {Tb1[0,3]} | Y1: {Tb1[1,3]} | Z1: {Tb1[2,3]}')
    print(f'X2: {Tb2[0,3]} | Y2: {Tb2[1,3]} | Z2: {Tb2[2,3]}')
    print(f'X3: {Tb3[0,3]} | Y3: {Tb3[1,3]} | Z3: {Tb3[2,3]}')

def print_xyz_equations():
    Tm = tf.create_base_transformation(0, 0, 0, 0, 0, 0)
    x_ee, y_ee, z_ee = sym.symbols('x_ee, y_ee, z_ee')
    Tbee = legtf.create_base_to_ee_transformation(Tm, x_ee, y_ee, z_ee)
    print(f'X: {Tbee[0, 3]}')
    print(f'---------------')
    print(f'Y: {Tbee[1, 3]}')
    print(f'---------------')
    print(f'Z: {Tbee[2, 3]}')
    print(f'---------------')
    return

def print_solved_angles(x_ee, y_ee, z_ee):
    Tm = tf.create_base_transformation(0, 0, 0, 0, 0, 0)
    print(legtf.solve_for_angles(Tm, x_ee, y_ee, z_ee))

def test_eq(x_ee, y_ee, z_ee):
    len1 = 0.055
    c = m.sqrt(((z_ee-0)**2) + ((y_ee-0.055)**2))
    b = m.sqrt((c**2)-(len1**2))
    thetaA = m.atan2((z_ee-0), (y_ee-0.055))
    thetaB = m.atan2(-b, len1)
    theta1 = thetaB - thetaA
    return theta1

def test_eq2(x_ee, y_ee, z_ee, theta1):
    len2 = 0.125
    len3 = 0.135
    x13 = (x_ee - 0.101)
    z13 = (z_ee - 0)
    a = (x13**2) + (z13**2) - (len2**2) - (len3**2)
    b = -2*len2*len3
    theta3 = (m.acos(a/b)/2)
    theta3 = round(theta3, 4)
    return theta3

def test_eq3(x_ee, y_ee, z_ee, theta3):
    len2 = 0.125
    len3 = 0.135
    a = len3 * m.sin(theta3)
    b = len3 * m.cos(theta3)
    x2 = abs(x_ee - a)
    z2 = abs(z_ee + b)
    x12 = 0.101 - x2
    z12 = z2
    print(x12)
    print(z12)
    theta2 = m.atan2(z12, x12)
    theta2 = round(theta2, 4)
    return theta2

def main():
    x_ee = 0.1080710678
    y_ee = 0.11
    z_ee = -0.1838477631
    # print_home()
    theta1 = test_eq(x_ee, y_ee, z_ee)
    theta3 = test_eq2(x_ee, y_ee, z_ee, theta1)
    theta2 = test_eq3(x_ee, y_ee, z_ee, theta3)
    print(f'theta1: {theta1}')
    print(f'theta2: {theta2}')
    print(f'theta3: {theta3}')

if __name__ == '__main__':
    main()

# a*sin(y)*sin(z) + a*sin(y)*cos(z) + a*cos(y)*cos(z) - a*cos(y)*sin(z) - b*cos(y) + b*sin(y) = d
# -a*sin(x)*sin(y)*cos(z) + a*sin(x)*sin(y)*sin(z) + b*sin(x)*sin(y) + b*sin(x)*cos(y) + a*sin(x)*cos(y)*sin(z) + a*sin(x)*cos(y)*cos(z) + c*cos(x) = e
# -c*sin(x) + a*sin(y)*cos(x)*cos(z) - a*sin(y)*cos(x)*sin(z) - b*cos(x)*sin(y) - b*cos(x)*sin(y) - a*cos(x)*cos(y)*sin(z) - a*cos(x)*cos(y)*cos(z) = f