from PyQt5 import QtCore, QtGui, QtWidgets


class UiVideoPage(object):
    def setupUi(self, Form):
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 80, 650, 141))
        self.groupBox.setMinimumSize(QtCore.QSize(650, 100))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 551, 41))
        self.lineEdit.setMinimumSize(QtCore.QSize(520, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(30, 90, 150, 23))
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QPushButton(self.groupBox)
        self.toolButton.setGeometry(QtCore.QRect(590, 20, 60, 31))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "      Incarcare video"))
        self.pushButton.setText(_translate("MainWindow", "Incarcare"))
        self.toolButton.setText(_translate("MainWindow", "..."))