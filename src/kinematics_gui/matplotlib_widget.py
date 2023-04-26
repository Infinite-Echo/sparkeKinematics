import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Matplotlib3DWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.updateGeometry()
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)
        self.button_pressed = False
        self.start_x = None
        self.start_y = None
        self.start_rotation = None
        self.canvas.mpl_connect('button_press_event', self.on_button_press)
        self.canvas.mpl_connect('motion_notify_event', self.on_motion_notify)
        self.canvas.mpl_connect('button_release_event', self.on_button_release)

    def on_button_press(self, event):
        if event.button == Qt.LeftButton:
            self.button_pressed = True
            self.start_x = event.x
            self.start_y = event.y
            self.start_rotation = self.ax.azim, self.ax.elev

    def on_motion_notify(self, event):
        if self.button_pressed:
            dx = event.x - self.start_x
            dy = -(event.y - self.start_y)  # invert the y direction
            rotation = self.start_rotation[1] + dy/2, self.start_rotation[0] - dx/2
            self.ax.view_init(*rotation)
            self.canvas.draw()

    def on_button_release(self, event):
        if event.button == Qt.LeftButton:
            self.button_pressed = False