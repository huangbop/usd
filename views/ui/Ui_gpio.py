# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\hb\projects\usd\views\ui\gpio.ui'
#
# Created: Sun Feb  8 23:51:37 2015
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

class Ui_gpio(object):
    def setupUi(self, gpio):
        gpio.setObjectName(_fromUtf8("gpio"))
        gpio.resize(615, 520)
        self.horizontalLayout = QtGui.QHBoxLayout(gpio)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.bg = QtGui.QWidget(gpio)
        self.bg.setObjectName(_fromUtf8("bg"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.bg)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setContentsMargins(15, 15, 30, 15)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.plot_bg = QtGui.QWidget(self.bg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_bg.sizePolicy().hasHeightForWidth())
        self.plot_bg.setSizePolicy(sizePolicy)
        self.plot_bg.setObjectName(_fromUtf8("plot_bg"))
        self.horizontalLayout_2.addWidget(self.plot_bg)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.bg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_2 = QtGui.QPushButton(self.bg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.bg)

        self.retranslateUi(gpio)
        QtCore.QMetaObject.connectSlotsByName(gpio)

    def retranslateUi(self, gpio):
        gpio.setWindowTitle(_translate("gpio", "Form", None))
        self.pushButton.setText(_translate("gpio", "Acquire", None))
        self.pushButton_2.setText(_translate("gpio", "Export", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    gpio = QtGui.QWidget()
    ui = Ui_gpio()
    ui.setupUi(gpio)
    gpio.show()
    sys.exit(app.exec_())

