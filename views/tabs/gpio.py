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

        self.plotwidget = pg.PlotWidget(self.bg)
        self.plotitem = self.plotwidget.getPlotItem()
        self.plotitem.setClipToView(True)
        self.plotitem.setXRange(0, 100)
        self.plotitem.setLabel("bottom", "Time", "s")

        bg_hlayout = QHBoxLayout(self.bg)
        bg_hlayout.setContentsMargins(15, 10, 150, 10)
        bg_hlayout.addWidget(self.plotwidget)

        # Timer Plot
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(100)

        self.data = []
        self.curves = []
        for i in range(8):
            d = np.empty((100, 2), int)
            self.data.append(d)
            curve = self.plotitem.plot(pen=(255, 0, 0))
            self.curves.append(curve)
            
        
    def update_plot(self):
        for i in range(8):
            self.data[i][:,0] = range(100)
            self.data[i][:,1] = np.random.randint(0, 2, 100) + i * 2
            self.curves[i].setData(self.data[i], pen=(i * 20, 255, 0))
