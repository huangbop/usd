import os
import sys
import random
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from usd.views.ui.Ui_title import Ui_title
from usd.views.setting import title_style


class TitleForm(QWidget, Ui_title):
    def __init__(self, mainform):
        QWidget.__init__(self, mainform)
        self.mainform = mainform
        self.setupUi(self)

        # Drive the main form
        self.start_moving = False
        self.start_x = self.start_y = 0
        self.btn_close.clicked.connect(self.mainform.close)
        self.btn_min.clicked.connect(self.mainform.showMinimized)

        # Set stylesheet
        self.setStyleSheet(title_style)

    def mousePressEvent(self, event):
        self.start_moving = True
        self.start_x = event.x()
        self.start_y = event.y()

    def mouseReleaseEvent(self, event):
        self.start_moving = False

    def mouseMoveEvent(self, event):
        if self.start_moving:
            self.mainform.move(event.globalX() - self.start_x, event.globalY() - self.start_y)

