import typing
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import *
from GologinController.GologinController import GologinController

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 734)
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.groupBox = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(200, 200))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        
        self.textEdit = QtWidgets.QTextEdit(parent=self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(10, 59, 180, 30))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit.setObjectName("textEdit")
        
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 23, 59, 16))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 60, 16))
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setObjectName("label_2")
        
        self.spinBox = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(150, 100, 37, 30))
        self.spinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.spinBox.setMaximumSize(QtCore.QSize(50, 50))
        self.spinBox.setObjectName("spinBox")
        
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 4, 1, 1)
        
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.spinBox_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_3.addWidget(self.spinBox_2, 1, 2, 1, 1)
        
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        
        self.comboBox = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 2, 2, 1, 1)
        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.groupBox_2)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_3.addWidget(self.plainTextEdit, 3, 2, 1, 1)
        
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget, 5, 0, 1, 5)
        
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 0, 100, 30))
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 2, 2)
        
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 0, 100, 30))
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.frame_2, 2, 0, 2, 2)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Connect:
        self.pushButton.clicked.connect(self.run_profile)
        self.pushButton_2.clicked.connect(self.stop)
        
        self.row_count = 0
        
    
    def run_profile(self):
        
        token = self.textEdit.toPlainText()
        number_thread = self.spinBox.value()
        self.threads = {}
        for i in range(number_thread):
            self.threads[i] = ThreadProfile(token = token, name_profile=f"profile_{i}", port= 3200 + i)
            self.threads[i].start()
            self.threads[i].signal_status.connect(self.update_table)
            
    def stop(self):
        
        for i in range(len( self.threads)):
            self.threads[i].stop()
        
    def update_table(self, profile_id, account, password, status):
        
        # STT, Profile ID, Acc, Pass, Status
        
        self.tableWidget.setColumnCount(5)
        
        
        self.tableWidget.setStyleSheet("background-color:rgb(85, 255, 127)rgb(255, 255, 255)")

        self.tableWidget.setHorizontalHeaderLabels(['STT', 'Profile ID', 'Acc', 'Pass', 'Status'])
        # self.tableWidget.setSelectionMode(QAbstractItemView.setSelection)
        # self.tableWidget.setEditTriggers(QAbstractItemView.EditTriggers.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.Stretch)
        # self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeColumnToContents(2)
        self.tableWidget.setColumnWidth(1,150)
        # self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        print(profile_id, account, password, status)
        
        self.row_count += 1
        self.tableWidget.setRowCount(self.row_count)
        self.tableWidget.setItem(self.row_count - 1, 0, QtWidgets.QTableWidgetItem(self.row_count))
        self.tableWidget.setItem(self.row_count - 1, 1, QtWidgets.QTableWidgetItem(profile_id))
        self.tableWidget.setItem(self.row_count - 1, 2, QtWidgets.QTableWidgetItem(account))
        self.tableWidget.setItem(self.row_count - 1, 3, QtWidgets.QTableWidgetItem(password))
        self.tableWidget.setItem(self.row_count - 1, 4, QtWidgets.QTableWidgetItem(status))
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Cài đặt chung"))
        self.label.setText(_translate("MainWindow", "Nhập token:"))
        self.label_2.setText(_translate("MainWindow", "Số luồng:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Hành động"))
        self.label_4.setText(_translate("MainWindow", "Số lượng reg:"))
        self.label_3.setText(_translate("MainWindow", "Proxy:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "TMProxy"))
        self.comboBox.setItemText(1, _translate("MainWindow", "MinProxy"))
        self.pushButton.setText(_translate("MainWindow", "Chạy"))
        self.pushButton_2.setText(_translate("MainWindow", "Dừng"))
        

class ThreadProfile(QtCore.QThread):
    
    signal_status = QtCore.pyqtSignal(object, object, object, object)
    def __init__(self, token, name_profile, port):
        super(ThreadProfile, self).__init__()
        self.token = token
        self.name_profile = name_profile
        self.port = port

    def run(self):
        # Chạy hành động gì???
        auto = GologinController(token=self.token)
        profile_id = auto.create_profile(name_profile=self.name_profile)
        auto.open_profile(port=self.port)
        account, password = auto.reg_gmail()
        self.signal_status.emit(profile_id, account, password, "Thành công!")
    
    def stop(self):
        self.terminate()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    
    sys.exit(app.exec())


