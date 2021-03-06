import sys
import os
import threading
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from qt_material import apply_stylesheet
from src.structure import Ui_MainWindow
from src.wellcome_page import UiWellcomePage
from src.image_page import UiImagePage
from src.video_page import UiVideoPage
from src.aux_page import UiAuxPage


# pyuic5 -x resources/ui/test.ui -o test.py


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()

        self.actionExit = self.findChild(QtWidgets.QAction, "actionExit")

        self.image_label = None
        self.button_back = None
        self.detection_info = None
        self.img_graph = None
        self.button_export = None

        wellcome_page = QWidget(self)
        UiWellcomePage().setupUi(wellcome_page, self)

        image_page = QWidget(self)
        UiImagePage().setupUi(image_page, self)

        video_page = QWidget(self)
        UiVideoPage().setupUi(video_page, self)

        aux_page = QWidget(self)
        UiAuxPage().setupUi(aux_page, self)

        pages = {"wellcome_page": wellcome_page,
                 "image_page": image_page,
                 "video_page": video_page,
                 "aux_page": aux_page
                 }
        self.ui.setupUi(self, pages)

        # ____________________PAGES______________________

        # HOME
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.wellcome_page))
        self.ui.btn_home.clicked.connect(lambda: self.activePage(self.ui.btn_home))

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page1))
        self.ui.btn_page_1.clicked.connect(lambda: self.activePage(self.ui.btn_page_1))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page2))
        self.ui.btn_page_2.clicked.connect(lambda: self.activePage(self.ui.btn_page_2))

        # ____________________Show main window______________________
        self.show()

    def activePage(self, btn):
        self.ui.btn_home.setStyleSheet(inactive)
        self.ui.btn_page_1.setStyleSheet(inactive)
        self.ui.btn_page_2.setStyleSheet(inactive)
        if btn == self.ui.btn_home:
            self.ui.btn_home.setStyleSheet(active)
        elif btn == self.ui.btn_page_1:
            self.ui.btn_page_1.setStyleSheet(active)
        elif btn == self.ui.btn_page_2:
            self.ui.btn_page_2.setStyleSheet(active)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'P??r??se??ti aplica??ia?',
                                     'E??ti sigur c?? dore??ti s?? p??r??se??ti aplica??ia?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            # to terminate the thread from video if exists
            self.ui.stackedWidget.setCurrentWidget(self.ui.wellcome_page)
            if not type(event) == bool:
                event.accept()
            else:
                sys.exit()
        else:
            if not type(event) == bool:
                event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_blue.xml")

    # set css
    stylesheet = app.styleSheet()
    with open('resources/css/main.css') as file:
        app.setStyleSheet(stylesheet + file.read().format(**os.environ))
    with open('resources/css/active.css') as file:
        active = file.read().format(**os.environ)
    with open('resources/css/inactive.css') as file:
        inactive = file.read().format(**os.environ)

    window = MainWindow()

    sys.exit(app.exec_())
