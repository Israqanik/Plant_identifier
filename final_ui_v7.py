#imports for the UI
##########################################################
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon
import os
##########################################################
# Imports for the Neural network
# 'use Ctrl + / to comment all of the selected text'
#########################################################
import tensorflow as tf
import numpy as np
from tensorflow.keras import layers
from PIL import Image
from skimage import transform
from tensorflow.keras.models import load_model
import pathlib
##########################################################
#import popup
from weights import Ui_weights
##########################################################

global x

# for processing the loaded the image
def load(filename):
    np_image = Image.open(filename)
    np_image = np.array(np_image).astype('float32')/255
    np_image = transform.resize(np_image, (100, 100, 3))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image

# ui part
class Ui_leaf(object):

    #popup function
    def openWindow(self):
        self.window = QtWidgets.QMainWindow() 
        self.ui = Ui_weights()
        self.ui.setupUi(self.window)
        self.window.show()

    #main ui
    def setupUi(self, leaf):
        leaf.setObjectName("leaf")
        leaf.resize(800, 565)
        leaf.setWindowIcon(QIcon(os.path.join(os.getcwd(),'icon.png'))) 

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

        # clicking function // pushbutton for test
        self.pushButton.clicked.connect(self.clicked)

        self.pushButton_2 = QtWidgets.QPushButton(leaf)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 430, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        # clicking function // pushbutton_2 for load 
        self.pushButton_2.clicked.connect(self.loading)

        #popup link up
        self.pushButton.clicked.connect(self.openWindow)
        # passing infro connect
        #self.pushButton.clicked.connect(self.passingInfo)


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
        self.label_2.setText(_translate("leaf", "Scientific Name"))
        self.label_3.setText(_translate("leaf", "Flowering Period"))
        self.label_4.setText(_translate("leaf", "Fruit Type"))
        self.label_5.setText(_translate("leaf", "Floral Type"))
        self.pushButton.setText(_translate("leaf", "Detect"))
        self.pushButton_2.setText(_translate("leaf", "Load"))
        self.label_6.setText(_translate("leaf", "Input image"))
        self.label_7.setText(_translate("leaf", "Detected Plant"))
        

        #the pixmap method
        pixmap=QtGui.QPixmap(os.path.join(os.getcwd(), "leafc.jpg"))

        self.image_1.setPixmap(pixmap)
        self.image_2.setPixmap(pixmap)

        # to load another image decleare it as a pixpam and use setPixmap

    def clicked(self):
        #test file
        image = load(test_img_path)

        x = new_model.predict(image)
        # to see the weight distribution
        print("|| Bay || Coconut || Jackfruit || Mango || Taro ||")
        print(x)

       

        detectedClass = np.argmax(x)
        
        if detectedClass == 0:
            self.textEdit.setText("Bayleaf")
            self.textEdit_2.setText("Cinnamomum Tamala")
            self.textEdit_3.setText("Jan - March")
            self.textEdit_4.setText("Round, purple colored and has a single seed inside.")
            self.textEdit_5.setText("Tiny, greenish yellow, insignificant.")
            #show detected image example
            bayIm = QtGui.QPixmap(os.path.join(os.getcwd(), "bayim.jpg"))
            self.image_2.setPixmap(bayIm)

        elif detectedClass == 1:
            self.textEdit.setText("Coconut")
            self.textEdit_2.setText("Cocos nucifera")
            self.textEdit_3.setText("5–7 years after planting")
            self.textEdit_4.setText("Drupe (or stone fruit)")
            self.textEdit_5.setText("Polygamomonoecious")
            #show detected image example
            cocoIm = QtGui.QPixmap(os.path.join(os.getcwd(), "cocoim.jpg"))
            self.image_2.setPixmap(cocoIm)

        elif detectedClass == 2:
            self.textEdit.setText("Jackfruit")
            self.textEdit_2.setText("Artocarpus Heterophyllus")
            self.textEdit_3.setText("February-July")
            self.textEdit_4.setText("Coenocarpium")
            self.textEdit_5.setText(str(x))
            #show detected image example
            jackIm = QtGui.QPixmap(os.path.join(os.getcwd(), "jackim.jpg"))
            self.image_2.setPixmap(jackIm)

        elif detectedClass == 3:
            self.textEdit.setText("Mango")
            self.textEdit_2.setText("Mangifera Indica")
            self.textEdit_3.setText("January-June")
            self.textEdit_4.setText("Drupe")
            self.textEdit_5.setText("Pentamerous")
            #show detected image example
            mangoIm = QtGui.QPixmap(os.path.join(os.getcwd(), "mangoim.jpg"))
            self.image_2.setPixmap(mangoIm)

        elif detectedClass == 4:
            self.textEdit.setText("Taro")
            self.textEdit_2.setText("Colocasia Esculenta")
            self.textEdit_3.setText("February-April")
            self.textEdit_4.setText("Seed Pods")
            self.textEdit_5.setText("Yellowish-white Bloom, Insignificant")
            #show detected image example
            taroIm = QtGui.QPixmap(os.path.join(os.getcwd(), "taroim.jpg"))
            self.image_2.setPixmap(taroIm)

        
        

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

        # passing the loaded file to test
        global test_img_path
        test_img_path = loadedim

    # passing the weights   
    #def passingInfo(self):
        #self.openWindow.windowText.setText(x)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    leaf = QtWidgets.QDialog()
    ui = Ui_leaf()
    ui.setupUi(leaf)
    leaf.show()

    #ann part
    model_path ="./saved_model.h5"
    global new_model 
    new_model = load_model(model_path)
    # use global for the model
    sys.exit(app.exec_())
