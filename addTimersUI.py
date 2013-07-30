# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addTimers.ui'
#
# Created: Mon Jul 29 22:33:22 2013
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_dlogAddTimers(object):
    def setupUi(self, dlogAddTimers):
        dlogAddTimers.setObjectName(_fromUtf8("dlogAddTimers"))
        dlogAddTimers.resize(368, 109)
        self.buttonBox = QtGui.QDialogButtonBox(dlogAddTimers)
        self.buttonBox.setGeometry(QtCore.QRect(10, 70, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.textEdit = QtGui.QTextEdit(dlogAddTimers)
        self.textEdit.setGeometry(QtCore.QRect(20, 30, 331, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(dlogAddTimers)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), dlogAddTimers.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), dlogAddTimers.reject)
        QtCore.QMetaObject.connectSlotsByName(dlogAddTimers)

    def retranslateUi(self, dlogAddTimers):
        dlogAddTimers.setWindowTitle(_translate("dlogAddTimers", "Add Timers", None))

