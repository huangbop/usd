import os
import sys
import random
import string
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pyqtgraph as pg

from usd.views.ui.Ui_gpio import Ui_gpio
from usd.views.setting import tabs_style
from usd.views.setting import colors


class LedsView(QGraphicsView):
    def __init__(self, parent):
        QGraphicsView.__init__(self, parent)

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self._status = 0

        self.brushes = [QBrush(QColor(c[0], c[1], c[2], c[3])) for c in colors]
        self.leds = []
        for i in range(len(self.brushes) - 1):
            led = self.scene.addEllipse(0, 0, 2, 2, QPen(QColor(176, 176, 176, 255)),
                                        self.brushes[-1])
            self.leds.append(led)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, values):
        d = len(values) - len(self.leds)
        if d > 0:
            values = values[:-d]
        for i, v in enumerate(values):
            self.leds[i].setBrush(self.brushes[i] if v else self.brushes[-1])        

    def resizeEvent(self, event):
        size = event.size()     # QSize
        w = size.width()
        h = size.height()
        self.scene.setSceneRect(0, 0, w, h)
        # Lay out leds
        deltax = w / len(self.leds)
        for i, led in enumerate(self.leds):
            led.setRect(i*deltax + deltax/2, 0, h, h)

        self.status = (0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0)

class GpioForm(QWidget, Ui_gpio):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.setStyleSheet(tabs_style)

        # Leds
        self.ledsview = LedsView(self.leds_bg)
        self.ledsview.setStyleSheet("""
        border: none;
        """)
        ledsbg_hlayout = QHBoxLayout(self.leds_bg)
        ledsbg_hlayout.setContentsMargins(0, 0, 0, 0)
        ledsbg_hlayout.addWidget(self.ledsview)
        
        # Plot view
        self.plotview = pg.PlotWidget(self.plot_bg)
        self.plotview.setStyleSheet("""
        background-color: red;
        border-radius: 10px;
        """)

        self.plot_bg.setStyleSheet("""
        background-color: red;
        border-radius: 10px;
        """)
        plotbg_hlayout = QHBoxLayout(self.plot_bg)
        plotbg_hlayout.setContentsMargins(0, 0, 0, 0)
        plotbg_hlayout.addWidget(self.plotview)

    
