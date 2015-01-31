import os
import sys
    
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from usd.views.tabs.uart import UartForm
from usd.views.tabs.gpio import GpioForm


class StatusBar(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.bg = QWidget(self)
        vlayout = QVBoxLayout(self)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.addWidget(self.bg)

        self.bg.setObjectName("statusbar")
        self.bg.setStyleSheet("""#statusbar {
        background-color: qlineargradient(spread:pad,
        x1:0, y1:1, x2:0, y2:0,
        stop:0 rgb(208, 208, 208), stop:1 rgb(224, 224, 224));
        }""")

class Container(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.stage = QWidget(self)
        self.stage.setObjectName("stage")
        self.stage.setStyleSheet("""
        #stage {
        background-color: white;
        }
        """)
        
        self.statusbar = StatusBar(self)
        self.statusbar.setFixedHeight(32)

        vlayout = QVBoxLayout(self)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.setSpacing(0)
        vlayout.addWidget(self.stage)
        vlayout.addWidget(self.statusbar)

        # Forms in stage
        self.forms = []
        self.uart_form = UartForm(self.stage)
        self.gpio_form = GpioForm(self.stage)
        self.forms.append(self.uart_form)
        self.forms.append(self.gpio_form)

    def show_tab(self, checked_id):
        self.forms[checked_id].raise_()
            
    def resizeEvent(self, event):
        g = self.stage.geometry()
        for form in self.forms:
            form.setGeometry(g)
            
        
