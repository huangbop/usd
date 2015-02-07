import os
import sys
import random
import string
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from usd.views.ui.Ui_gpio import Ui_gpio
from usd.views.setting import tabs_style


class GpioForm(QWidget, Ui_gpio):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.setStyleSheet(tabs_style)

        
