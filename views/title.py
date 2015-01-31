import os
import sys
import random
    
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TabsTitle(QWidget):
    def __init__(self, mainform):
        QWidget.__init__(self, mainform)
        self.mainform = mainform

        self.bg = QWidget(self)
        vlayout = QVBoxLayout(self)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.addWidget(self.bg)
        self.bg.setObjectName('tabstitle')
        self.bg.setStyleSheet("""#tabstitle {
        background-color: qlineargradient(spread:pad,
        x1:0, y1:1, x2:0, y2:0,
        stop:0 rgb(208, 208, 208), stop:1 rgb(224, 224, 224));
        }""")

        # Buttons group
        self.btnsgroup = QWidget(self.bg)
        #self.btnsgroup.setStyleSheet("background-color: red")
        btns_layout = QHBoxLayout(self.btnsgroup)
        btns_layout.setContentsMargins(0, 0, 10, 50)
        self.btn_close = QToolButton(self.btnsgroup)
        self.btn_close.setFixedSize(QSize(24, 24))
        self.btn_close.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.btn_close.setIcon(QIcon("images/close.png"))
        self.btn_close.setIconSize(QSize(24, 24))
        self.btn_min = QToolButton(self.btnsgroup)
        self.btn_min.setFixedSize(QSize(24, 24))
        self.btn_min.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.btn_min.setIcon(QIcon("images/min.png"))
        self.btn_min.setIconSize(QSize(24, 24))
        self.btn_setting = QToolButton(self.btnsgroup)
        self.btn_setting.setFixedSize(QSize(28, 28))
        self.btn_setting.setAutoRaise(True)
        self.btn_setting.setIcon(QIcon("images/setting.png"))
        self.btn_setting.setIconSize(QSize(24, 24))
        self.btn_setting.setPopupMode(QToolButton.MenuButtonPopup)
        self.btn_setting.setToolButtonStyle(Qt.ToolButtonIconOnly)
        btns_layout.addWidget(self.btn_setting)
        btns_layout.addWidget(self.btn_min)
        btns_layout.addWidget(self.btn_close)

        # Tabs group
        self.tabsgroup = QWidget(self.bg)
        tabs_layout = QHBoxLayout(self.tabsgroup)
        tabs_layout.setContentsMargins(0, 16, 0, 0)
        self.tab_uart = QToolButton(self.tabsgroup)
        self.tab_uart.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.tab_uart.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.tab_uart.setIcon(QIcon("images/uart.png"))
        self.tab_uart.setIconSize(QSize(48, 48))
        self.tab_uart.setFixedSize(QSize(70, 70))
        self.tab_uart.setText("UART")
        self.tab_gpio = QToolButton(self.tabsgroup)
        self.tab_gpio.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.tab_gpio.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.tab_gpio.setIcon(QIcon("images/gpio.png"))
        self.tab_gpio.setIconSize(QSize(48, 48))
        self.tab_gpio.setFixedSize(QSize(70, 70))
        self.tab_gpio.setText("GPIO")
        tabs_layout.addWidget(self.tab_uart)
        tabs_layout.addWidget(self.tab_gpio)
        tabs_layout.addStretch()
        self.tabsgroup.setStyleSheet("""
        color: rgb(80, 80, 80);
        font: 8pt "verdana";
        """)
        
        # Lay out all components
        self.layout_all()

        # Drive the main form
        self.start_moving = False
        self.start_x = self.start_y = 0
        self.btn_close.clicked.connect(self.mainform.close)
        self.btn_min.clicked.connect(self.mainform.showMinimized)

        # Tabs signal map
        self.tabs_signalmapper = QSignalMapper()
        self.tabs_signalmapper.setMapping(self.tab_uart, 0)
        self.tabs_signalmapper.setMapping(self.tab_gpio, 1)
        self.tab_uart.clicked.connect(self.tabs_signalmapper.map)
        self.tab_gpio.clicked.connect(self.tabs_signalmapper.map)
        
    def layout_all(self):
        bg_hlayout = QHBoxLayout(self.bg)
        bg_hlayout.setContentsMargins(0, 0, 0, 0)
        bg_hlayout.addSpacing(100)
        bg_hlayout.addWidget(self.tabsgroup)
        bg_hlayout.addWidget(self.btnsgroup)

    def mousePressEvent(self, event):
        self.start_moving = True
        self.start_x = event.x()
        self.start_y = event.y()

    def mouseReleaseEvent(self, event):
        self.start_moving = False

    def mouseMoveEvent(self, event):
        if self.start_moving:
            self.mainform.move(event.globalX() - self.start_x, event.globalY() - self.start_y)

