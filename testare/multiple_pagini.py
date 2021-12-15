from random import randint
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui  import QIcon
from PyQt5.QtWidgets import (QWidget, QListWidget, QStackedWidget, 
                             QHBoxLayout, QListWidgetItem, QLabel)
from qt_material import apply_stylesheet

class LeftTabWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(LeftTabWidget, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        # Left and right layout (one QListWidget on the left + QStackedWidget on the right)
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        # List on the left
        self.listWidget = QListWidget(self)
        layout.addWidget(self.listWidget)
        # Cascading window on the right
        self.stackedWidget = QStackedWidget(self)
        layout.addWidget(self.stackedWidget)

        self.initUi()

    def initUi(self):
        # Initialization interface
        # Switch the sequence number in QStackedWidget by the current item change of QListWidget
        self.listWidget.currentRowChanged.connect(
            self.stackedWidget.setCurrentIndex)
        # Remove the border
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        # Hide scroll bar
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Here we use the general text with the icon mode (you can also use Icon mode, setViewMode directly)
        for i in range(5):
            item = QListWidgetItem(
                QIcon('Ok.png'), str('Option %s' % i), self.listWidget)
            # Set the default width and height of the item (only height is useful here)
            item.setSizeHint(QSize(16777215, 60))
            # Text centered
            item.setTextAlignment(Qt.AlignCenter)

        # Simulate 5 right-side pages (it won't loop with the top)
        for i in range(5):
            label = QLabel('This is the page %d' % i, self)
            label.setAlignment(Qt.AlignCenter)
            # Set the background color of the label (randomly here)
            # Added a margin margin here (to easily distinguish between QStackedWidget and QLabel colors)
            label.setStyleSheet('background: rgb(%d, %d, %d); margin: 50px;' % (
                randint(0, 255), randint(0, 255), randint(0, 255)))
            self.stackedWidget.addWidget(label)


# style sheet
Stylesheet = """
QListWidget, QListView, QTreeWidget, QTreeView {
    outline: 0px;
}
QListWidget {
    min-width: 120px;
    max-width: 120px;
    color: white;
    background: black;
}
QListWidget::item:selected {
    background: rgb(52, 52, 52);
    border-left: 2px solid rgb(9, 187, 7);
}
HistoryPanel::item:hover {background: rgb(52, 52, 52);}
QStackedWidget {background: rgb(30, 30, 30);}
QLabel {color: white;}
"""

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    app.setStyleSheet(Stylesheet)

    # setup stylesheet
    apply_stylesheet(app, theme='dark_teal.xml')
    w = LeftTabWidget()
    w.show()
    sys.exit(app.exec_())