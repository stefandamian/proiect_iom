from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QFileDialog, QPushButton, QWidget, QVBoxLayout


# Video page UI
class UiVideoPage(object):
    def setupUi(self, Form, root):
        def openVideo():
            self.groupBox.setHidden(True)
            file = self.lineEdit_5.text()



        def openFileDialog():
            file, check = QFileDialog.getOpenFileName(None, "Select video", "",
                                                      "Mp4 video (*.mp4);;Avi video (*.avi)")
            if check:
                self.lineEdit_5.setText(file)
                self.pushButton_10.setEnabled(True)
            else:
                self.lineEdit_5.setText("Alege alt videoclip ...")

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
        # open my thing
        self.pushButton_10.clicked.connect(openVideo)
        self.pushButton_10.setGeometry(QtCore.QRect(570, 130, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
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
        self.lineEdit_5.setPlaceholderText(_translate("Form", "   Alege un videoclip ..."))
        self.label_11.setText(_translate("Form", "* Extensii acceptate: MP4, avi"))
        self.label_10.setText(_translate("Form", "Încarcă un videoclip"))
        self.pushButton_11.setToolTip(_translate("Form", "<html><head/><body><p>Alege o imagine</p></body></html>"))
        self.pushButton_11.setText(_translate("Form", "..."))
        self.pushButton_10.setText(_translate("Form", "Încarcă"))