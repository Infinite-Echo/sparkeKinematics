import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib_widget import Matplotlib3DWidget

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Robot Dog Control')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('icon.png'))

        # Load the UI from the .ui file
        uic.loadUi('/home/echo/workspaces/sparkeKinematics/kinematics_gui/mainwindow.ui', self)

        # Get the plot widget and layout from the UI
        plot_widget = Matplotlib3DWidget(self)
        plot_layout = self.findChild(QVBoxLayout, 'plot_layout')
        plot_layout.addWidget(plot_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
