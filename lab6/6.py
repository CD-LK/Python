import sys
import csv
import datetime
import os
import multiprocessing as mlp
from Test import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.chek = False
        self.login_array = []
        self.data_array = []
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.OpenFile.clicked.connect(self.OpenFile)
        self.ui.AnalizFile.clicked.connect(self.full_pool)
        self.ui.serchLogin.clicked.connect(self.serch_Login)
        self.ui.serchData.clicked.connect(self.serch_Data)
        self.ui.saveData.clicked.connect(self.save_Data)
        self.ui.AnalizFile_2.clicked.connect(self.go_to)
        self.my_pool = mlp.Pool(1)

    def OpenFile(self):
        fileD = QtWidgets.QFileDialog()
        open_file = fileD.getExistingDirectory(self)
        self.ui.PathFile.setText('')
        self.ui.PathFile.setText(open_file)

    """def read_dir(self):
        print('read')
        self.ui.tableWidget.setRowCount(0)
        self.path_file = self.ui.PathFile.text()
        if os.path.exists(self.path_file) is False:
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Введите путь')
            self.ui.PathFile.setText('')
            return 2
        list_dir = os.listdir(self.path_file)
        csv_files = []
        for i in range(len(list_dir) - 1):
            chek = os.path.isfile(list_dir[i])
            if chek:
                sp_file = list_dir[i].split('.')
                if sp_file[-1] == 'csv':
                    csv_files.append(list_dir[i])
        if self.data_array != []:
            self.data_array.clear()
        if self.data_array != []:
            self.login_array.clear()
        all_data = []
        for i in range(len(csv_files)):
            with open(csv_files[i], 'r')as csv_file:
                reader = csv.reader(csv_file)  # reader - список списсков
                data = list(reader)
            all_data.append(data)
        solo_data = list.copy(all_data[0])
        for i in range(1, len(all_data)):
            all_data[i].remove(all_data[i][0])
            solo_data += all_data[i]
        print(solo_data)
        return solo_data"""

    def set_data(self, solo_data):
        print('start')
        if self.data_array != []:
            self.data_array.clear()
        if self.data_array != []:
            self.login_array.clear()
        miim = 0
        maam = len(solo_data) - 2
        id = self.ui.comboBox.currentIndex()
        count_box = self.ui.comboBox.count()
        for i in range(1, count_box):
            if id == i:
                miim = (i - 1) * 100
                maam = i * 100 - 1
        ost = len(solo_data) % 100
        count_id = len(solo_data) - ost
        count_id = int(count_id / 100)
        self.ui.tableWidget.setHorizontalHeaderLabels(solo_data[0])
        self.ui.progressBar.setMaximum(len(solo_data))
        value = 0
        self.ui.tableWidget.setRowCount(0)
        for i, row in enumerate(solo_data[1:]):
            value += 1
            self.ui.progressBar.setValue(value)
            if miim <= i <= maam:
                self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
                for j, v in enumerate(row):
                    if j == 0:
                        self.data_array.append(v)
                    elif j == 3:
                        self.login_array.append(v)
                    it = QtWidgets.QTableWidgetItem()
                    it.setData(QtCore.Qt.DisplayRole, v)
                    self.ui.tableWidget.setItem((i - miim), j, it)
        c = self.ui.comboBox.count()
        if c > 1:
            self.ui.comboBox.clear()
            self.ui.comboBox.addItem("Все элементы")
        for i in range(count_id):
            self.ui.comboBox.addItem("{0} - ая сотня элементов".format(i + 1))
        self.ui.comboBox.addItem("Последнии элементы")
        self.ui.progressBar.setValue(value + 1)
        self.ui.progressBar.setValue(0)
        self.chek = True
        self.save_array = list.copy(solo_data)
        print('end')

    def go_to(self):
        d = self.ui.tableWidget.rowViewportPosition(100)
        self.ui.tableWidget.SelectionMode(4)
        print(d)

    def serch_Login(self):
        if self.data_array != []:
            self.data_array.clear()
        if self.chek:
            login, ok = QtWidgets.QInputDialog.getText(self, "Ввод логина",
                                                       "Введите логин для поиска:", QtWidgets.QLineEdit.Normal,
                                                       '')

            if ok and login:
                if login in self.login_array:
                    self.login_array.clear()
                    self.ui.tableWidget.setRowCount(0)
                    self.ui.tableWidget.setHorizontalHeaderLabels(self.save_array[0])
                    self.ui.progressBar.setMaximum(len(self.save_array))
                    p = 0
                    value = 0
                    for i, row in enumerate(self.save_array[1:]):
                        value += 1
                        self.ui.progressBar.setValue(value)
                        if login in row:
                            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
                            for j, v in enumerate(row):
                                if j == 0:
                                    self.data_array.append(v)
                                it = QtWidgets.QTableWidgetItem()
                                it.setData(QtCore.Qt.DisplayRole, v)
                                self.ui.tableWidget.setItem(p, j, it)
                            p += 1
                    self.ui.progressBar.setValue(value + 1)
                    self.ui.progressBar.setValue(0)
                else:
                    QtWidgets.QMessageBox.about(self, 'Ошибка', 'Логина не найдено.')
            else:
                QtWidgets.QMessageBox.about(self, 'Ошибка', 'Введите логин.')
        else:
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Проанализируйте файл.')

    def serch_Data(self):
        if self.login_array != []:
            self.login_array.clear()
        if self.chek:
            enter = self.ui.dateTimeEdit.text()
            enter = enter.split(' ')
            age = enter[0]
            clock = enter[1]
            age = age.split('.')
            clock = clock.split(':')
            unix_time = datetime.datetime(int(age[2]), int(age[1]), int(age[0]), int(clock[0]), int(clock[1]),
                                          int(clock[2])).timestamp()

            unix_time = int(unix_time)
            unix_time += 36000
            unix_time = str(unix_time)
            if unix_time in self.data_array:
                self.data_array.clear()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setHorizontalHeaderLabels(self.save_array[0])
                self.ui.progressBar.setMaximum(len(self.save_array))
                p = 0
                value = 0
                for i, row in enumerate(self.save_array[1:]):
                    value += 1
                    self.ui.progressBar.setValue(value)
                    if unix_time == row[0]:
                        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
                        for j, v in enumerate(row):
                            if j == 3:
                                self.login_array.append(v)
                            it = QtWidgets.QTableWidgetItem()
                            it.setData(QtCore.Qt.DisplayRole, v)
                            self.ui.tableWidget.setItem(p, j, it)
                        p += 1

                self.ui.progressBar.setValue(value + 1)
                self.ui.progressBar.setValue(0)

                pass
            else:
                QtWidgets.QMessageBox.about(self, 'Ошибка', 'Дата не найдена')
        else:
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Проанализируйте файл')

    def save_Data(self):
        header = ['begin', 'end', 'time interval', 'login', 'mac ab', 'ULSK1', 'BRAS ip', 'start count', 'alive count',
                  'stop count', 'incoming', 'outcoming', 'error_count', 'code 0', 'code 1011', 'code 1100', 'code -3',
                  'code -52', 'code -42', 'code -21', 'code -40', ' code -44', 'code -46', ' code -38']
        rowCount = self.ui.tableWidget.rowCount()
        columCount = 24
        d = QtWidgets.QFileDialog.getSaveFileName(self, "Choose a filename to save under", "/data_save",
                                                  "Файл Microsoft Excel (*.csv)")
        if d[0] == '':
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Вы отменили сохранение')
            return 1
        self.ui.progressBar.setMaximum(rowCount)
        value = 0
        with open(d[0], 'w', newline='') as file_csv:
            writher = csv.writer(file_csv)
            writher.writerow(header)
            for i in range(rowCount):
                save = []
                value += 1
                self.ui.progressBar.setValue(value)
                for j in range(columCount):
                    p = self.ui.tableWidget.item(i, j).text()
                    save.append(p)
                writher.writerow(save)
        self.ui.progressBar.setValue(value + 1)
        self.ui.progressBar.setValue(0)

    def full_pool(self):
        print(000)
        path_file = self.ui.PathFile.text()
        if os.path.exists(path_file) is False:
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Введите путь')
            self.ui.PathFile.setText('')
            return 2
        list_dir = os.listdir(path_file)
        print(123)
        csv_files = []
        for i in range(len(list_dir) - 1):
            chek = os.path.isfile(list_dir[i])
            if chek:
                sp_file = list_dir[i].split('.')
                if sp_file[-1] == 'csv':
                    csv_files.append(list_dir[i])
        print(321)
        print(len(csv_files))
        print(csv_files)
        self.my_pool.apply_async(func=read_ddir, args=(csv_files,), callback=self.set_data)
        print(111)
        self.my_pool.close()
        self.my_pool.join()



def read_ddir(csv_files):
    print(99)
    all_data = []
    for i in range(len(csv_files)):
        with open(csv_files[i], 'r')as csv_file:
            reader = csv.reader(csv_file)  # reader - список списсков
            data = list(reader)
        all_data.append(data)
    solo_data = list.copy(all_data[0])
    for i in range(1, len(all_data)):
        all_data[i].remove(all_data[i][0])
        solo_data += all_data[i]
    print(190)
    return solo_data


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
