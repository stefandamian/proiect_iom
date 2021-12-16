from PyQt5 import QtCore, QtGui, QtWidgets

# Wellcome page UI
class UiWellcomePage(object):
    def setupUi(self, widget):
        widget.setEnabled(True)
        widget.setObjectName("wellcome_page")
        self.label_2 = QtWidgets.QLabel(widget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #FFF;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.w_page_verticalLayout = QtWidgets.QVBoxLayout(widget)
        self.w_page_verticalLayout.setObjectName("w_page_verticalLayout")
        self.w_page_verticalLayout.addWidget(self.label_2)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("MainWindow", "Home"))
