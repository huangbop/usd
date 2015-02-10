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

        # Scene & tabs
        self.scene = QWidget(self)
                
        self.config_form = ConfigForm(self)
        self.uart_form = UartForm(self)
        self.gpio_form = GpioForm(self)
        self.register_form = RegisterForm(self)

        self.tabs = [self.config_form, self.uart_form, self.gpio_form,
                     self.register_form] 

        # Status
        self.status = StatusForm(self)
        self.status.setFixedHeight(30)
        
        bg_vlayout.addWidget(self.title)
        bg_vlayout.addWidget(self.scene)
        bg_vlayout.addWidget(self.status)

        # Connect tabs clicked signal & slot
        self.title.tabs_signalmapper.mapped.connect(self.check_tab)

        # Mask bitmap
        self.mask_map = QBitmap(":/images/images/main_bg.png")

    def check_tab(self, id_):
        self.tabs[id_].raise_()
        
    def resizeEvent(self, event):
        self.setMask(self.mask_map)

        for tab in self.tabs:
            tab.setGeometry(self.scene.geometry())
        self.tabs[0].raise_()
        
    def closeEvent(self, event):
        event.accept()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/images/images/uart.png"))
    form = MainForm()
    form.resize(setting.MAIN_WIDTH, setting.MAIN_HEIGHT)
    form.setWindowTitle('SSD Uart Diag Tool')
    form.show()
    sys.exit(app.exec_())
