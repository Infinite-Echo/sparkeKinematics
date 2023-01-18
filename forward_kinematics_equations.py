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

def test_eq():
    x_ee = 0.1080710678
    y_ee = 0.11
    z_ee = -0.1838477631
    len1 = 0.055
    c = m.sqrt(((z_ee-0)**2) + ((y_ee-0.055)**2))
    b = m.sqrt((c**2)-(len1**2))
    thetaA = m.atan2((z_ee-0), (y_ee-0.055))
    thetaB = m.atan2(-b, len1)
    theta1 = thetaB - thetaA
    # theta1 = m.atan2(z_ee, y_ee) + m.atan2(m.sqrt((y_ee**2)+(z_ee**2)+(0.055**2)), -0.055)
    print(theta1)

def main():
    # cosb, cos1 = sym.symbols('cosb, cos1')
    # A = sym.Matrix([[1, cosb], [cos1, 1]])
    # print(A**2)
    # print_xyz_equations()
    # x_ee = (0.005*m.sqrt(2)) + 0.101
    # y_ee = (0.0225742726730441*m.sqrt(2)) + 0.109164425701277
    # z_ee = (-0.128025006203019*m.sqrt(2)) - 0.00955065382321095
    # print(z_ee)
    # print_solved_angles(x_ee, y_ee, z_ee)
    # print_home()
    test_eq()

# -1.2801098374086937 = 0 degrees
# -1.1465608223128407 = 10 degrees

if __name__ == '__main__':
    main()

# a*sin(y)*sin(z) + a*sin(y)*cos(z) + a*cos(y)*cos(z) - a*cos(y)*sin(z) - b*cos(y) + b*sin(y) = d
# -a*sin(x)*sin(y)*cos(z) + a*sin(x)*sin(y)*sin(z) + b*sin(x)*sin(y) + b*sin(x)*cos(y) + a*sin(x)*cos(y)*sin(z) + a*sin(x)*cos(y)*cos(z) + c*cos(x) = e
# -c*sin(x) + a*sin(y)*cos(x)*cos(z) - a*sin(y)*cos(x)*sin(z) - b*cos(x)*sin(y) - b*cos(x)*sin(y) - a*cos(x)*cos(y)*sin(z) - a*cos(x)*cos(y)*cos(z) = f