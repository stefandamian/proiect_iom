import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(100,100,200,50)
   b.move(50,20)
   w.setWindowTitle("PyQt5")
   w.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   window()

   # Utile
   # se instealeaza Qt Designer oriunde si cand se realieaza un UI se salveaza in resources/ui/... apoi se foloseste:
   # comanda pt transformat din ui in py este: pyuic5 -x resources/ui/test.ui -o test.py
   # cand instalam un packet punem si versiunea in requirements.txt
   # structura de proiect:
            # https://stackoverflow.com/questions/3495703/how-to-organize-gui-code-for-a-pyqt-project