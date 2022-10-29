# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'leaf_v4.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
###########################################################
# Ui is finished now the implimentation is next
##########################################################
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon

class Ui_leaf(object):
    def setupUi(self, leaf):
        leaf.setObjectName("leaf")
        leaf.resize(800, 565)
        leaf.setWindowIcon(QIcon('E:\Python\GUI Try\icon.png')) 

        self.label_1 = QtWidgets.QLabel(leaf)
        self.label_1.setGeometry(QtCore.QRect(70, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(leaf)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 91, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(leaf)
        self.label_3.setGeometry(QtCore.QRect(70, 200, 91, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(leaf)
        self.label_4.setGeometry(QtCore.QRect(70, 260, 61, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(leaf)
        self.label_5.setGeometry(QtCore.QRect(70, 300, 61, 41))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(leaf)
        self.pushButton.setGeometry(QtCore.QRect(270, 430, 91, 41))
        self.pushButton.setObjectName("pushButton")

        # clicking function // pushbutton for reset
        self.pushButton.clicked.connect(self.clicked)

        self.pushButton_2 = QtWidgets.QPushButton(leaf)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 430, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        # clicking function // pushbutton_2 for load 
        self.pushButton_2.clicked.connect(self.loading)


        self.textEdit = QtWidgets.QTextEdit(leaf)
        self.textEdit.setGeometry(QtCore.QRect(160, 110, 231, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(leaf)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 160, 231, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(leaf)
        self.textEdit_3.setGeometry(QtCore.QRect(160, 210, 231, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(leaf)
        self.textEdit_4.setGeometry(QtCore.QRect(160, 260, 231, 41))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(leaf)
        self.textEdit_5.setGeometry(QtCore.QRect(160, 310, 231, 41))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_6 = QtWidgets.QLabel(leaf)
        self.label_6.setGeometry(QtCore.QRect(550, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(leaf)
        self.label_7.setGeometry(QtCore.QRect(550, 270, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.image_1 = QtWidgets.QLabel(leaf)
        self.image_1.setGeometry(QtCore.QRect(470, 70, 241, 171))
        self.image_1.setScaledContents(True)
        self.image_1.setObjectName("image_1")
        self.image_2 = QtWidgets.QLabel(leaf)
        self.image_2.setGeometry(QtCore.QRect(470, 330, 241, 171))
        self.image_2.setScaledContents(True)
        self.image_2.setObjectName("image_2")

        self.retranslateUi(leaf)
        QtCore.QMetaObject.connectSlotsByName(leaf)

    def retranslateUi(self, leaf):
        _translate = QtCore.QCoreApplication.translate
        leaf.setWindowTitle(_translate("leaf", "Plant Identifier"))
        self.label_1.setText(_translate("leaf", "Name"))
        self.label_2.setText(_translate("leaf", "Batanic texanomy"))
        self.label_3.setText(_translate("leaf", "Flowering period"))
        self.label_4.setText(_translate("leaf", "Leaf type"))
        self.label_5.setText(_translate("leaf", "confidence"))
        self.pushButton.setText(_translate("leaf", "Reset"))
        self.pushButton_2.setText(_translate("leaf", "Load"))
        self.label_6.setText(_translate("leaf", "Input image"))
        self.label_7.setText(_translate("leaf", "Detected Plant"))

        #SHOWING THE IMAGES
        
        #src method
        #self.image_1.setText(_translate("leaf", "<html><head/><body><p><img src=\"E:\Python\GUI Try\leafc.jpg\"/></p></body></html>"))
        #self.image_2.setText(_translate("leaf", "<html><head/><body><p><img src=\"E:\Python\GUI Try\leafc.jpg\"/></p></body></html>"))
        
        #or use the pixmap method
        pixmap=QtGui.QPixmap("E:\Python\GUI Try\leafc.jpg")

        self.image_1.setPixmap(pixmap)
        self.image_2.setPixmap(pixmap)

        # to load another image decleare it as a pixpam and use setPixmap

    def clicked(self):
        self.textEdit.setText("Reset")
        self.textEdit_2.setText("Reset 1")
        self.textEdit_3.setText("Reset 2")
        self.textEdit_4.setText("Reset 3")
        self.textEdit_5.setText("Reset 4")
        
        

    def loading(self):
        self.textEdit.setText("Loading")
        self.textEdit_2.setText("Loading 1")
        self.textEdit_3.setText("Loading 2")
        self.textEdit_4.setText("Loading 3")
        self.textEdit_5.setText("Loading 4")

        #loading a file/image
        loadedim, _ = QFileDialog.getOpenFileName()
        # the _ is used to unpack the tuple and get only the file name as str value
        loadedimpx = QtGui.QPixmap(loadedim)
        self.image_1.setPixmap(loadedimpx)    




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    leaf = QtWidgets.QDialog()
    ui = Ui_leaf()
    ui.setupUi(leaf)
    leaf.show()
    sys.exit(app.exec_())
