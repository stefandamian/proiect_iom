# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/structure.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

# Set stylesheet
stylesheet = """
    QPushButton {
        color: rgb(255, 255, 255);
        background-color: rgb(35, 35, 35);
        border: 0px solid;
        height: 60px;
        margin: 10px 0;
        padding: 10px 0;
    }
    QPushButton:hover {
        background-color: rgb(85, 170, 255);
    }
"""

active = """
    QPushButton {
        color: rgb(255, 255, 255);
        margin: 10px 0;
        padding: 10px 0;
        border: 0px solid;
        height: 60px;
        background-color: rgb(85, 170, 255);
    }
"""

# Structure for project
class Ui_MainWindow(object):
    def setupUi(self, MainWindow, pages):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 500)
        MainWindow.setMinimumSize(QtCore.QSize(950, 400))
        MainWindow.showMaximized()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(140, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(0, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)

        # btn Home
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_home = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_home.setFont(font)
        self.btn_home.setStyleSheet(stylesheet)
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout_4.addWidget(self.btn_home)

        # btn Imagine
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_page_1 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_1.setFont(font)
        self.btn_page_1.setStyleSheet(stylesheet)
        self.btn_page_1.setObjectName("btn_page_1")
        self.verticalLayout_4.addWidget(self.btn_page_1)

        #btn Video
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_page_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_2.setFont(font)
        self.btn_page_2.setStyleSheet(stylesheet)
        self.btn_page_2.setObjectName("btn_page_2")
        self.verticalLayout_4.addWidget(self.btn_page_2)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")

        #PAGE 1
        self.page1 = pages["image_page"]

        #PAGE 2
        self.page2 = pages["video_page"]

        #PAGE wellcome
        self.wellcome_page = pages["wellcome_page"]

        #auxiliar page
        self.aux_page = pages["aux_page"]

        # Add pages in layout
        self.stackedWidget.addWidget(self.page1)
        self.stackedWidget.addWidget(self.page2)
        self.stackedWidget.addWidget(self.wellcome_page)
        self.stackedWidget.addWidget(self.aux_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.btn_home.setStyleSheet(active)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Detecția participanților la trafic | Proiect IOM 2022"))
        self.btn_page_1.setText(_translate("MainWindow", "Imagine"))
        self.btn_page_2.setText(_translate("MainWindow", "Videoclip"))
        self.btn_home.setText(_translate("MainWindow", "Acasă"))

