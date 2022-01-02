from PyQt5 import QtCore, QtGui, QtWidgets

# Image page UI
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
import cv2


class UiImagePage(object):

    def setupUi(self, Form, root):
        def openImage():
            def convert_cv_qt(cv_img):
                """Convert from an opencv image to QPixmap"""
                rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
                p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
                return QPixmap.fromImage(p)

            root.ui.stackedWidget.setCurrentWidget(root.ui.auxiliar_page)

            file = self.lineEdit_5.text()

            self.disply_width = 640
            self.display_height = 480
            # create the label that holds the image
            self.image_label = QtWidgets.QLabel()
            self.image_label.resize(self.disply_width, self.display_height)
            self.layout = QtWidgets.QVBoxLayout(root.ui.auxiliar_page)
            self.layout.addWidget(self.image_label)

            img = cv2.imread(file)

            self.image_label.setPixmap(convert_cv_qt(img))

        def openFileDialog():
            file, check = QFileDialog.getOpenFileName(None, "Select image", "",
                                                      "JPG image (*.jpg);;JPEG image (*.jpeg);;PNG image (*.png)")
            if check:
                self.lineEdit_5.setText(file)
                self.pushButton_10.setEnabled(True)
            else:
                self.lineEdit_5.setText("Alege alta imagine ...")

        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMinimumSize(QtCore.QSize(700, 100))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 250))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 60, 581, 41))
        self.lineEdit_5.setMinimumSize(QtCore.QSize(520, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setFrame(True)
        self.lineEdit_5.setDragEnabled(False)
        self.lineEdit_5.setClearButtonEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(20, 200, 601, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(20, 30, 601, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setGeometry(QtCore.QRect(620, 60, 61, 41))
        self.pushButton_11.setObjectName("pushButton_11")
        # open file dialog
        self.pushButton_11.clicked.connect(openFileDialog)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setEnabled(False)
        self.pushButton_10.setGeometry(QtCore.QRect(570, 130, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        # open image
        self.pushButton_10.clicked.connect(openImage)
        self.horizontalLayout.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(43, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "   Alege o imagine ..."))
        self.label_11.setText(_translate("Form", "* Extensii acceptate: JPG, JPEG, PNG"))
        self.label_10.setText(_translate("Form", "Încarcă o imagine"))
        self.pushButton_11.setToolTip(_translate("Form", "<html><head/><body><p>Alege o imagine</p></body></html>"))
        self.pushButton_11.setText(_translate("Form", "..."))
        self.pushButton_10.setText(_translate("Form", "Încarcă"))
