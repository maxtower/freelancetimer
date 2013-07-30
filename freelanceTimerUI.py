# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'freelanceTimer.ui'
#
# Created: Mon Jul 29 22:33:36 2013
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(396, 307)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 200, 181, 61))
        self.pushButton.setStyleSheet(_fromUtf8("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 170, 0, 255), stop:1 rgba(0, 255, 0, 255));"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 10, 271, 31))
        self.comboBox.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 80, 271, 91))
        self.label.setStyleSheet(_fromUtf8("font: 48pt \"MS Shell Dlg 2\";"))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 396, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Project = QtGui.QAction(MainWindow)
        self.actionAdd_Project.setObjectName(_fromUtf8("actionAdd_Project"))
        self.actionSave_Timers = QtGui.QAction(MainWindow)
        self.actionSave_Timers.setObjectName(_fromUtf8("actionSave_Timers"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionAdd_Project)
        self.menuFile.addAction(self.actionSave_Timers)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Freelance Timer", None))
        self.pushButton.setText(_translate("MainWindow", "Start", None))
        self.label.setText(_translate("MainWindow", "0:00:00", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionAdd_Project.setText(_translate("MainWindow", "Add Project", None))
        self.actionSave_Timers.setText(_translate("MainWindow", "Save Timers", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

