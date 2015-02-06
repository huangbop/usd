# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\hb\projects\usd\views\ui\title.ui'
#
# Created: Fri Feb  6 17:43:38 2015
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

class Ui_title(object):
    def setupUi(self, title):
        title.setObjectName(_fromUtf8("title"))
        title.resize(549, 199)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(title)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.bg = QtGui.QWidget(title)
        self.bg.setObjectName(_fromUtf8("bg"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.bg)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setMargin(2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tab_uart = QtGui.QToolButton(self.bg)
        self.tab_uart.setMinimumSize(QtCore.QSize(70, 70))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/uart.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_uart.setIcon(icon)
        self.tab_uart.setIconSize(QtCore.QSize(48, 48))
        self.tab_uart.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tab_uart.setObjectName(_fromUtf8("tab_uart"))
        self.horizontalLayout_2.addWidget(self.tab_uart)
        self.tab_gpio = QtGui.QToolButton(self.bg)
        self.tab_gpio.setMinimumSize(QtCore.QSize(70, 70))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/gpio.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_gpio.setIcon(icon1)
        self.tab_gpio.setIconSize(QtCore.QSize(48, 48))
        self.tab_gpio.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tab_gpio.setObjectName(_fromUtf8("tab_gpio"))
        self.horizontalLayout_2.addWidget(self.tab_gpio)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(224, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(-1, 4, 6, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolButton = QtGui.QToolButton(self.bg)
        self.toolButton.setMinimumSize(QtCore.QSize(28, 28))
        self.toolButton.setMaximumSize(QtCore.QSize(28, 28))
        self.toolButton.setBaseSize(QtCore.QSize(28, 28))
        self.toolButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/setting.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon2)
        self.toolButton.setIconSize(QtCore.QSize(24, 24))
        self.toolButton.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.btn_min = QtGui.QToolButton(self.bg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_min.sizePolicy().hasHeightForWidth())
        self.btn_min.setSizePolicy(sizePolicy)
        self.btn_min.setMinimumSize(QtCore.QSize(10, 10))
        self.btn_min.setMaximumSize(QtCore.QSize(24, 24))
        self.btn_min.setBaseSize(QtCore.QSize(10, 10))
        self.btn_min.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/min.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_min.setIcon(icon3)
        self.btn_min.setIconSize(QtCore.QSize(24, 24))
        self.btn_min.setObjectName(_fromUtf8("btn_min"))
        self.horizontalLayout.addWidget(self.btn_min)
        self.btn_close = QtGui.QToolButton(self.bg)
        self.btn_close.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QtCore.QSize(24, 24))
        self.btn_close.setMaximumSize(QtCore.QSize(24, 24))
        self.btn_close.setBaseSize(QtCore.QSize(24, 24))
        self.btn_close.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon4)
        self.btn_close.setIconSize(QtCore.QSize(24, 24))
        self.btn_close.setObjectName(_fromUtf8("btn_close"))
        self.horizontalLayout.addWidget(self.btn_close)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addWidget(self.bg)

        self.retranslateUi(title)
        QtCore.QMetaObject.connectSlotsByName(title)

    def retranslateUi(self, title):
        title.setWindowTitle(_translate("title", "Form", None))
        self.tab_uart.setText(_translate("title", "UART", None))
        self.tab_gpio.setText(_translate("title", "GPIO", None))

import usd_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    title = QtGui.QWidget()
    ui = Ui_title()
    ui.setupUi(title)
    title.show()
    sys.exit(app.exec_())

