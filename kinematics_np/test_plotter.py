import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sparke_leg_IK import sparkeLeg as spLegIK
import base_transformations as basetf
import leg_transformations as legtf

def plot_points(arr1, arr2):
    # Create figure and 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the points from arr1
    ax.scatter(arr1[:,0], arr1[:,1], arr1[:,2], c='r', marker='o')

    # Plot the points from arr2
    ax.scatter(arr2[:,0], arr2[:,1], arr2[:,2], c='b', marker='^')

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Show the plot
    plt.show()

def main():
    
    Tm = basetf.create_base_transformation(0, 0, 0, 0, 0, 0)
    x_ee = 0.1080710678
    y_ee = 0.11
    z_ee = -0.1838477631
    leg = spLegIK(1)
    leg.solve_angles(Tm, x_ee, y_ee, z_ee)
    print(f'theta1: {leg.theta1}')
    print(f'theta2: {leg.theta2}')
    print(f'theta3: {leg.theta3}')

    f_Tb0 = legtf.create_Tb0(Tm)
    f_t01 = legtf.create_T01(0)
    f_t12 = legtf.create_T12(0)
    f_t23 = legtf.create_T23(0)
    f_Tb1 = np.matmul(f_Tb0, f_t01)
    f_Tb2 = np.matmul(f_Tb1, f_t12)
    f_Tb3 = np.matmul(f_Tb2, f_t23)
    f_x0, f_y0, f_z0 = f_Tb0[0,3], f_Tb0[1,3], f_Tb0[2,3]
    f_x1, f_y1, f_z1 = f_Tb1[0,3], f_Tb1[1,3], f_Tb1[2,3]
    f_x2, f_y2, f_z2 = f_Tb2[0,3], f_Tb2[1,3], f_Tb2[2,3]
    f_x3, f_y3, f_z3 = f_Tb3[0,3], f_Tb3[1,3], f_Tb3[2,3]

    i_Tb0 = legtf.create_Tb0(Tm)
    i_t01 = legtf.create_T01(leg.theta1)
    i_t12 = legtf.create_T12(leg.theta2 + np.pi/4)
    i_t23 = legtf.create_T23(leg.theta3 - np.pi/4)
    i_Tb1 = np.matmul(i_Tb0, i_t01)
    i_Tb2 = np.matmul(i_Tb1, i_t12)
    i_Tb3 = np.matmul(i_Tb2, i_t23)
    i_x0, i_y0, i_z0 = i_Tb0[0,3], i_Tb0[1,3], i_Tb0[2,3]
    i_x1, i_y1, i_z1 = i_Tb1[0,3], i_Tb1[1,3], i_Tb1[2,3]
    i_x2, i_y2, i_z2 = i_Tb2[0,3], i_Tb2[1,3], i_Tb2[2,3]
    i_x3, i_y3, i_z3 = i_Tb3[0,3], i_Tb3[1,3], i_Tb3[2,3]

    # Create an empty numpy array to hold scatter points
    points_arr1 = np.empty((0,3))
    points_arr2 = np.empty((0,3))

    # Add scatter points to the array
    points_arr1 = np.append(points_arr1, [[0,0,0], [f_x0, f_y0, f_z0], [f_x1, f_y1, f_z1]], axis=0)
    points_arr1 = np.append(points_arr1, [[f_x2, f_y2, f_z2], [f_x3, f_y3, f_z3]], axis=0)

    points_arr2 = np.append(points_arr2, [[0,0,0], [i_x0, i_y0, i_z0], [i_x1, i_y1, i_z1]], axis=0)
    points_arr2 = np.append(points_arr2, [[i_x2, i_y2, i_z2], [i_x3, i_y3, i_z3]], axis=0)

    plot_points(points_arr1, points_arr2)

if __name__ == '__main__':
    main()