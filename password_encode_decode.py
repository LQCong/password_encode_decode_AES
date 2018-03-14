# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Crypto.Cipher import AES
import base64
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 370)
        MainWindow.setMinimumSize(QtCore.QSize(640, 370))
        MainWindow.setMaximumSize(QtCore.QSize(640, 370))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setToolTip("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(22, 30, 561, 68))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMaxLength(16)
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setMaxLength(16)
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 110, 601, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(597, 28, 31, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setWhatsThis("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setWhatsThis("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(110, 220, 417, 94))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 180, 601, 28))
        self.lineEdit_4.setObjectName("lineEdit_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 34))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        # 加密
        self.pushButton_4.clicked.connect(lambda: self.password_encode())
        # 解密
        self.pushButton_3.clicked.connect(lambda: self.password_deconde())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # self.buttonbox.clicked.connect(lambda: self.Foo(x1, x2, x3))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "简易AES密码加密工具"))
        self.label.setText(_translate("MainWindow", "请输入AES加密KEY值(最长16位)"))
        self.label_2.setText(_translate("MainWindow", "请输入AES加密VI值 (最长16位)"))
        self.label_3.setText(_translate("MainWindow", "需加密/解码的密码"))
        self.pushButton_2.setText(_translate("MainWindow", " ？"))
        self.pushButton_2.setToolTip("请输入一串自己容易记的KEY值，该值在加密或解密时需要\n"
                                         "如果不记得将无法解密，不超过16个字符\n"
                                         "不输入则用默认值16个0【不推荐】")
        self.pushButton.setText(_translate("MainWindow", " ？"))
        self.pushButton.setToolTip("请输入一串自己容易记的KEY值，该值在加密或解密时需要\n"
                                         "如果不记得将无法解密，不超过16个字符\n"
                                         "不输入则用默认值16个0【不推荐】")
        self.pushButton_4.setText(_translate("MainWindow", "加密"))
        self.pushButton_3.setText(_translate("MainWindow", "解密"))



    def password_encode(self):
        key = self.lineEdit.text()
        iv = self.lineEdit_2.text()
        string = self.lineEdit_3.text()
        #如果不输入key或iv值，则使用默认值
        if key == "":
            key = "0000000000000000"
        if iv == "":
            iv = "0000000000000000"

        #检查key和iv值是否满足16位,不满足16位用空格填充
        if len(key) != 16:
            key = key + "\0" * (16-len(key))
        if len(iv) != 16:
            iv = iv + "\0" * (16-len(iv))

        obj = AES.new(key, AES.MODE_CBC, iv)
        # 判断输入字码是否为16的倍数，不是16倍以空格填充
        count = len(string) % 16
        if len(string) != 0:
            text = string + "\0" * (16 - count)
        c = obj.encrypt(text)
        # print(c)
        s = base64.encodebytes(c).decode("utf-8")
        return (self.lineEdit_4.setText(s))


    def password_deconde(self):
        key = self.lineEdit.text()
        iv = self.lineEdit_2.text()
        string = self.lineEdit_3.text()
        #如果不输入key或iv值，则使用默认值
        if key == "":
            key = "0000000000000000"
        if iv == "":
            iv = "0000000000000000"
        #检查key和iv值是否满足16位,不满足16位用空格填充
        if len(key) != 16:
            key = key + "\0" * (16-len(key))
        if len(iv) != 16:
            iv = iv + "\0" * (16-len(iv))
        try:
            c = base64.decodebytes(str.encode(string))
            obj2 = AES.new(key, AES.MODE_CBC, iv)
            e = obj2.decrypt(c).decode("utf-8").strip()
            return (self.lineEdit_4.setText(e))
        except Exception as err:
            self.lineEdit_4.setText("输入的解密密码错误，请检查")
            #pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(windows)

    windows.show()
    sys.exit(app.exec_())