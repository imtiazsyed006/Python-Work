from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QWidget, QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot, QObject
from PyQt5.QtGui import QImage, QPixmap
import cv2
import sys
import time

## Some Global Variable
height = [0]
width  = [0]

buttonStatus = [0]

## IP Camera Class ##
class Thread(QObject):
    changePixmap = pyqtSignal(QImage)
    
    def run(self):
        
        cap = cv2.VideoCapture('rtsp://10.1.17.206/user=admin&password=&channel=1&stream=0.sdp?real_stream--rtp-caching=100')
        while True:
            
            ret, frame = cap.read()
            if ret and buttonStatus[0] != 0:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888).scaled(height[0],width[0], aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
                # p = convertToQtFormat.
                self.changePixmap.emit(convertToQtFormat)



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        H = self.label.frameGeometry().height()
        W = self.label.frameGeometry().width()    
        height[0] = H
        width[0] = W
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.showImage()
        self.pushButton.clicked.connect(self.buttonPressed)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start IP Cam"))
        
        # self.label.setText(_translate("MainWindow", "TextLabel"))

    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image)) 
        H = self.label.frameGeometry().height()
        W = self.label.frameGeometry().width()    
        height[0] = H
        width[0] = W


    def showImage(self):
        self.thread = QThread()
        self.worker = Thread()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.thread.start()
        self.worker.changePixmap.connect(self.setImage)

    def buttonPressed(self):
        if buttonStatus[0] == 0:
            buttonStatus[0] = 1
            self.pushButton.setText("Stop IP Cam")
        else:
            buttonStatus[0] = 0
            self.pushButton.setText("Start IP Cam")
            self.label.setText(" ")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
