import os
import sys
import random
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from usd.views.ui.Ui_status import Ui_status
from usd.views.setting import status_style


class StatusForm(QWidget, Ui_status):
    def __init__(self, mainform):
        QWidget.__init__(self, mainform)
        self.mainform = mainform
        self.setupUi(self)

        self.setStyleSheet(status_style)

                
