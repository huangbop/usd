import os
import sys
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)

import usd
from usd.views import setting


class MainForm(QMainWindow):
    """
    """
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.FramelessWindowHint)

        # This bg will all fill the main window's background
        self.bg = QWidget(self)     
        self.setCentralWidget(self.bg)

        bg_vlayout = QVBoxLayout(self.bg)
        bg_vlayout.setContentsMargins(1, 1, 1, 1)
        bg_vlayout.setSpacing(0)

    def resizeEvent(self, event):
        self.setMask(QBitmap("images/main_bg.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/uart.png"))
    form = MainForm()
    form.resize(setting.MAIN_WIDTH, setting.MAIN_HEIGHT)
    form.setWindowTitle('SSD Uart Diag Tool')
    form.show()
    sys.exit(app.exec_())
