import os
import threading
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from src.vehicle_count import from_static_video


# Video page UI
class UiVideoPage(object):
    def setupUi(self, Form, root):
        def openVideo():
            file = self.lineEdit_5.text()
            if (os.path.isfile(file)):
                # sets image
                root.ui.stackedWidget.setCurrentWidget(root.ui.aux_page)

                q = []
                t = threading.Thread(name='video_process', target=from_static_video,
                                     args=(file, root.image_label, root.detection_info, root.img_graph, root, q))
                t.start()

                root.button_back.clicked.connect(lambda: root.ui.stackedWidget.setCurrentWidget(root.ui.page2))
                root.button_export.clicked.connect(lambda: exportResults(root, q, file))
                root.button_back.setText("Alt videoclip")
            else:
                QMessageBox.about(root, "A apărut o eroare", "Videoclipul ales nu există")

            self.pushButton_10.setEnabled(False)
            self.lineEdit_5.setText("")

        def openFileDialog():
            file, check = QFileDialog.getOpenFileName(None, "Select video", "",
                                                      "Mp4 video (*.mp4);;Avi video (*.avi)")
            if check:
                self.lineEdit_5.setText(file)
                self.pushButton_10.setEnabled(True)
            else:
                self.lineEdit_5.setText("Alege alt videoclip ...")

        def exportResults(root, q, file):
            info = q[-1]

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

            total = info[0] + info[1] + info[2] + info[3] + info[4] + info[5]
            results = 'Pentru fisierul: ' + file + '\n\n'
            if total != 0:
                results += 'S-au detectat ' + str(total) + ' participanti la trafic: \n\n'
                if info[0] != 0:
                    results += 'Persoane - ' + str(info[0]) + '\n'
                if info[1] != 0:
                    results += 'Biciclete - ' + str(info[1]) + '\n'
                if info[2] != 0:
                    results += 'Masini - ' + str(info[2]) + '\n'
                if info[3] != 0:
                    results += 'Motociclete - ' + str(info[3]) + '\n'
                if info[4] != 0:
                    results += 'Autobuze - ' + str(info[4]) + '\n'
                if info[5] != 0:
                    results += 'Camioane - ' + str(info[5]) + '\n'
            else:
                results += 'Nu s-a detectat niciun participant la trafic: \n\n'

            results += '\nSalvat la data de: ' + dt_string

            S__File_V = QFileDialog.getSaveFileName(None, 'SaveTextFile', '/', "Text Files (*.txt)")

            if S__File_V[0]:
                try:
                    with open(S__File_V[0], 'w') as file:
                        file.write(results)
                        QMessageBox.about(root, "Succes", "Datele au fost salvate cu succes.")
                        root.button_export.clicked.disconnect()
                except BaseException as error:
                    print('An exception occurred: {}'.format(error))
                    QMessageBox.about(root, "Eroare", "A apărut o eroare. Incearcă din nou.")

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
