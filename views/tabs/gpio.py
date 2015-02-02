import os
import sys
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class GpioForm(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.bg = QWidget(self)
        vlayout = QVBoxLayout(self)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.addWidget(self.bg)
        self.bg.setStyleSheet("background-color: blue")




        
        


