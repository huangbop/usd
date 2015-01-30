import os
import sys
    
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class StatusBar(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.bg = QWidget(self)
        vlayout = QVBoxLayout(self)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.addWidget(self.bg)

        self.bg.setObjectName("statusbar")
        self.bg.setStyleSheet("""#statusbar {
        background-color: qlineargradient(spread:pad,
        x1:0, y1:1, x2:0, y2:0,
        stop:0 rgb(208, 208, 208), stop:1 rgb(224, 224, 224));
        }""")

class Container(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.content = QWidget(self)
        
        self.statusbar = StatusBar(self)
        self.statusbar.setFixedHeight(32)

        vlayout = QVBoxLayout(self)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.setSpacing(0)
        vlayout.addWidget(self.content)
        vlayout.addWidget(self.statusbar)

        
