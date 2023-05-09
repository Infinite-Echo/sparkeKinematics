from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTreeView, QApplication, QWidget, QVBoxLayout, QSizePolicy, QMainWindow

class TrajectoryTree(QWidget):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.ui = parent.ui
        # Initialize the model and set the headers for the tree
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Control Points', ''])
        self.tree = QTreeView(self)
        self.tree.setModel(self.model)
        self.tree.setColumnWidth(0, 125)
        self.tree.setColumnWidth(1, 50)

        self.trajectory_enabled = False

        # Add some items to the tree, with the first column unable to be edited
        self.parent_item = self.model.invisibleRootItem()

        self.parent_item.appendRow([self.generate_velocity_item(), self.generate_empty_item()])

        point_items = self.generate_point_items()
        for point in point_items:
            self.parent_item.appendRow([point, self.generate_empty_item()])

        layout = QVBoxLayout(self)
        layout.addWidget(self.tree)

    def generate_velocity_item(self):
        vel_item = QStandardItem('Velocity')
        vel_item.setEditable(False)
        vel_item.appendRow([self.generate_linear_vel_item(), self.generate_empty_item()])
        vel_item.appendRow([self.generate_angular_vel_item(), self.generate_empty_item()])
        return vel_item

    def generate_linear_vel_item(self):
        linear_vel_parent_item = QStandardItem('Position')
        linear_vel_parent_item.setEditable(False)
        linear_vels = ['X', 'Y', 'Z']
        for vel in linear_vels:
            vel_item = QStandardItem(vel)
            vel_item.setEditable(False)
            linear_vel_parent_item.appendRow([vel_item, self.generate_empty_item(True)])
        return linear_vel_parent_item
    
    def generate_angular_vel_item(self):
        angular_vel_parent_item = QStandardItem('Rotation')
        angular_vel_parent_item.setEditable(False)
        angular_vels = ['X\'', 'Y\'', 'Z\'']
        for vel in angular_vels:
            vel_item = QStandardItem(vel)
            vel_item.setEditable(False)
            angular_vel_parent_item.appendRow([vel_item, self.generate_empty_item(True)])
        return angular_vel_parent_item

    def generate_point_items(self):
        points = []
        for i in range(12):
            points.append(f'P{i+1}')
        
        positions = ['X', 'Y', 'Z']
            
        point_items = []
        for point in points:
            pos_parent_item = QStandardItem(point)
            pos_parent_item.setEditable(False)
            for position in positions:
                position_item = QStandardItem(position)
                position_item.setEditable(False)
                pos_parent_item.appendRow([position_item, self.generate_empty_item(True)])
            point_items.append(pos_parent_item)
        return point_items
    
    def generate_empty_item(self, editable = False):
        item = QStandardItem('')
        item.setEditable(editable)
        return item
    
    def get_points(self):
        child = self.parent_item.child(0, 0)
        child = child.child(0,0)
        index = child.index()
        print(index.data())
        

    def toggle_trajectory(self):
        self.trajectory_enabled = not self.trajectory_enabled

        if self.trajectory_enabled:
            self.ui.trajectory_dock_widget.setEnabled(True)
            self.get_points()
        else:
            self.ui.trajectory_dock_widget.setEnabled(False)