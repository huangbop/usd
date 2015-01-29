import os
import sys
    
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class BaseTitle(QWidget):
    """
    """
    def __init__(self, parent):
        QWidget.__init__(self, parent) # Need parent

        # Always fills a background widget
        self.bg = QWidget(self)
        vlayout = QVBoxLayout(self)
        vlayout.addWidget(self.bg)
        
        # Buttons group
        self.btnsgroup = QWidget(self.bg)
        self.btnsgroup.setFixedSize(96, 32)
        grouplayout = QHBoxLayout(self.btnsgroup)
        self.btn_close = QPushButton('X', self.btnsgroup)
        self.btn_close.setFlat(True)
        self.btn_min = QPushButton('-', self.btnsgroup)
        self.btn_min.setFlat(True)
        self.btn_setting = QPushButton('V', self.btnsgroup)
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
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    title = BaseTitle(None)
    title.setWindowTitle('SSD Uart Diag Tool')
    title.show()
    sys.exit(app.exec_())
