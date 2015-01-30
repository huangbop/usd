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
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.addWidget(self.bg)
        self.bg.setStyleSheet("""
        background-color: yellow;
        """)
        
        # Buttons group
        self.btnsgroup = QWidget(self.parent) # 
        self.btnsgroup.setFixedSize(96, 28)
        grouplayout = QHBoxLayout(self.btnsgroup)
        
        self.btn_close = QPushButton(QIcon("images/close.png"), '', self.btnsgroup)
        self.btn_close.setFlat(True)
        self.btn_min = QPushButton(QIcon("images/min.png"), '', self.btnsgroup)
        self.btn_min.setFlat(True)
        self.btn_setting = QPushButton(QIcon("images/setting.png"), '', self.btnsgroup)
        self.btn_setting.setFlat(True)
        grouplayout.addWidget(self.btn_setting)
        grouplayout.addWidget(self.btn_min)
        grouplayout.addWidget(self.btn_close)

        # Lay buttons group
        bg_hlayout = QHBoxLayout()
        bg_hlayout.addStretch()
        bg_hlayout.addWidget(self.btnsgroup)
        bg_vlayout = QVBoxLayout(self.bg)
        bg_vlayout.setContentsMargins(0, 0, 0, 0)
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

    def raise_minclose(self):
        self.btnsgroup.raise_()
        

class TabsTitle(BaseTitle):
    def __init__(self, parent):
        BaseTitle.__init__(self, parent)

        self.bg = QWidget(self)
        
        self.tabsgroup = QWidget(self.bg)
        self.tab_uart = QPushButton("UART", self.tabsgroup)
        self.tab_gpio = QPushButton("GPIO", self.tabsgroup)
        self.tab_register = QPushButton("REGISTER", self.tabsgroup)
        hlayout = QHBoxLayout(self.tabsgroup)
        hlayout.addWidget(self.tab_uart)
        hlayout.addWidget(self.tab_gpio)
        hlayout.addWidget(self.tab_register)
        self.tabsgroup.setFixedSize(300, 80)
        
        # Lay tabsgroup
        bg_hlayout = QHBoxLayout()
        bg_hlayout.setContentsMargins(0, 0, 0, 0)
        bg_hlayout.addSpacing(30)
        bg_hlayout.addWidget(self.tabsgroup)
        bg_hlayout.addStretch()
        bg_vlayout = QVBoxLayout(self.bg)
        bg_vlayout.setContentsMargins(0, 0, 0, 0)
        bg_vlayout.addSpacing(8)
        bg_vlayout.addLayout(bg_hlayout)
        bg_vlayout.addStretch()

    def resizeEvent(self, event):
        self.bg.resize(event.size())
        self.raise_minclose()
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    title = BaseTitle(None)
    title.setWindowTitle('SSD Uart Diag Tool')
    title.show()
    sys.exit(app.exec_())
