from sparke_kinematics import base_transformations as basetf
from sparke_kinematics import leg_transformations as legtf
# from sparke_kinematics.sparke_base_IK import SparkeBase
from sparke_kinematics.sparke_leg_IK import SparkeLeg
from PyQt5.QtWidgets import QTreeView, QApplication, QWidget, QVBoxLayout, QSizePolicy, QMainWindow
import numpy as np
from mainwindow import Ui_MainWindow
from kinematics_controller_utils import *
import forward_kinematics_utils as fk_utils
import time
import copy
class kinematicsController():
    def __init__(self, parent: QMainWindow, model):
        kinematicsController.LEG_DICT = {
            0: 'Front Left',
            1: 'Front Right',
            2: 'Back Left',
            3: 'Back Right',
        }
        kinematicsController.JOINT_DICT = {
            0: 'Shoulder',
            1: 'Leg',
            2: 'Wrist',
        }
        kinematicsController.HOME_POSITIONS = [
            [1, 12, 0], #FL Shoulder
            [2, 11, 1], #FL Leg
            [3, 10, 0], #FL Wrist
            [4, 9, 1], #FR Shoulder
            [5, 8, 0], #FR Leg
            [6, 7, 1], #FR Wrist
            [7, 6, 0], #BL Shoulder
            [8, 5, 1], #BL Leg
            [9, 4, 0], #BL Wrist
            [10, 3, 1], #BR Shoulder
            [11, 2, 0], #BR Leg
            [12, 1, 1], #BR Wrist
        ]
        self.current_positions = copy.deepcopy(kinematicsController.HOME_POSITIONS)
        self.ui = parent.ui
        self.model = model
        self.sparke_legs = []
        for leg in range(1, 5):
            self.sparke_legs.append(SparkeLeg(leg))
        self.home()
        # print(self.sparke_legs[0].t_b0)
        # self.sparke_legs[0].solve_angles(self.Tm, 0.10807106781186548, 0.11, -0.18384776310850237)
        # print(round(np.degrees(self.sparke_legs[0].theta2)))
        # set_positions(self.model, 'Base', [0, 0, 0])
        # set_positions(self.model, 'Front Left', [0, 1, 0], 'Shoulder')
        # set_positions(self.model, 'Front Left', [1, 0, 0], 'Leg')
        # set_positions(self.model, 'Front Left', [0, 0, 1], 'Wrist')
        # print(get_positions(self.model, 'Base'))
        # print(get_positions(self.model, 'Front Left', 'Shoulder'))
        # print(get_positions(self.model, 'Front Left', 'Leg'))
        # print(get_positions(self.model, 'Front Left', 'Wrist'))
        # set_positions(self.model, 'Base', [0.101, 0.055, 0])
        # print(get_positions(self.model, 'Base'))
        # set_base_rotations(self.model, [0, 15, 0])
        # print(get_base_rotations(self.model))

    def home(self):
        self.Tm = basetf.create_base_transformation(0, 0, 0, 0, 0, 0)
        for i in range(4):
            self.sparke_legs[i].update_Tb0(self.Tm)
            set_positions(self.model, kinematicsController.LEG_DICT[i], kinematicsController.HOME_POSITIONS[3*i], kinematicsController.JOINT_DICT[0])
            set_positions(self.model, kinematicsController.LEG_DICT[i], kinematicsController.HOME_POSITIONS[(3*i)+1], kinematicsController.JOINT_DICT[1])
            set_positions(self.model, kinematicsController.LEG_DICT[i], kinematicsController.HOME_POSITIONS[(3*i)+2], kinematicsController.JOINT_DICT[2])
        
    def solve_ik(self):
        #store current angles and positions
        #try:
        # solve
        #except:
        # restore original values
        pass
        #grab positions from ui

    def solve_fk(self):
        try:
            self.update_Tm()
            angles = self.get_angles_from_tree()
            for i in range(4):
                positions = fk_utils.get_leg_positions(self.sparke_legs[i], self.Tm, angles[i])
                for j in range(4):
                    
                
                


                    
        except:
            pass
        #store current angles and positions
        #try:
        # solve
        #except:
        # restore original values
        pass
        #grab angles from ui and convert to rads

    def update_Tm(self):
        base_positions = get_positions(self.model, 'Base')
        base_rotations = get_base_rotations(self.model)
        self.Tm = basetf.create_base_transformation(base_positions[0], base_positions[1], base_positions[2], \
                                                     base_rotations[0], base_rotations[1], base_rotations[2])

    def get_angles_from_tree(self):
        angles = []
        for i in range(4):
            for j in range(3):
                angles.append(get_joint_angle(self.model, kinematicsController.LEG_DICT[i], kinematicsController.JOINT_DICT[j]))
        return angles