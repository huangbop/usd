# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\hb\projects\usd\views\ui\gpio.ui'
#
# Created: Sat Feb  7 18:02:21 2015
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
        gpio.resize(528, 502)
        self.horizontalLayout = QtGui.QHBoxLayout(gpio)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.bg = QtGui.QWidget(gpio)
        self.bg.setObjectName(_fromUtf8("bg"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.bg)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.leds_bg = QtGui.QWidget(self.bg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leds_bg.sizePolicy().hasHeightForWidth())
        self.leds_bg.setSizePolicy(sizePolicy)
        self.leds_bg.setMinimumSize(QtCore.QSize(0, 50))
        self.leds_bg.setObjectName(_fromUtf8("leds_bg"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.leds_bg)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.toolButton = QtGui.QToolButton(self.leds_bg)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.toolButton_2 = QtGui.QToolButton(self.leds_bg)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        self.toolButton_3 = QtGui.QToolButton(self.leds_bg)
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.horizontalLayout_2.addWidget(self.toolButton_3)
        self.toolButton_4 = QtGui.QToolButton(self.leds_bg)
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.horizontalLayout_2.addWidget(self.toolButton_4)
        self.toolButton_5 = QtGui.QToolButton(self.leds_bg)
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.horizontalLayout_2.addWidget(self.toolButton_5)
        self.toolButton_6 = QtGui.QToolButton(self.leds_bg)
        self.toolButton_6.setObjectName(_fromUtf8("toolButton_6"))
        self.horizontalLayout_2.addWidget(self.toolButton_6)
        self.toolButton_7 = QtGui.QToolButton(self.leds_bg)
        self.toolButton_7.setObjectName(_fromUtf8("toolButton_7"))
        self.horizontalLayout_2.addWidget(self.toolButton_7)
        self.toolButton_8 = QtGui.QToolButton(self.leds_bg)
        self.toolButton_8.setObjectName(_fromUtf8("toolButton_8"))
        self.horizontalLayout_2.addWidget(self.toolButton_8)
        self.horizontalLayout_3.addWidget(self.leds_bg)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.plot_bg = QtGui.QWidget(self.bg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_bg.sizePolicy().hasHeightForWidth())
        self.plot_bg.setSizePolicy(sizePolicy)
        self.plot_bg.setMinimumSize(QtCore.QSize(80, 400))
        self.plot_bg.setBaseSize(QtCore.QSize(30, 50))
        self.plot_bg.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 127);"))
        self.plot_bg.setObjectName(_fromUtf8("plot_bg"))
        self.verticalLayout.addWidget(self.plot_bg)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButton = QtGui.QPushButton(self.bg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButton_2 = QtGui.QPushButton(self.bg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addWidget(self.bg)

        self.retranslateUi(gpio)
        QtCore.QMetaObject.connectSlotsByName(gpio)

    def retranslateUi(self, gpio):
        gpio.setWindowTitle(_translate("gpio", "Form", None))
        self.toolButton.setText(_translate("gpio", "a", None))
        self.toolButton_2.setText(_translate("gpio", "b", None))
        self.toolButton_3.setText(_translate("gpio", "c", None))
        self.toolButton_4.setText(_translate("gpio", "d", None))
        self.toolButton_5.setText(_translate("gpio", "e", None))
        self.toolButton_6.setText(_translate("gpio", "f", None))
        self.toolButton_7.setText(_translate("gpio", "g", None))
        self.toolButton_8.setText(_translate("gpio", "h", None))
        self.pushButton.setText(_translate("gpio", "PushButton", None))
        self.pushButton_2.setText(_translate("gpio", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    gpio = QtGui.QWidget()
    ui = Ui_gpio()
    ui.setupUi(gpio)
    gpio.show()
    sys.exit(app.exec_())

