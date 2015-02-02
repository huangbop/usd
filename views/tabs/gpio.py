import os
import sys
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pyqtgraph as pg


class GpioForm(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.bg = QWidget(self)
        vlayout = QVBoxLayout(self)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.addWidget(self.bg)
        self.bg.setStyleSheet("""
        background-color: white;
        """)

        self.plotview = pg.PlotWidget(self.bg)
        self.plotview.setStyleSheet("""
        border-radius: 6px;
        """)
        
        bg_hlayout = QHBoxLayout(self.bg)
        bg_hlayout.setContentsMargins(15, 10, 150, 10)
        bg_hlayout.addWidget(self.plotview)



        
        


