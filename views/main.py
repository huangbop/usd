import os
import sys
    
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)

import usd
from usd.views import setting
from usd.views.title import BaseTitle, TabsTitle
from usd.views.container import Container
        

class MainForm(QMainWindow):
    """
    """
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.FramelessWindowHint)

        # This bg will all fill the main window's background
        self.bg = QWidget(self)
        self.setCentralWidget(self.bg)
        self.bg.setObjectName("mainform_bg")
        self.bg.setStyleSheet("""
        #mainform_bg {
        background-color: rgb(208, 208, 208);
        }
        """)

        self.title = TabsTitle(self) # Drive the main window
        self.title.setFixedHeight(96)
        
        self.content = Container(self.bg)
        self.content.setBaseSize(100, 100)
        #self.content.setStyleSheet("background-color: red")

        bg_vlayout = QVBoxLayout(self.bg)
        bg_vlayout.setContentsMargins(1, 1, 1, 1)
        bg_vlayout.setSpacing(0)
        bg_vlayout.addWidget(self.title)
        bg_vlayout.addWidget(self.content)

    def resizeEvent(self, event):
        self.setMask(QBitmap("images/main_bg.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.resize(setting.MAIN_WIDTH, setting.MAIN_HEIGHT)
    form.setWindowTitle('SSD Uart Diag Tool')
    form.show()
    sys.exit(app.exec_())

