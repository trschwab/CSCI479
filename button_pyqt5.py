import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import bee_track_v1
class App(QWidget):

    beeNumber = 99999999

    def __init__(self):
        super().__init__()
        self.title = 'Insect Tracker App'
        self.left = 250
        self.top = 150
        self.width = 420
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #
        # MY CODE
        #



        #
        #
        #

        run_button = QPushButton('Run Trial', self)
        run_button.setToolTip('Click here to start image processing for a trial')
        run_button.move(150,210)
        run_button.clicked.connect(self.on_click)

        view_button = QPushButton('View Results', self)
        view_button.setToolTip('Click here to see past results of trials')
        view_button.move(150,120)
        view_button.clicked.connect(self.on_click)


        self.show()

    @pyqtSlot()
    def on_click(self):
        beeNumber = self.getInteger()
        bee_track_v1.runTest(beeNumber)

    def getInteger(self):
        i, okPressed = QInputDialog.getInt(self, "Trial ID","Enter Trial ID:", 28, 0, 100, 1)
        if okPressed:
            return i

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
