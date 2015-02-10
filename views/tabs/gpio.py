import os
import sys
import random
import string
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np
import pyqtgraph as pg

from usd.views.ui.Ui_gpio import Ui_gpio
from usd.views.setting import tabs_style
from usd.views.setting import colors


class LedsBar(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.qss = """
        border: 1px solid rgb(208, 208, 208);
        border-radius: 10px;
        background-color: rgb%s;
        """
        self.leds = []
        hlayout = QHBoxLayout(self)
        for i in range(len(colors) - 1):
            tb = QToolButton(self)
            tb.setFixedSize(20, 20)
            tb.setStyleSheet(self.qss % str(colors[-1]))
            hlayout.addWidget(tb)
            self.leds.append(tb)

        self._status = [0 for i in range(len(colors) - 1)]

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, v):
        self._status = v

        for i, s in enumerate(self._status):
            if s:
                self.leds[i].setStyleSheet(self.qss % str(colors[i]))
            else:
                self.leds[i].setStyleSheet(self.qss % str(colors[-1]))


class GpioPlotView(pg.PlotWidget):
    def __init__(self, parent):
        pg.PlotWidget.__init__(self, parent)

        self.curves = []
        self.data = []
        for i, color in enumerate(colors[:-1]):
            curve = self.plot((2 * i, 2 * i), pen=color)
            self.curves.append(curve)
            self.data.append(np.empty(100))
        self.ptr = 0

    def update(self, values):
        for i, dat in enumerate(self.data):
            dat[self.ptr] = values[i] + 2 * i
        self.ptr += 1
        if self.ptr >= self.data[0].shape[0]:
            for i in range(len(self.curves)):
                temp = self.data[i]
                self.data[i] = np.empty(self.data[i].shape[0] * 2)
                self.data[i][:temp.shape[0]] = temp
        for i, curve in enumerate(self.curves):
            curve.setData(self.data[i][:self.ptr])
        
class GpioForm(QWidget, Ui_gpio):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.setStyleSheet(tabs_style)

        # Leds
        self.ledsbar = LedsBar(self.leds_bg)
        ledsbg_hlayout = QHBoxLayout(self.leds_bg)
        ledsbg_hlayout.setContentsMargins(0, 0, 0, 0)
        ledsbg_hlayout.addWidget(self.ledsbar)
        
        # Plot view
        self.plotview = GpioPlotView(self.plot_bg)

        plotbg_hlayout = QHBoxLayout(self.plot_bg)
        plotbg_hlayout.setContentsMargins(0, 0, 0, 0)
        plotbg_hlayout.addWidget(self.plotview)

        # Timer
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.yield_values)

        # Signals
        self.btn_acquire.clicked.connect(self.timer.start)

    def yield_values(self):
        sts = [random.choice([0, 1]) for i in range(8)]
        self.plotview.update(sts)
        self.ledsbar.status = sts
        

