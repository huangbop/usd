import os
import sys
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pyqtgraph as pg
import numpy as np
from numpy import random

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

        self.plot_widget = pg.PlotWidget(self.bg)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.plot_widget.setStyleSheet("""
        border-radius: 6px;
        """)
        
        bg_hlayout = QHBoxLayout(self.bg)
        bg_hlayout.setContentsMargins(15, 10, 150, 10)
        bg_hlayout.addWidget(self.plot_widget)

        # Timer Plot
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(100)

        self.data = random.randint(0, 2, 20)
        
    def update_plot(self):
        self.data[:-1] = self.data[1:]
        self.data[-1] = random.randint(0, 2)
        self.plot_widget.plot(self.data, clear=True)
        
