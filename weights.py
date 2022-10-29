from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_weights(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(617, 195)
        self.buttonBox = QtWidgets.QPushButton(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 140, 120, 40))
        self.buttonBox.setObjectName("buttonBox")

        #closing pope up window 
        self.buttonBox.clicked.connect(Dialog.close)

        self.windowText = QtWidgets.QTextEdit(Dialog)
        self.windowText.setGeometry(QtCore.QRect(20, 90, 104, 31))
        self.windowText.setObjectName("windowText")

        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(140, 90, 104, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(260, 90, 104, 31))
        self.textEdit_3.setObjectName("textEdit_3")

        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(380, 90, 104, 31))
        self.textEdit_4.setObjectName("textEdit_4")

        self.textEdit_5 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(500, 90, 104, 31))
        self.textEdit_5.setObjectName("textEdit_5")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(270, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(410, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(530, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(210, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "  BAY"))
        self.label_2.setText(_translate("Dialog", "COCONUT"))
        self.label_3.setText(_translate("Dialog", "JACKFRUIT"))
        self.label_4.setText(_translate("Dialog", "MANGO"))
        self.label_5.setText(_translate("Dialog", "TARO"))
        self.label_6.setText(_translate("Dialog", "Weight Distribution"))
        self.buttonBox.setText(_translate("Dialog", "OK"))








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_weights()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
