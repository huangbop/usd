# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\hb\projects\usd\views\ui\uart.ui'
#
# Created: Fri Feb  6 16:08:39 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_uart(object):
    def setupUi(self, uart):
        uart.setObjectName(_fromUtf8("uart"))
        uart.resize(447, 239)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(uart)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.bg = QtGui.QWidget(uart)
        self.bg.setObjectName(_fromUtf8("bg"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.bg)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setContentsMargins(15, 15, 30, 15)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.bg)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.bg)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.bg)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_3 = QtGui.QPushButton(self.bg)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.bg)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout.addWidget(self.pushButton_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addWidget(self.bg)

        self.retranslateUi(uart)
        QtCore.QMetaObject.connectSlotsByName(uart)

    def retranslateUi(self, uart):
        uart.setWindowTitle(_translate("uart", "Form", None))
        self.pushButton.setText(_translate("uart", "Setting", None))
        self.pushButton_2.setText(_translate("uart", "Start", None))
        self.pushButton_3.setText(_translate("uart", "Load", None))
        self.pushButton_4.setText(_translate("uart", "Save", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    uart = QtGui.QWidget()
    ui = Ui_uart()
    ui.setupUi(uart)
    uart.show()
    sys.exit(app.exec_())

