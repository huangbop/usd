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

        # The QGraphicsProxyWidget tab list
        self.tabs = []

    def addTab(self, widget):
        """
        Add the tab widget to the main scene
        """
        tab = self.scene.addWidget(widget)
        self.tabs.append(tab)


    def resizeEvent(self, event):
        size = event.size()     # QSize
        w = size.width()
        h = size.height()
        self.scene.setSceneRect(0, 0, w, h)
        for tab in self.tabs:
            tab.setGeometry(QRectF(0, 0, w, h))
        
        
