import os
import sys
import random
import string
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from usd.views.ui.Ui_register import Ui_register_
from usd.views.setting import tabs_style


class RegisterForm(QWidget, Ui_register_):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.setStyleSheet(tabs_style)

        
