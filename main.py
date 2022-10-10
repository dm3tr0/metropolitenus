from lzma import is_check_supported
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.withdraw()

station_list = []

answers = 0
rights = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 449)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 100, 441, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 290, 441, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 230, 400, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 180, 441, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(350, 230, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 441, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_3.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.progressBar.setValue(0)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel1"))
        self.label_2.setText(_translate("MainWindow", "TextLabel2"))
        self.label_3.setText(_translate("MainWindow", "TextLabel3"))
        self.pushButton.setText(_translate("MainWindow", "Старт"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton2"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton3"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton4"))
        self.label_4.setText(_translate("MainWindow", "Обери лінію (колір)"))
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.answer1)
        self.pushButton_3.clicked.connect(self.answer2)
        self.pushButton_4.clicked.connect(self.answer3)
        self.radioButton_3.setText(_translate("MainWindow", "Червона"))
        self.radioButton_2.setText(_translate("MainWindow", "Синя"))
        self.radioButton.setText(_translate("MainWindow", "Зелена"))
    def linus(self):
        global station_list
        if self.radioButton_3.isChecked():
            self.line.setStyleSheet('color:red')
            station_list = ["Академ", "Житомирська", "Святошин", "Нивки", "Берестейська",
            "Шулявська", "Політех","Вокзальна", "Коледж зв'язку", "Театральна", "Хрещатик",
            "Общага", "Дніпро", "Гідропарк", "Лівобережна", "Дарниця", "Чернігівська", "Лісова"]
            return station_list
        elif self.radioButton_2.isChecked():
            self.line.setStyleSheet('color:blue')
            station_list = ["Теремки", "Іподром", "Плаза", "Васильківська", "Голосіївська",
            "Деміївська", "Либідська", "Палац Україна", "Олімпійська", "Площа Льва Толстого",
            "Майдан", "Поштова площа", "Контрактова площа", "Тараса Шевченка", "Петрівка", "Оболонь",
            "Мінська", "Героїв Дніпра"]
            return station_list
        elif self.radioButton.isChecked():
            self.line.setStyleSheet('color:green')
            station_list = ["Сирець", "Борн", "Лук'янівська", "Золоті Ворота", "Палац спорту",
            "Кловська", "Общага 2", "Дружби народів", "Видубичі", "Славутич", "Осокорки", "Позняки",
            "Харківська", "Вирлиця", "Бориспільська", "Червоний Хутір"]
            return station_list
        else:
            station_list = ['', '', '', '', '']
            return station_list
    def start(self):
        global random_list2, random_1
        self.linus()
        self.pushButton.setText('Рестарт')
        random_1 = random.randint(0, len(station_list)-3)
        random_list = random.sample(station_list, 2)
        random_list.append(station_list[random_1+1])
        self.label.setText(station_list[random_1])
        self.label_2.setText('?')
        self.label_3.setText(station_list[random_1+2])
        random_list2 = random.sample(random_list, 3)
        self.pushButton_2.setText(random_list2[0])
        self.pushButton_3.setText(random_list2[1])
        self.pushButton_4.setText(random_list2[2])
    
    def answer1(self):
        global rights, answers
        if self.pushButton_2.text() == station_list[random_1+1]:
            self.label_4.setText(f'Правильно, це - {station_list[random_1+1]}')
            answers += 1
            rights += 1
            self.progressBar.setProperty('value', rights/answers*100)
            self.start()
        else:
            self.label_4.setText(f'Ні, це - {station_list[random_1+1]}')
            answers += 1
            self.progressBar.setProperty('value', rights/answers*100)
            self.start()
    def answer2(self):
        global rights, answers
        if self.pushButton_3.text() == station_list[random_1+1]:
            self.label_4.setText(f'Правильно, це - {station_list[random_1+1]}')
            answers += 1
            rights += 1
            self.progressBar.setProperty('value', rights/answers*100)
            self.start()
        else:
            self.label_4.setText(f'Ні, це - {station_list[random_1+1]}')
            answers += 1
            self.progressBar.setProperty('value', rights/answers*100)
            self.start()
    def answer3(self):
        global rights, answers
        if self.pushButton_4.text() == station_list[random_1+1]:
            self.label_4.setText(f'Правильно, це - {station_list[random_1+1]}')
            answers += 1
            rights += 1
            self.progressBar.setProperty('value', rights/answers*100)
            self.start()
        else:
            self.label_4.setText(f'Ні, це - {station_list[random_1+1]}')
            answers += 1
            self.progressBar.setProperty('value', rights/answers*100)
            self.start()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())