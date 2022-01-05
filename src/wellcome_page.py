from PyQt5 import QtCore, QtGui, QtWidgets

# Set stylesheet
inactive = """
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


# Wellcome page UI
class UiWellcomePage(object):
    def setupUi(self, Form, root):
        Form.setObjectName("Form")
        Form.resize(851, 808)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(700, 100))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 713))
        self.widget.setObjectName("widget")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 120, 621, 351))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(40, 490, 621, 101))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 30, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(270, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.widget)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(43, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        self.pushButton.clicked.connect(lambda: root.ui.stackedWidget.setCurrentWidget(root.ui.page1))
        self.pushButton.clicked.connect(lambda: self.activePage('img', root))

        self.pushButton_2.clicked.connect(lambda: root.ui.stackedWidget.setCurrentWidget(root.ui.page2))
        self.pushButton_2.clicked.connect(lambda: self.activePage('video', root))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#448aff;\">Detecția participanților la trafic</span></p>\n"
                                            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; font-weight:600; color:#448aff;\"><br /></p>\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">    </span><span style=\" color:#ffffff;\">Scopul aplicației este de a detecta participanții la trafic dintr-o imagine sau dintr-un videoclip.</span></p>\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">    </span></p>\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">    În urma detecției, poți vizualiza rezultatele inclusiv grafic. De asemenea, în cazul detecției dintr-un videoclip, rezultatele le vei putea vizualiza în timp real.</span></p>\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">    </span></p>\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">    Instrucțiuni de utilizare a aplicației:</span></p>\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">    - folosește meniul din stânga pentru a alege încărca un videoclip/imagine</span></p>\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">    - alege un videoclip/imagine din calculator</span></p>\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">    - apasă pe &quot;Încarcă imagine/videoclip&quot;</span></p>\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">    - vizualizează rezultatele</span></p>\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">    </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#448aff;\">© 2022, Enrico Gărăiman &amp; Ștefan Damian</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "Detecție din imagine"))
        self.label.setText(_translate("Form", "SAU"))
        self.pushButton.setText(_translate("Form", "Detecție din imagine"))

    def activePage(self, btn, root):
        root.ui.btn_home.setStyleSheet(inactive)
        root.ui.btn_page_1.setStyleSheet(inactive)
        root.ui.btn_page_2.setStyleSheet(inactive)
        if btn == 'img':
            root.ui.btn_page_1.setStyleSheet(active)
        elif btn == 'video':
            root.ui.btn_page_2.setStyleSheet(active)
