import os
import sys
import random

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MotiView(QGraphicsView):
    def __init__(self, parent):
        QGraphicsView.__init__(self, parent)

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        
