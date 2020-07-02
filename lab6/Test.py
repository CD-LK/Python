# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1083, 714)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.OpenFile.setGeometry(QtCore.QRect(10, 10, 181, 31))
        self.OpenFile.setObjectName("OpenFile")
        self.AnalizFile = QtWidgets.QPushButton(self.centralwidget)
        self.AnalizFile.setGeometry(QtCore.QRect(10, 90, 181, 31))
        self.AnalizFile.setObjectName("AnalizFile")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(1040, 10, 31, 691))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1050, 20, 16, 651))
        self.label.setIndent(-2)
        self.label.setObjectName("label")
        self.PathFile = QtWidgets.QLineEdit(self.centralwidget)
        self.PathFile.setGeometry(QtCore.QRect(200, 10, 831, 31))
        self.PathFile.setObjectName("PathFile")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(200, 50, 831, 651))
        self.tableWidget.setColumnCount(24)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.serchLogin = QtWidgets.QPushButton(self.centralwidget)
        self.serchLogin.setGeometry(QtCore.QRect(10, 170, 181, 31))
        self.serchLogin.setObjectName("serchLogin")
        self.serchData = QtWidgets.QPushButton(self.centralwidget)
        self.serchData.setGeometry(QtCore.QRect(10, 250, 181, 31))
        self.serchData.setObjectName("serchData")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 130, 181, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.saveData = QtWidgets.QPushButton(self.centralwidget)
        self.saveData.setGeometry(QtCore.QRect(10, 50, 181, 31))
        self.saveData.setObjectName("saveData")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(10, 210, 181, 31))
        self.dateTimeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.OpenFile.raise_()
        self.AnalizFile.raise_()
        self.progressBar.raise_()
        self.PathFile.raise_()
        self.tableWidget.raise_()
        self.serchLogin.raise_()
        self.serchData.raise_()
        self.comboBox.raise_()
        self.saveData.raise_()
        self.label.raise_()
        self.dateTimeEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OpenFile.setText(_translate("MainWindow", "Открыть Папку"))
        self.AnalizFile.setText(_translate("MainWindow", "Анализ Папки"))
        self.label.setText(_translate("MainWindow", "П\n"
"р\n"
"о\n"
"г\n"
"р\n"
"е\n"
"с\n"
"с\n"
" \n"
"а\n"
"н\n"
"а\n"
"л\n"
"и\n"
"з\n"
"а\n"
" \n"
"ф\n"
"а\n"
"й\n"
"л\n"
"а"))
        self.serchLogin.setText(_translate("MainWindow", "Поиск по логину"))
        self.serchData.setText(_translate("MainWindow", "Поиск по дате"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Все элементы"))
        self.saveData.setText(_translate("MainWindow", "Сохранить данные"))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy H:mm:ss"))
