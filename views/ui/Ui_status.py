# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\hb\projects\usd\views\ui\status.ui'
#
# Created: Fri Feb  6 13:53:27 2015
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

class Ui_status(object):
    def setupUi(self, status):
        status.setObjectName(_fromUtf8("status"))
        status.resize(718, 45)
        self.horizontalLayout = QtGui.QHBoxLayout(status)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.bg = QtGui.QWidget(status)
        self.bg.setObjectName(_fromUtf8("bg"))
        self.horizontalLayout.addWidget(self.bg)

        self.retranslateUi(status)
        QtCore.QMetaObject.connectSlotsByName(status)

    def retranslateUi(self, status):
        status.setWindowTitle(_translate("status", "Form", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    status = QtGui.QWidget()
    ui = Ui_status()
    ui.setupUi(status)
    status.show()
    sys.exit(app.exec_())

