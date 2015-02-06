import os
import sys
import random
import string
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from usd.views.ui.Ui_uart import Ui_uart
from usd.views.setting import tabs_style


class PrintThread(QThread):

    yield_text = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while True:
            self.yield_text.emit(''.join(random.sample(string.printable, 90)))
            self.msleep(100)


class UartForm(QWidget, Ui_uart):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.setStyleSheet(tabs_style)

        self.log.setReadOnly(False)
        self.log.setMaximumBlockCount(5000)

        # Connect signals
        self.btn_startstop.clicked.connect(self.startstop_clicked)

        # Print thread
        self.print_thread = PrintThread()
        self.print_thread.yield_text.connect(self.do_print)

    def startstop_clicked(self):
        if self.btn_startstop.text() == "Start":
            if not self.print_thread.isRunning():
                self.print_thread.start()
            self.btn_startstop.setText("Stop")
        else:
            if self.print_thread.isRunning():
                self.print_thread.terminate()
            self.btn_startstop.setText("Start")

    def do_print(self, str):
        self.log.appendPlainText(str)
        self.log.verticalScrollBar().setSliderPosition(
            self.log.verticalScrollBar().maximum())
        
