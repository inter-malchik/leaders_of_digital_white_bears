# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUItest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 368)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 401, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.directoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.directoryButton.setGeometry(QtCore.QRect(140, 80, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.directoryButton.setFont(font)
        self.directoryButton.setObjectName("directoryButton")
        self.handlerButton = QtWidgets.QPushButton(self.centralwidget)
        self.handlerButton.setGeometry(QtCore.QRect(20, 230, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.handlerButton.setFont(font)
        self.handlerButton.setObjectName("handlerButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.directoryButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.directoryButton_2.setGeometry(QtCore.QRect(140, 170, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.directoryButton_2.setFont(font)
        self.directoryButton_2.setObjectName("directoryButton_2")
        self.saveToLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.saveToLineEdit.setGeometry(QtCore.QRect(130, 140, 341, 22))
        self.saveToLineEdit.setObjectName("saveToLineEdit")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(452, 10, 31, 28))
        self.closeButton.setObjectName("closeButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 492, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "????????:"))
        self.directoryButton.setText(_translate("MainWindow", "?????????????? ??????????"))
        self.handlerButton.setText(_translate("MainWindow", "?????????? ??????????"))
        self.label_2.setText(_translate("MainWindow", "?????????????????? ?? "))
        self.directoryButton_2.setText(_translate("MainWindow", "?????????????? ??????????"))
        self.closeButton.setText(_translate("MainWindow", "x"))
