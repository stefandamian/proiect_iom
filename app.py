import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from qt_material import apply_stylesheet
from src.structure import Ui_MainWindow
from src.wellcome_page import UiWellcomePage
from src.image_page import UiImagePage
from src.video_page import UiVideoPage


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()

        wellcome_page = QtWidgets.QWidget()
        UiWellcomePage().setupUi(wellcome_page)

        image_page = QtWidgets.QWidget()
        UiImagePage().setupUi(image_page)

        video_page = QtWidgets.QWidget()
        UiVideoPage().setupUi(video_page)

        pages = {"wellcome_page": wellcome_page,
                 "image_page": image_page,
                 "video_page": video_page
                 }
        self.ui.setupUi(self, pages)

        # ____________________PAGES______________________

        # HOME
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.wellcome_page))

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page1))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page2))

        # ____________________Show main window______________________
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_blue.xml")

    # stylesheet = app.styleSheet()
    # with open('custom.css') as file:
    #     app.setStyleSheet(stylesheet + file.read().format(**os.environ))

    window = MainWindow()
    sys.exit(app.exec_())

