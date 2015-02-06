import os
import sys
import random
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from usd.views.ui.Ui_uart import Ui_uart
from usd.views.setting import tabs_style


class UartForm(QWidget, Ui_uart):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.setStyleSheet(tabs_style)

        
    
