from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from pytube import YouTube


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(700, 820)

        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(QtCore.Qt.transparent)
        icon = QIcon(transparent_pixmap)
        MainWindow.setWindowIcon(icon)

        MainWindow.setStyleSheet("background: #D9D9D9;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: #D9D9D9;")
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Jockey One")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

        self.url_label = QtWidgets.QLabel(self.centralwidget)
        self.url_label.setGeometry(QtCore.QRect(100, 190, 221, 51))
        self.url_label.setFont(font)
        self.url_label.setStyleSheet("font: bold 16pt \"Jockey One\";")
        self.url_label.setObjectName("url_label")


        self.Search_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Search_Button.setGeometry(QtCore.QRect(500, 280, 101, 33))
        self.Search_Button.setStyleSheet("border-radius: 10px;\n"
                                         "background: #747474;\n"
                                         "width: 107px;\n"
                                         "height: 35px;\n"
                                         "color: #FFF;\n"
                                         "font-size: 20px;\n"
                                         "font-family: Fira Sans;\n"
                                         "font-style: normal;\n"
                                         "font-weight: 400;\n"
                                         "line-height: normal;")
        self.Search_Button.setFlat(False)
        self.Search_Button.setObjectName("Search_Button")
        self.Search_Button.clicked.connect(self.download_video)



        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 240, 501, 34))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border-radius: 5px;\n"
                                    "background: #FFF;\n"
                                    "padding-left: 10px;\n"
                                    "color: #747474;\n"
                                    "font-size: 16px;\n"
                                    "font-family: Fira Sans;\n"
                                    "font-style: normal;\n"
                                    "font-weight: 400;\n"
                                    "line-height: normal;")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setObjectName("textEdit")
        self.miniature = QtWidgets.QLabel(self.centralwidget)
        self.miniature.setGeometry(QtCore.QRect(100, 340, 232, 163))
        self.miniature.setMinimumSize(QtCore.QSize(232, 163))
        self.miniature.setMaximumSize(QtCore.QSize(232, 163))
        self.miniature.setStyleSheet("background: #FFF;\n"
                                     "")
        self.miniature.setText("")
        self.miniature.setObjectName("miniature")
        self.title = QtWidgets.QTextEdit(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(380, 450, 221, 21))
        self.title.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setObjectName("title")
        self.duration = QtWidgets.QTextEdit(self.centralwidget)
        self.duration.setGeometry(QtCore.QRect(380, 390, 221, 21))
        self.duration.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.duration.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.duration.setObjectName("duration")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 530, 151, 41))
        self.label.setStyleSheet("font: bold 22pt \"Jockey One\";")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 580, 501, 35))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "color: #747474;\n"
                                    "font-size: 16px;\n"
                                    "font-family: Fira Sans;\n"
                                    "font-style: normal;\n"
                                    "font-weight: 400;\n"
                                    "line-height: normal;\n"
                                    "padding-left: 10px;")
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 630, 201, 41))
        self.label_2.setStyleSheet("font: bold 22pt \"Jockey One\";")
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 680, 391, 34))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("border-radius: 5px;\n"
                                      "background: #FFF;\n"
                                      "padding-left: 10px;\n"
                                      "color: #747474;\n"
                                      "font-size: 16px;\n"
                                      "font-family: Fira Sans;\n"
                                      "font-style: normal;\n"
                                      "font-weight: 400;\n"
                                      "line-height: normal;")
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_2.setObjectName("textEdit_2")

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(110, -50, 577, 293))
        self.logo.setObjectName("logo")
        pixmap = QPixmap("logo.png")
        self.logo.setPixmap(pixmap)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 410, 151, 41))
        self.label_4.setStyleSheet("font: bold 12pt \"Jockey One\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 350, 151, 41))
        self.label_5.setStyleSheet("font: bold 12pt \"Jockey One\";")
        self.label_5.setObjectName("label_5")
        self.Search_Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Search_Button_2.setGeometry(QtCore.QRect(500, 680, 101, 33))
        self.Search_Button_2.setStyleSheet("border-radius: 10px;\n"
                                           "background: #747474;\n"
                                           "width: 107px;\n"
                                           "height: 35px;\n"
                                           "color: #FFF;\n"
                                           "font-size: 20px;\n"
                                           "font-family: Fira Sans;\n"
                                           "font-style: normal;\n"
                                           "font-weight: 400;\n"
                                           "line-height: normal;")
        self.Search_Button_2.setFlat(False)
        self.Search_Button_2.setObjectName("Search_Button_2")
        self.Search_Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Search_Button_3.setGeometry(QtCore.QRect(260, 750, 181, 38))
        self.Search_Button_3.setStyleSheet("border-radius: 10px;\n"
                                           "background: #39A728;\n"
                                           "width: 107px;\n"
                                           "height: 35px;\n"
                                           "color: #FFF;\n"
                                           "font-size: 20px;\n"
                                           "font-family: Fira Sans;\n"
                                           "font-style: normal;\n"
                                           "font-weight: 400;\n"
                                           "line-height: normal;")
        self.Search_Button_3.setFlat(False)
        self.Search_Button_3.setObjectName("Search_Button_3")
        self.label_4.raise_()
        self.logo.raise_()
        self.url_label.raise_()
        self.Search_Button.raise_()
        self.textEdit.raise_()
        self.miniature.raise_()
        self.title.raise_()
        self.duration.raise_()
        self.label.raise_()
        self.comboBox.raise_()
        self.label_2.raise_()
        self.textEdit_2.raise_()
        self.label_5.raise_()
        self.Search_Button_2.raise_()
        self.Search_Button_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.url_label.setText(_translate("MainWindow", "Enter the URL:"))
        self.Search_Button.setText(_translate("MainWindow", "SEARCH"))
        self.label.setText(_translate("MainWindow", "File Type:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "teste"))
        self.comboBox.setItemText(1, _translate("MainWindow", "teste2"))
        self.label_2.setText(_translate("MainWindow", "File Location:"))
        self.label_4.setText(_translate("MainWindow", "Duration:"))
        self.label_5.setText(_translate("MainWindow", "Title:"))
        self.Search_Button_2.setText(_translate("MainWindow", "BROWSE"))
        self.Search_Button_3.setText(_translate("MainWindow", "DOWNLOAD"))

    def download_video(self):
        url = self.textEdit.toPlainText()
        try:
            yt = YouTube(url)
            video = yt.streams.get_lowest_resolution()
            if video is not None:
                video.download()
                print("Download concluído.")
            else:
                print("Não foi possível encontrar uma versão de maior resolução para download.")
        except Exception as e:
            print("Erro durante o download:", str(e))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
