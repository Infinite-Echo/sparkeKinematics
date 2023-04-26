from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTreeView, QApplication, QWidget, QVBoxLayout, QSizePolicy, QMainWindow
from kinematics_np.sparke_base_IK import SparkeBase
from mainwindow import Ui_MainWindow

class EditableTree(QWidget):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.ui = parent.ui
        # Initialize the model and set the headers for the tree
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Robot', ''])
        self.tree = QTreeView(self)
        self.tree.setModel(self.model)
        self.mode = 'fk'

        # Add some items to the tree, with the first column unable to be edited
        self.parent_item = self.model.invisibleRootItem()

        self.parent_item.appendRow([self.generate_base_item(), self.generate_empty_item()])

        leg_items = self.generate_leg_items()
        for leg in leg_items:
            self.parent_item.appendRow([leg, self.generate_empty_item()])

        layout = QVBoxLayout(self)
        layout.addWidget(self.tree)
        self.ui.actionForward_Kinematics.triggered.connect(self.toggle_ik)
        self.ui.actionInverse_Kinematics.triggered.connect(self.toggle_fk)

    def generate_base_item(self):
        base_item = QStandardItem('Base')
        base_item.setEditable(False)
        base_item.appendRow([self.generate_position_item(), self.generate_empty_item()])
        base_item.appendRow([self.generate_base_rot_item(), self.generate_empty_item()])
        return base_item
    
    def generate_leg_items(self):
        legs = ['Front Left', 'Front Right', 'Back Left', 'Back Right']
        leg_items = []
        for leg in legs:
            leg_item = QStandardItem(leg)
            leg_item.setEditable(False)
            joint_items = self.generate_joint_items()
            for joint in joint_items:
                leg_item.appendRow([joint, self.generate_empty_item()])
            leg_items.append(leg_item)
        return leg_items

    def generate_joint_items(self):
        joints = ['Shoulder', 'Leg', 'Wrist']
        joint_items = []
        for joint in joints:
            joint_item = QStandardItem(joint)
            joint_item.setEditable(False)
            joint_item.appendRow([self.generate_position_item(), self.generate_empty_item()])
            joint_item.appendRow([self.generate_rotation_item(), self.generate_empty_item()])
            joint_items.append(joint_item)
        return joint_items
            
    def generate_position_item(self):
        pos_parent_item = QStandardItem('Position')
        pos_parent_item.setEditable(False)
        positions = ['X', 'Y', 'Z']
        for position in positions:
            position_item = QStandardItem(position)
            position_item.setEditable(False)
            pos_parent_item.appendRow([position_item, self.generate_empty_item()])
        return pos_parent_item
    
    def generate_base_rot_item(self):
        rot_parent_item = QStandardItem('Rotation')
        rot_parent_item.setEditable(False)
        rotations = ['Roll', 'Pitch', 'Yaw']
        for rotation in rotations:
            rotation_item = QStandardItem(rotation)
            rotation_item.setEditable(False)
            rot_parent_item.appendRow([rotation_item, self.generate_empty_item(True)])
        return rot_parent_item
    
    def generate_rotation_item(self):
        rotation_item = QStandardItem('Rotation')
        rotation_item.setEditable(False)
        theta_item = QStandardItem('Theta')
        theta_item.setEditable(False)
        rotation_item.appendRow([theta_item, self.generate_empty_item()])
        return rotation_item
    
    def generate_empty_item(self, editable = False):
        item = QStandardItem('')
        item.setEditable(editable)
        return item

    def update_mode(self):
        #toggle editability of joint angles (fk) / pos (ik) 
        if self.ui.actionForward_Kinematics.isChecked()==True and self.ui.actionInverse_Kinematics.isChecked()==False:
            self.mode = 'fk'
            self.activate_fk_mode()
        elif self.ui.actionForward_Kinematics.isChecked()==False and self.ui.actionInverse_Kinematics.isChecked()==True:
            self.mode = 'ik'
            self.activate_ik_mode()
        
    def toggle_fk(self):
        self.ui.actionForward_Kinematics.toggle()
        self.update_mode()

    def toggle_ik(self):
        self.ui.actionInverse_Kinematics.toggle()
        self.update_mode()

    def activate_ik_mode(self):
        pass

    def activate_fk_mode(self):
        pass

if __name__ == '__main__':
    app = QApplication([])
    window = EditableTree()
    app.exec_()
