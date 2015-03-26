# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\hb\projects\usd\views\ui\uart.ui'
#
# Created: Fri Feb 13 20:14:13 2015
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
        uart.resize(628, 376)
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
        self.log = QtGui.QPlainTextEdit(self.bg)
        self.log.setFrameShape(QtGui.QFrame.NoFrame)
        self.log.setTabChangesFocus(True)
        self.log.setReadOnly(False)
        self.log.setObjectName(_fromUtf8("log"))
        self.horizontalLayout.addWidget(self.log)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.bg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 60))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.btn_startstop = QtGui.QPushButton(self.bg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_startstop.sizePolicy().hasHeightForWidth())
        self.btn_startstop.setSizePolicy(sizePolicy)
        self.btn_startstop.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_startstop.setObjectName(_fromUtf8("btn_startstop"))
        self.verticalLayout.addWidget(self.btn_startstop)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_3 = QtGui.QPushButton(self.bg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.bg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout.addWidget(self.pushButton_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addWidget(self.bg)

        self.retranslateUi(uart)
        QtCore.QMetaObject.connectSlotsByName(uart)

    def retranslateUi(self, uart):
        uart.setWindowTitle(_translate("uart", "Form", None))
        self.pushButton.setText(_translate("uart", "Setting", None))
        self.btn_startstop.setText(_translate("uart", "Start", None))
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

