from kinematics_np.sparke_base_IK import SparkeBase
from kinematics_np.sparke_leg_IK import SparkeLeg
from kinematics_np import base_transformations as basetf
from kinematics_np import leg_transformations as legtf
from PyQt5.QtWidgets import QTreeView, QApplication, QWidget, QVBoxLayout, QSizePolicy, QMainWindow
import numpy as np
from mainwindow import Ui_MainWindow

class kinematicsController():
    def __init__(self, parent: QMainWindow):
        self.ui = parent.ui
        self.sparke_legs = []
        for leg in range(4):
            self.sparke_legs.append(SparkeLeg(leg))

    def home(self):
        self.Tm = basetf.create_base_transformation(0, 0, 0, 0, 0, 0)
        for leg in self.sparke_legs:
            leg.update_Tb0(self.Tm)
        
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
        self.ui.tree_layout