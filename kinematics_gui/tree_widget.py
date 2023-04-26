from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTreeView, QApplication, QWidget, QVBoxLayout, QSizePolicy

class EditableTree(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize the model and set the headers for the tree
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Robot', ''])
        self.tree = QTreeView(self)
        self.tree.setModel(self.model)

        # Add some items to the tree, with the first column unable to be edited
        self.parent_item = self.model.invisibleRootItem()

        self.parent_item.appendRow([self.generate_base_item(), self.generate_empty_item()])

        leg_items = self.generate_leg_items()
        for leg in leg_items:
            self.parent_item.appendRow([leg, self.generate_empty_item()])

        layout = QVBoxLayout(self)
        layout.addWidget(self.tree)

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
            joint_item = self.disable_item_editing(joint_item)
            joint_item.appendRow([self.generate_position_item(), self.generate_empty_item()])
            joint_item.appendRow([self.generate_rotation_item(), self.generate_empty_item()])
            joint_items.append(joint_item)
        return joint_items
            
    def generate_position_item(self):
        pos_parent_item = QStandardItem('Position')
        pos_parent_item = self.disable_item_editing(pos_parent_item)
        positions = ['X', 'Y', 'Z']
        for position in positions:
            position_item = QStandardItem(position)
            position_item = self.disable_item_editing(position_item)
            pos_parent_item.appendRow([position_item, self.generate_empty_item()])
        return pos_parent_item
    
    def generate_base_rot_item(self):
        rot_parent_item = QStandardItem('Rotation')
        rot_parent_item = self.disable_item_editing(rot_parent_item)
        rotations = ['X\'', 'Y\'', 'Z\'']
        for rotation in rotations:
            rotation_item = QStandardItem(rotation)
            rotation_item = self.disable_item_editing(rotation_item)
            rot_parent_item.appendRow([rotation_item, self.generate_empty_item()])
        return rot_parent_item
    
    def generate_rotation_item(self):
        rotation_item = QStandardItem('Rotation')
        rotation_item = self.disable_item_editing(rotation_item)
        theta_item = QStandardItem('Theta')
        theta_item = self.disable_item_editing(theta_item)
        rotation_item.appendRow([theta_item, self.generate_empty_item()])
        return rotation_item
    
    def generate_empty_item(self):
        item = QStandardItem('')
        item = self.disable_item_editing(item)
        return item
    
    def disable_item_editing(self, item):
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        return item

    def change_mode(self):
        #toggle editability of joint angles (fk) / pos (ik) 
        pass

if __name__ == '__main__':
    app = QApplication([])
    window = EditableTree()
    app.exec_()
