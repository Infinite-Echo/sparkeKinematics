import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTreeWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QModelIndex, pyqtSignal, QModelIndex
from mainwindow import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib_widget import Matplotlib3DWidget
from kinematics_tree_widget import KinematicsTree
from trajectory_tree_widget import TrajectoryTree
from kinematics_controller import kinematicsController

class App(QMainWindow):
    data_changed_signal = pyqtSignal(QModelIndex, QModelIndex)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Robot Dog Control')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('icon.png'))

        # Set up the UI from the converted Python module
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Get the plot widget and layout from the UI
        self.plot_widget = Matplotlib3DWidget(self)
        self.plot_layout = self.ui.plot_layout
        self.plot_layout.addWidget(self.plot_widget)

        self.kinematics_tree_widget = KinematicsTree(self)
        self.kinematics_tree_layout = self.ui.kinematics_tree_layout
        self.kinematics_tree_layout.addWidget(self.kinematics_tree_widget)
        kinematics_model = self.kinematics_tree_widget.tree.model()

        self.trajectory_tree_widget = TrajectoryTree(self)
        self.trajectory_tree_layout = self.ui.trajectory_tree_layout
        self.trajectory_tree_layout.addWidget(self.trajectory_tree_widget)
        
        self.controller = kinematicsController(self, kinematics_model, self.plot_widget)
        # Connect the dataChanged signal to the controller's slot
        self.data_changed_signal.connect(self.controller.data_changed)
        self.ui.actionReset.triggered.connect(self.controller.home)
        self.ui.toggle_trajectory_button.pressed.connect(self.toggle_trajectory_clicked)
        self.ui.toggle_labels_button.pressed.connect(self.plot_widget.toggle_labels)
        self.ui.clear_trajectory_plot_button.pressed.connect(self.plot_widget.clear_points)
        self.ui.reset_trajectory_button.pressed.connect(self.trajectory_tree_widget.reset_trajectory)
        self.ui.reset_vel_button.pressed.connect(self.trajectory_tree_widget.reset_velocity)
        self.ui.plot_trajectory_button.pressed.connect(self.trajectory_tree_widget.plot_trajectory)

        # Emit the signal when the model's data changes
        kinematics_model.dataChanged.connect(lambda i1, i2: self.data_changed_signal.emit(i1, i2))

    def toggle_trajectory_clicked(self):
        self.trajectory_tree_widget.toggle_trajectory()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
