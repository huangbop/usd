# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\hb\projects\usd\views\ui\register.ui'
#
# Created: Tue Feb 10 22:39:53 2015
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

class Ui_register_(object):
    def setupUi(self, register_):
        register_.setObjectName(_fromUtf8("register_"))
        register_.resize(680, 467)
        self.horizontalLayout = QtGui.QHBoxLayout(register_)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.bg = QtGui.QWidget(register_)
        self.bg.setObjectName(_fromUtf8("bg"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.bg)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setContentsMargins(15, 15, 30, 15)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableWidget = QtGui.QTableWidget(self.bg)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(self.bg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
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

        self.retranslateUi(register_)
        QtCore.QMetaObject.connectSlotsByName(register_)

    def retranslateUi(self, register_):
        register_.setWindowTitle(_translate("register_", "Form", None))
        self.pushButton.setText(_translate("register_", "Read", None))
        self.pushButton_2.setText(_translate("register_", "Write", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    register_ = QtGui.QWidget()
    ui = Ui_register_()
    ui.setupUi(register_)
    register_.show()
    sys.exit(app.exec_())

