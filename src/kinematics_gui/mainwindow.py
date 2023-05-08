# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(991, 629)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(903, 594))
        MainWindow.setAcceptDrops(False)
        MainWindow.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 480))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.plot_dock_widget = QtWidgets.QDockWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_dock_widget.sizePolicy().hasHeightForWidth())
        self.plot_dock_widget.setSizePolicy(sizePolicy)
        self.plot_dock_widget.setMinimumSize(QtCore.QSize(480, 240))
        self.plot_dock_widget.setMaximumSize(QtCore.QSize(799, 524287))
        self.plot_dock_widget.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.plot_dock_widget.setAllowedAreas(QtCore.Qt.NoDockWidgetArea)
        self.plot_dock_widget.setObjectName("plot_dock_widget")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.plot_layout = QtWidgets.QVBoxLayout()
        self.plot_layout.setObjectName("plot_layout")
        self.gridLayout_6.addLayout(self.plot_layout, 0, 0, 1, 1)
        self.plot_dock_widget.setWidget(self.dockWidgetContents_3)
        self.gridLayout_5.addWidget(self.plot_dock_widget, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5.addWidget(self.frame_2, 0, 2, 2, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5.addWidget(self.frame_3, 0, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 991, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuMode = QtWidgets.QMenu(self.menuOptions)
        self.menuMode.setObjectName("menuMode")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuVisibility = QtWidgets.QMenu(self.menuView)
        self.menuVisibility.setObjectName("menuVisibility")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.tree_dock_widget = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_dock_widget.sizePolicy().hasHeightForWidth())
        self.tree_dock_widget.setSizePolicy(sizePolicy)
        self.tree_dock_widget.setAutoFillBackground(False)
        self.tree_dock_widget.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.tree_dock_widget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.TopDockWidgetArea)
        self.tree_dock_widget.setObjectName("tree_dock_widget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.kinematics_tree_layout = QtWidgets.QGridLayout()
        self.kinematics_tree_layout.setObjectName("kinematics_tree_layout")
        self.gridLayout_2.addLayout(self.kinematics_tree_layout, 0, 0, 1, 1)
        self.tree_dock_widget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.tree_dock_widget)
        self.trajectory_dock_widget = QtWidgets.QDockWidget(MainWindow)
        self.trajectory_dock_widget.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trajectory_dock_widget.sizePolicy().hasHeightForWidth())
        self.trajectory_dock_widget.setSizePolicy(sizePolicy)
        self.trajectory_dock_widget.setMinimumSize(QtCore.QSize(127, 380))
        self.trajectory_dock_widget.setMaximumSize(QtCore.QSize(300, 600))
        self.trajectory_dock_widget.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.trajectory_dock_widget.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.RightDockWidgetArea|QtCore.Qt.TopDockWidgetArea)
        self.trajectory_dock_widget.setObjectName("trajectory_dock_widget")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.trajectory_tree_layout = QtWidgets.QGridLayout()
        self.trajectory_tree_layout.setSpacing(0)
        self.trajectory_tree_layout.setObjectName("trajectory_tree_layout")
        self.gridLayout_3.addLayout(self.trajectory_tree_layout, 0, 0, 1, 1)
        self.trajectory_dock_widget.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.trajectory_dock_widget)
        self.control_dock_widget = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.control_dock_widget.sizePolicy().hasHeightForWidth())
        self.control_dock_widget.setSizePolicy(sizePolicy)
        self.control_dock_widget.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.control_dock_widget.setObjectName("control_dock_widget")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_4.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_4.setSizePolicy(sizePolicy)
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents_4)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.trajectory_toggle_button = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.trajectory_toggle_button.setObjectName("trajectory_toggle_button")
        self.gridLayout.addWidget(self.trajectory_toggle_button, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.control_dock_widget.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.control_dock_widget)
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionForward_Kinematics = QtWidgets.QAction(MainWindow)
        self.actionForward_Kinematics.setCheckable(True)
        self.actionForward_Kinematics.setChecked(True)
        self.actionForward_Kinematics.setObjectName("actionForward_Kinematics")
        self.actionInverse_Kinematics = QtWidgets.QAction(MainWindow)
        self.actionInverse_Kinematics.setCheckable(True)
        self.actionInverse_Kinematics.setObjectName("actionInverse_Kinematics")
        self.actionHome_Position = QtWidgets.QAction(MainWindow)
        self.actionHome_Position.setCheckable(True)
        self.actionHome_Position.setObjectName("actionHome_Position")
        self.actionKinematics = QtWidgets.QAction(MainWindow)
        self.actionKinematics.setCheckable(True)
        self.actionKinematics.setObjectName("actionKinematics")
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addAction(self.actionExport)
        self.menuMode.addAction(self.actionForward_Kinematics)
        self.menuMode.addAction(self.actionInverse_Kinematics)
        self.menuOptions.addAction(self.menuMode.menuAction())
        self.menuVisibility.addAction(self.actionHome_Position)
        self.menuVisibility.addAction(self.actionKinematics)
        self.menuView.addAction(self.menuVisibility.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sparke Kinematics Previewer"))
        self.plot_dock_widget.setWindowTitle(_translate("MainWindow", "3D Plot"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuMode.setTitle(_translate("MainWindow", "Mode"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuVisibility.setTitle(_translate("MainWindow", "Visibility"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.tree_dock_widget.setWindowTitle(_translate("MainWindow", "Robot Tree"))
        self.trajectory_dock_widget.setWindowTitle(_translate("MainWindow", "Trajectory"))
        self.control_dock_widget.setWindowTitle(_translate("MainWindow", "Control"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.trajectory_toggle_button.setText(_translate("MainWindow", "Toggle Trajectory"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionForward_Kinematics.setText(_translate("MainWindow", "Forward Kinematics"))
        self.actionInverse_Kinematics.setText(_translate("MainWindow", "Inverse Kinematics"))
        self.actionHome_Position.setText(_translate("MainWindow", "Home Position"))
        self.actionKinematics.setText(_translate("MainWindow", "Kinematics"))
