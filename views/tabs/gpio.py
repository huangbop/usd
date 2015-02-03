import os
import sys
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pyqtgraph as pg
import numpy as np


class GpioForm(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.bg = QWidget(self)
        vlayout = QVBoxLayout(self)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.addWidget(self.bg)
        self.bg.setObjectName("gpioform_bg")
        self.bg.setStyleSheet("""
        #gpioform_bg {
        background-color: qlineargradient(spread:pad,
        x1:0, y1:1, x2:0, y2:0,
        stop:0 rgb(224, 224, 224), stop:1 rgb(240, 240, 240));
        }
        """)

        self.plotview = pg.PlotWidget(self.bg)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.plotview.setStyleSheet("""
        border-radius: 6px;
        """)
        
        bg_hlayout = QHBoxLayout(self.bg)
        bg_hlayout.setContentsMargins(15, 10, 150, 10)
        bg_hlayout.addWidget(self.plotview)

        # Plot
        x = np.arange(100)
        y = np.random.normal(size=(3, 100))
        for i in range(3):
            self.plotview.plot(x, y[i], pen=(i, 3))

