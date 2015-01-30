import os
import sys
import random
    
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class BaseTitle(QWidget):
    """
    """
    def __init__(self, parent):
        QWidget.__init__(self, parent) # Need parent
        self.parent = parent

        # Always fills a background widget
        self.bg = QWidget(self)
        vlayout = QVBoxLayout(self)
        vlayout.addWidget(self.bg)
        
        # Buttons group
        self.btnsgroup = QWidget(self.bg)
        self.btnsgroup.setFixedSize(96, 32)
        self.btnsgroup.setStyleSheet("background-color: rgb(192, 192, 192)")
        grouplayout = QHBoxLayout(self.btnsgroup)
        self.btn_close = QPushButton(QIcon("images/close.png"), '', self.btnsgroup)
        self.btn_close.setIconSize(QSize(16, 16))
        self.btn_close.setFlat(True)
        self.btn_min = QPushButton(QIcon("images/min.png"), '', self.btnsgroup)
        self.btn_min.setIconSize(QSize(16, 16))
        self.btn_min.setFlat(True)
        self.btn_setting = QPushButton(QIcon("images/setting.png"), '', self.btnsgroup)
        self.btn_setting.setIconSize(QSize(16, 16))
        self.btn_setting.setFlat(True)
        grouplayout.addWidget(self.btn_setting)
        grouplayout.addWidget(self.btn_min)
        grouplayout.addWidget(self.btn_close)

        # Lay buttons group
        bg_hlayout = QHBoxLayout()
        bg_hlayout.addStretch()
        bg_hlayout.addWidget(self.btnsgroup)
        bg_vlayout = QVBoxLayout(self.bg)
        bg_vlayout.addLayout(bg_hlayout)
        bg_vlayout.addStretch()

        # Set bg widget sytle
        self.bg.setObjectName('basetitle')
        self.bg.setStyleSheet("""#basetitle {
        background-color: qlineargradient(spread:pad,
        x1:0, y1:1, x2:0, y2:0,
        stop:0 rgb(208, 208, 208), stop:1 rgb(224, 224, 224));
        }""")

        self.start_move = False
        self.start_x = self.start_y = 0

        # Signals
        self.btn_close.clicked.connect(self.parent.close)
        self.btn_min.clicked.connect(self.parent.showMinimized)

    def mousePressEvent(self, event):
        self.start_move = True
        self.start_x = event.x() + 10 
        self.start_y = event.y() + 10

    def mouseReleaseEvent(self, event):
        self.start_move = False

    def mouseMoveEvent(self, event):
        if self.start_move:
            self.parent.move(event.globalX() - self.start_x, event.globalY() - self.start_y)


class TabsTitle(BaseTitle):
    def __init__(self, parent):
        BaseTitle.__init__(self, parent)

        self.tabsgroup = QWidget(self)
        hlayout = QHBoxLayout(self.tabsgroup)

        self.tab_uart = QPushButton(QIcon("images/close.png"), "", self.tabsgroup)
        #self.tab_uart.setFixedSize(64, 64)
        self.tab_gpio = QPushButton(QIcon("images/close.png"), "", self.tabsgroup)
        #self.tab_gpio.setFixedSize(64, 64)
        hlayout.addWidget(self.tab_uart)
        hlayout.addWidget(self.tab_gpio)
        self.tabsgroup.setGeometry(0, 20, 100, 80)
        self.tabsgroup.setStyleSheet("""
        background-image: url(images/close.png);
                                     """)
    
        
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    title = BaseTitle(None)
    title.setWindowTitle('SSD Uart Diag Tool')
    title.show()
    sys.exit(app.exec_())
