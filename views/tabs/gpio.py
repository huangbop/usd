import os
import sys
import random
import string
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pyqtgraph as pg

from usd.views.ui.Ui_gpio import Ui_gpio
from usd.views.setting import tabs_style


class GpioForm(QWidget, Ui_gpio):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.setStyleSheet(tabs_style)

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
        hlayout = QHBoxLayout(self.plot_bg)
        hlayout.setContentsMargins(0, 0, 0, 0)
        hlayout.addWidget(self.plotview)

    
