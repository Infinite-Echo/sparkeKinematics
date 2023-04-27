import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTreeWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QModelIndex
from mainwindow import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib_widget import Matplotlib3DWidget
from tree_widget import EditableTree
from kinematics_controller import kinematicsController

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Robot Dog Control')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('icon.png'))

        # Set up the UI from the converted Python module
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Get the plot widget and layout from the UI
        plot_widget = Matplotlib3DWidget(self)
        self.plot_layout = self.ui.plot_layout
        self.plot_layout.addWidget(plot_widget)

        tree_widget = EditableTree(self)
        self.tree_layout = self.ui.tree_layout
        self.tree_layout.addWidget(tree_widget)
        model = tree_widget.tree.model()
        
        ctrlr = kinematicsController(self, model)
        # print(model.rowCount())
        # base_index = model.index(0,0,QModelIndex())
        # print(base_index.data())
        # base_model = base_index.model()
        # base_model.setData(base_index, 'Hello')
        # print(base_index.data())


        # controller = kinematicsController(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
