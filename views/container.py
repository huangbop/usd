import os
import sys
    
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Container(QTabWidget):
    def __init__(self, parent):
        QTabWidget.__init__(self, parent)

        self.setTabPosition(QTabWidget.South)

        self.uart = QWidget(self)
        self.gpio = QWidget(self)
        self.addTab(self.uart, "uart")
        self.addTab(self.gpio, "gpio")
        
        
        
        

