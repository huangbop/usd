import os
import sys
import random
import string
    
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from usd.views.ui.Ui_register import Ui_register_
from usd.views.setting import tabs_style


class CellWidget(QLineEdit):
    def __init__(self, row, col, parent):
        QLineEdit.__init__(self, parent)

        self.validators = [
            QRegExpValidator(QRegExp(r'0[xX][0-9]+')),
            QRegExpValidator(QRegExp(r'')),
            QRegExpValidator(QRegExp(r'')),
            QRegExpValidator(QRegExp(r'')),
        ]

        self.setValidator(self.validators[col])        
    


class RegTable(QTableWidget):
    def __init__(self, parent):
        QTableWidget.__init__(self, 0, 4, parent)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.horizontalHeader().setResizeMode(3, QHeaderView.Stretch)
        self.horizontalHeader().resizeSection(0, 160)
        self.horizontalHeader().resizeSection(1, 160)
        self.horizontalHeader().resizeSection(2, 160)
    
        self.headers = ('Address', 'Hex', 'Dec', 'Bin')
        self.setHorizontalHeaderLabels(self.headers)

    def add_row(self):
        row = self.rowCount()
        self.insertRow(row)
        for i in range(len(self.headers)):
            self.setItem(row, i, QTableWidgetItem())
            self.setCellWidget(row, i, CellWidget(row, i, self))

    def del_row(self):
        row_set = set()
        for item in self.selectedItems():
            row_set.add(item.row())
        for r in reversed(list(row_set)):
            self.removeRow(r)

    def load_rows(self):
        pass

    
                
        


class RegisterForm(QWidget, Ui_register_):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.setStyleSheet(tabs_style)

        self.table = RegTable(self)

        tablebg_hlayout = QHBoxLayout(self.table_bg)
        tablebg_hlayout.setContentsMargins(0, 0, 0, 0)
        tablebg_hlayout.addWidget(self.table)


        self.btn_add.clicked.connect(self.table.add_row)
        self.btn_del.clicked.connect(self.table.del_row)
        self.btn_load.clicked.connect(self.table.load_rows)
