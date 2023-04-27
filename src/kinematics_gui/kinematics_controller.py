from sparke_kinematics import base_transformations as basetf
from sparke_kinematics import leg_transformations as legtf
# from sparke_kinematics.sparke_base_IK import SparkeBase
from sparke_kinematics.sparke_leg_IK import SparkeLeg
from PyQt5.QtWidgets import QTreeView, QApplication, QWidget, QVBoxLayout, QSizePolicy, QMainWindow
import numpy as np
from mainwindow import Ui_MainWindow
from kinematics_controller_utils import *
import time
class kinematicsController():
    def __init__(self, parent: QMainWindow, model):
        kinematicsController.LEG_DICT = {
            0: 'Front Left',
            1: 'Front Right',
            2: 'Back Left',
            3: 'Back Right',
        }
        self.ui = parent.ui
        self.model = model
        self.sparke_legs = []
        for leg in range(1, 5):
            self.sparke_legs.append(SparkeLeg(leg))
        self.home()
        print(self.sparke_legs[0].t_b0)
        self.sparke_legs[0].solve_angles(self.Tm, 0.10807106781186548, 0.11, -0.18384776310850237)
        print(round(np.degrees(self.sparke_legs[0].theta2)))
        set_positions(self.model, 'Base', [0, 0, 0])
        set_positions(self.model, 'Front Left', [0, 1, 0], 'Shoulder')
        set_positions(self.model, 'Front Left', [1, 0, 0], 'Leg')
        set_positions(self.model, 'Front Left', [0, 0, 1], 'Wrist')
        print(get_positions(self.model, 'Base'))
        print(get_positions(self.model, 'Front Left', 'Shoulder'))
        print(get_positions(self.model, 'Front Left', 'Leg'))
        print(get_positions(self.model, 'Front Left', 'Wrist'))
        set_positions(self.model, 'Base', [0.101, 0.055, 0])
        print(get_positions(self.model, 'Base'))
        set_base_rotations(self.model, [0, 15, 0])
        print(get_base_rotations(self.model))

    def home(self):
        self.Tm = basetf.create_base_transformation(0, 0, 0, 0, 0, 0)
        for i in range(4):
            self.sparke_legs[i].update_Tb0(self.Tm)
            set_positions(self.model, kinematicsController.LEG_DICT[i], [0,0,0], 'Shoulder')
            set_positions(self.model, kinematicsController.LEG_DICT[i], [0,0,0], 'Leg')
            set_positions(self.model, kinematicsController.LEG_DICT[i], [0,0,0], 'Wrist')

        
    def solve_ik(self):
        #store current angles and positions
        #try:
        # solve
        #except:
        # restore original values
        pass
        #grab positions from ui

    def solve_fk(self):
        #store current angles and positions
        #try:
        # solve
        #except:
        # restore original values
        pass
        #grab angles from ui and convert to rads

    def update_Tm(self):
        pass