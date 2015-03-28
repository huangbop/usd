import os
import sys
import random
import string
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from serial.serialwin32 import Win32Serial 
from serial.tools.list_ports import comports
import re

from usd.views.ui.Ui_uart import Ui_uart
from usd.views.setting import tabs_style


class PrintThread(QThread):

    yield_text = pyqtSignal(str)

    def __init__(self, serial):
        QThread.__init__(self)
        self.serial = serial

    def run(self):
        if not self.serial.isOpen():
            return
        while True:
            self.yield_text.emit(self.serial.read().decode())


class UartForm(QWidget, Ui_uart):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.setStyleSheet(tabs_style)

        self.log.setReadOnly(True)
        self.log.setMaximumBlockCount(5000)

        # Connect signals
        self.btn_startstop.clicked.connect(self.startstop_clicked)

        # Enum serial devices
        self.serial = Win32Serial(baudrate=115200)
        self.serial_devices = sorted(comports())
        print(self.serial_devices)

        # Print thread
        self.print_thread = PrintThread(self.serial)
        self.print_thread.yield_text.connect(self.do_print)

    def startstop_clicked(self):
        if self.btn_startstop.text() == "Start":
            matched = False
            for port, desc, hwid in sorted(comports()):
                if re.match(r'PORTS\\VID_04B4&PID_0005.*&01', hwid):
                    matched = True
                    break
            if not matched:
                QMessageBox.information(None, "Warning",
                                        "No uart-diagnose board found.")
            else:
                self.serial.setPort(port)
                if not self.serial.isOpen():
                    self.serial.open()

                if not self.print_thread.isRunning():
                    self.print_thread.start()
                    self.btn_startstop.setText("Stop")

        else:
            if self.print_thread.isRunning():
                self.print_thread.terminate()
            self.serial.close()
            self.btn_startstop.setText("Start")

    def do_print(self, str):
        self.log.insertPlainText(str)
        self.log.verticalScrollBar().setSliderPosition(
            self.log.verticalScrollBar().maximum())
