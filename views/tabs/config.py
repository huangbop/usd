import os
import sys
import random
import string
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from usd.views.ui.Ui_config import Ui_config
from usd.views.setting import tabs_style


class ConfigForm(QWidget, Ui_config):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.setStyleSheet(tabs_style)

        
