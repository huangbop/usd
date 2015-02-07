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
from usd.views.tabs.config import ConfigForm
from usd.views.tabs.uart import UartForm
from usd.views.tabs.gpio import GpioForm
from usd.views.tabs.register import RegisterForm


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

        # Tab forms
        self.config_form = ConfigForm(None) # Must toplevel widget
        self.moti.addTab(self.config_form)
        
        self.uart_form = UartForm(None) # Must toplevel widget
        self.moti.addTab(self.uart_form)
        
        self.gpio_form = GpioForm(None) # Must toplevel widget
        self.moti.addTab(self.gpio_form)
        
        self.register_form = RegisterForm(None) # Must toplevel widget
        self.moti.addTab(self.register_form)

        # Status
        self.status = StatusForm(self)
        self.status.setFixedHeight(30)
        
        bg_vlayout.addWidget(self.title)
        bg_vlayout.addWidget(self.moti)
        bg_vlayout.addWidget(self.status)

        # Connect tabs clicked signal & slot
        self.title.tabs_signalmapper.mapped.connect(self.moti.showTab)

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
