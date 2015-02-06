import os
import sys
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)

import usd
from usd.views import setting
from usd.views.title import TitleForm
from usd.views.status import StatusForm
from usd.views.moti import MotiView


class MainForm(QMainWindow):
    """
    """
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.FramelessWindowHint)

        # This bg will all fill the main window's background
        self.bg = QWidget(self)     
        self.setCentralWidget(self.bg)
        self.bg.setObjectName("main_bg")
        self.bg.setStyleSheet("""
        #main_bg {
        background-color: rgb(208, 208, 208);
        }
        """)

        bg_vlayout = QVBoxLayout(self.bg)
        bg_vlayout.setContentsMargins(1, 1, 1, 1)
        bg_vlayout.setSpacing(0)

        # Title
        self.title = TitleForm(self)
        self.title.setFixedHeight(90)

        # Moti
        self.moti = MotiView(self)
        self.moti.setFrameShape(QFrame.NoFrame)
        
        # Status
        self.status = StatusForm(self)
        self.status.setFixedHeight(30)
        
        bg_vlayout.addWidget(self.title)
        bg_vlayout.addWidget(self.moti)
        bg_vlayout.addWidget(self.status)

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
