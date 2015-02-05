import os
import sys
import random
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from usd.views.ui import Ui_title


class TabsTitle(QWidget):
    def __init__(self, mainform):
        QWidget.__init__(self, mainform)
        self.mainform = mainform


        # Drive the main form
        self.start_moving = False
        self.start_x = self.start_y = 0
        self.btn_close.clicked.connect(self.mainform.close)
        self.btn_min.clicked.connect(self.mainform.showMinimized)


    def mousePressEvent(self, event):
        self.start_moving = True
        self.start_x = event.x()
        self.start_y = event.y()

    def mouseReleaseEvent(self, event):
        self.start_moving = False

    def mouseMoveEvent(self, event):
        if self.start_moving:
            self.mainform.move(event.globalX() - self.start_x, event.globalY() - self.start_y)

