import os
import sys
    
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class UartForm(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.bg = QWidget(self)
        vlayout = QVBoxLayout(self)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.addWidget(self.bg)
        self.bg.setObjectName("uartform_bg")
        self.bg.setStyleSheet("#uartform_bg {background-color: white;}")

        # Left text browser
        self.text_browser = QTextBrowser(self.bg)
        self.text_browser.setFrameShape(QFrame.NoFrame)
        self.text_browser.setStyleSheet("""
        background-color: qlineargradient(spread:pad,
        x1:0, y1:1, x2:0, y2:0,
        stop:0 rgb(208, 208, 208), stop:1 rgb(224, 224, 224));
        border-radius: 6px;
        """)

        browser_vlayout = QVBoxLayout(self.text_browser)
        browser_vlayout.addWidget(self.text_browser)

        # Right buttons
        self.btnsgroup = QWidget(self.bg)
        #self.btnsgroup.setFixedWidth(100)
        btnsgroup_vlayout = QVBoxLayout(self.btnsgroup)
        self.btn_startstop = QToolButton(self.btnsgroup)
        self.btn_startstop.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.btn_startstop.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.btn_startstop.setIcon(QIcon("images/start.png"))
        self.btn_startstop.setIconSize(QSize(48, 48))
        self.btn_startstop.setFixedSize(QSize(70, 70))
        self.btn_startstop.setText("START")
        btnsgroup_vlayout.addSpacing(30)
        btnsgroup_vlayout.addWidget(self.btn_startstop)
        btnsgroup_vlayout.addStretch()
        self.btnsgroup.setStyleSheet("""
        color: rgb(80, 80, 80);
        font: 8pt "verdana";
        """)
        
        # Lay out components
        bg_hlayout = QHBoxLayout(self.bg)
        bg_hlayout.setContentsMargins(15, 10, 10, 10)
        bg_hlayout.addWidget(self.text_browser)
        bg_hlayout.addWidget(self.btnsgroup)
        
        
        # Connect signals
        self.btn_startstop.clicked.connect(self.startstop_clicked)
        

    def startstop_clicked(self):
        if self.btn_startstop.text() == "START":
            self.btn_startstop.setText("STOP")
            self.btn_startstop.setIcon(QIcon("images/stop.png"))
        else:
            self.btn_startstop.setText("START")
            self.btn_startstop.setIcon(QIcon("images/start.png"))


