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

        # Tabs signal map
        self.tabs = [self.tab_config, self.tab_uart,
                     self.tab_gpio, self.tab_register]

        self.tabs_signalmapper = QSignalMapper()
        self.tabs_signalmapper.setMapping(self.tab_config, 0)
        self.tabs_signalmapper.setMapping(self.tab_uart, 1)
        self.tabs_signalmapper.setMapping(self.tab_gpio, 2)
        self.tabs_signalmapper.setMapping(self.tab_register, 3)
        self.tab_config.clicked.connect(self.tabs_signalmapper.map)
        self.tab_uart.clicked.connect(self.tabs_signalmapper.map)
        self.tab_gpio.clicked.connect(self.tabs_signalmapper.map)
        self.tab_register.clicked.connect(self.tabs_signalmapper.map)
        self.tab_uart
        
        self.tab_clicked(0)

        # Connect tabs clicked signal & slot
        self.tabs_signalmapper.mapped.connect(self.tab_clicked)

    def tab_clicked(self, ix):
        for tab in self.tabs:
            tab.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.tabs[ix].setStyleSheet("""
        border: none;
        border-radius: 6px;
        background-color: qlineargradient(spread:pad,
        x1:0, y1:1, x2:0, y2:0,
        stop:0 rgb(208, 208, 208), stop:1 rgb(176, 176, 176)); 
        """)
        
    def mousePressEvent(self, event):
        self.start_moving = True
        self.start_x = event.x()
        self.start_y = event.y()

    def mouseReleaseEvent(self, event):
        self.start_moving = False

    def mouseMoveEvent(self, event):
        if self.start_moving:
            self.mainform.move(event.globalX() - self.start_x, event.globalY() - self.start_y)

