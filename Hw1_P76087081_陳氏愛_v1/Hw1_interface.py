# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hw1_interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Opencv_hw1(object):
    def setupUi(self, Opencv_hw1):
        Opencv_hw1.setObjectName("Opencv_hw1")
        Opencv_hw1.setWindowModality(QtCore.Qt.NonModal)
        Opencv_hw1.setEnabled(True)
        Opencv_hw1.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Opencv_hw1.sizePolicy().hasHeightForWidth())
        Opencv_hw1.setSizePolicy(sizePolicy)
        Opencv_hw1.setMinimumSize(QtCore.QSize(0, 0))
        Opencv_hw1.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(10)
        Opencv_hw1.setFont(font)
        Opencv_hw1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cvHw1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Opencv_hw1.setWindowIcon(icon)
        Opencv_hw1.setStatusTip("")
        Opencv_hw1.setAccessibleName("")
        Opencv_hw1.setAccessibleDescription("")
        Opencv_hw1.setAutoFillBackground(True)
        Opencv_hw1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.btn_OK = QtWidgets.QPushButton(Opencv_hw1)
        self.btn_OK.setGeometry(QtCore.QRect(490, 560, 121, 31))
        self.btn_OK.setObjectName("btn_OK")
        self.btn_cancel = QtWidgets.QPushButton(Opencv_hw1)
        self.btn_cancel.setGeometry(QtCore.QRect(650, 560, 121, 31))
        self.btn_cancel.setObjectName("btn_cancel")
        self.opencv_group = QtWidgets.QGroupBox(Opencv_hw1)
        self.opencv_group.setGeometry(QtCore.QRect(20, 10, 781, 541))
        self.opencv_group.setObjectName("opencv_group")
        self.imgprocess_group = QtWidgets.QGroupBox(self.opencv_group)
        self.imgprocess_group.setGeometry(QtCore.QRect(20, 30, 151, 191))
        self.imgprocess_group.setObjectName("imgprocess_group")
        self.btn_loadimg = QtWidgets.QPushButton(self.imgprocess_group)
        self.btn_loadimg.setGeometry(QtCore.QRect(10, 30, 131, 31))
        self.btn_loadimg.setObjectName("btn_loadimg")
        self.btn_colorcov = QtWidgets.QPushButton(self.imgprocess_group)
        self.btn_colorcov.setGeometry(QtCore.QRect(10, 70, 131, 31))
        self.btn_colorcov.setObjectName("btn_colorcov")
        self.btn_imgflipping = QtWidgets.QPushButton(self.imgprocess_group)
        self.btn_imgflipping.setGeometry(QtCore.QRect(10, 110, 131, 31))
        self.btn_imgflipping.setObjectName("btn_imgflipping")
        self.btn_blending = QtWidgets.QPushButton(self.imgprocess_group)
        self.btn_blending.setGeometry(QtCore.QRect(10, 150, 131, 31))
        self.btn_blending.setObjectName("btn_blending")
        self.adaptive_group = QtWidgets.QGroupBox(self.opencv_group)
        self.adaptive_group.setGeometry(QtCore.QRect(180, 30, 171, 111))
        self.adaptive_group.setObjectName("adaptive_group")
        self.btn_globthreshold = QtWidgets.QPushButton(self.adaptive_group)
        self.btn_globthreshold.setGeometry(QtCore.QRect(30, 30, 131, 31))
        self.btn_globthreshold.setObjectName("btn_globthreshold")
        self.btn_localthreshold = QtWidgets.QPushButton(self.adaptive_group)
        self.btn_localthreshold.setGeometry(QtCore.QRect(30, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_localthreshold.setFont(font)
        self.btn_localthreshold.setObjectName("btn_localthreshold")
        self.convolution_group = QtWidgets.QGroupBox(self.opencv_group)
        self.convolution_group.setGeometry(QtCore.QRect(180, 160, 171, 191))
        self.convolution_group.setObjectName("convolution_group")
        self.btn_gaussian = QtWidgets.QPushButton(self.convolution_group)
        self.btn_gaussian.setGeometry(QtCore.QRect(30, 30, 131, 31))
        self.btn_gaussian.setObjectName("btn_gaussian")
        self.btn_sobelX = QtWidgets.QPushButton(self.convolution_group)
        self.btn_sobelX.setGeometry(QtCore.QRect(30, 70, 131, 31))
        self.btn_sobelX.setObjectName("btn_sobelX")
        self.btn_sobelY = QtWidgets.QPushButton(self.convolution_group)
        self.btn_sobelY.setGeometry(QtCore.QRect(30, 110, 131, 31))
        self.btn_sobelY.setObjectName("btn_sobelY")
        self.btn_magnitude = QtWidgets.QPushButton(self.convolution_group)
        self.btn_magnitude.setGeometry(QtCore.QRect(30, 150, 131, 31))
        self.btn_magnitude.setObjectName("btn_magnitude")
        self.imgtrans_group = QtWidgets.QGroupBox(self.opencv_group)
        self.imgtrans_group.setGeometry(QtCore.QRect(360, 30, 211, 321))
        self.imgtrans_group.setObjectName("imgtrans_group")
        self.inforpara_group = QtWidgets.QGroupBox(self.imgtrans_group)
        self.inforpara_group.setGeometry(QtCore.QRect(10, 20, 191, 251))
        self.inforpara_group.setObjectName("inforpara_group")
        self.parameter_group = QtWidgets.QGroupBox(self.inforpara_group)
        self.parameter_group.setGeometry(QtCore.QRect(10, 20, 171, 181))
        self.parameter_group.setObjectName("parameter_group")
        self.lineEdit_angle = QtWidgets.QLineEdit(self.parameter_group)
        self.lineEdit_angle.setGeometry(QtCore.QRect(50, 20, 81, 31))
        self.lineEdit_angle.setObjectName("lineEdit_angle")
        self.lineEdit_scale = QtWidgets.QLineEdit(self.parameter_group)
        self.lineEdit_scale.setGeometry(QtCore.QRect(50, 60, 81, 31))
        self.lineEdit_scale.setObjectName("lineEdit_scale")
        self.lineEdit_Tx = QtWidgets.QLineEdit(self.parameter_group)
        self.lineEdit_Tx.setGeometry(QtCore.QRect(50, 100, 81, 31))
        self.lineEdit_Tx.setObjectName("lineEdit_Tx")
        self.lineEdit_Ty = QtWidgets.QLineEdit(self.parameter_group)
        self.lineEdit_Ty.setGeometry(QtCore.QRect(50, 140, 81, 31))
        self.lineEdit_Ty.setObjectName("lineEdit_Ty")
        self.label_angle = QtWidgets.QLabel(self.parameter_group)
        self.label_angle.setGeometry(QtCore.QRect(10, 20, 52, 31))
        self.label_angle.setObjectName("label_angle")
        self.label_scale = QtWidgets.QLabel(self.parameter_group)
        self.label_scale.setGeometry(QtCore.QRect(10, 60, 52, 31))
        self.label_scale.setObjectName("label_scale")
        self.label_ty = QtWidgets.QLabel(self.parameter_group)
        self.label_ty.setGeometry(QtCore.QRect(10, 140, 52, 31))
        self.label_ty.setObjectName("label_ty")
        self.label_tx = QtWidgets.QLabel(self.parameter_group)
        self.label_tx.setGeometry(QtCore.QRect(10, 100, 52, 31))
        self.label_tx.setObjectName("label_tx")
        self.label_deg = QtWidgets.QLabel(self.parameter_group)
        self.label_deg.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_deg.setObjectName("label_deg")
        self.label_pixel1 = QtWidgets.QLabel(self.parameter_group)
        self.label_pixel1.setGeometry(QtCore.QRect(140, 100, 31, 31))
        self.label_pixel1.setObjectName("label_pixel1")
        self.label_pixel2 = QtWidgets.QLabel(self.parameter_group)
        self.label_pixel2.setGeometry(QtCore.QRect(140, 140, 31, 31))
        self.label_pixel2.setObjectName("label_pixel2")
        self.btn_roscaltran = QtWidgets.QPushButton(self.inforpara_group)
        self.btn_roscaltran.setGeometry(QtCore.QRect(10, 210, 171, 31))
        self.btn_roscaltran.setObjectName("btn_roscaltran")
        self.btn_prespective = QtWidgets.QPushButton(self.imgtrans_group)
        self.btn_prespective.setGeometry(QtCore.QRect(20, 280, 171, 31))
        self.btn_prespective.setObjectName("btn_prespective")
        self.trainingdata_group = QtWidgets.QGroupBox(self.opencv_group)
        self.trainingdata_group.setGeometry(QtCore.QRect(580, 30, 181, 321))
        self.trainingdata_group.setToolTipDuration(-1)
        self.trainingdata_group.setObjectName("trainingdata_group")
        self.btn_showimgtrain = QtWidgets.QPushButton(self.trainingdata_group)
        self.btn_showimgtrain.setGeometry(QtCore.QRect(10, 30, 161, 31))
        self.btn_showimgtrain.setObjectName("btn_showimgtrain")
        self.btn_showhyper = QtWidgets.QPushButton(self.trainingdata_group)
        self.btn_showhyper.setGeometry(QtCore.QRect(10, 80, 161, 31))
        self.btn_showhyper.setObjectName("btn_showhyper")
        self.btn_trainepoch = QtWidgets.QPushButton(self.trainingdata_group)
        self.btn_trainepoch.setGeometry(QtCore.QRect(10, 130, 161, 31))
        self.btn_trainepoch.setObjectName("btn_trainepoch")
        self.btn_showresulttrain = QtWidgets.QPushButton(self.trainingdata_group)
        self.btn_showresulttrain.setGeometry(QtCore.QRect(10, 180, 161, 31))
        self.btn_showresulttrain.setObjectName("btn_showresulttrain")
        self.btn_inferencetrain = QtWidgets.QPushButton(self.trainingdata_group)
        self.btn_inferencetrain.setGeometry(QtCore.QRect(10, 270, 161, 31))
        self.btn_inferencetrain.setObjectName("btn_inferencetrain")
        self.lineEdit_testimg = QtWidgets.QLineEdit(self.trainingdata_group)
        self.lineEdit_testimg.setGeometry(QtCore.QRect(100, 230, 71, 31))
        self.lineEdit_testimg.setText("")
        self.lineEdit_testimg.setObjectName("lineEdit_testimg")
        self.label_testimg = QtWidgets.QLabel(self.trainingdata_group)
        self.label_testimg.setGeometry(QtCore.QRect(10, 230, 91, 31))
        self.label_testimg.setObjectName("label_testimg")
        self.text_showvalue = QtWidgets.QTextBrowser(self.opencv_group)
        self.text_showvalue.setGeometry(QtCore.QRect(10, 370, 751, 151))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.text_showvalue.setFont(font)
        self.text_showvalue.setObjectName("text_showvalue")
        self.cbb_selecttrain = QtWidgets.QComboBox(self.opencv_group)
        self.cbb_selecttrain.setEnabled(True)
        self.cbb_selecttrain.setGeometry(QtCore.QRect(30, 220, 81, 22))
        self.cbb_selecttrain.setTabletTracking(False)
        self.cbb_selecttrain.setToolTipDuration(-1)
        self.cbb_selecttrain.setStatusTip("")
        self.cbb_selecttrain.setEditable(False)
        self.cbb_selecttrain.setCurrentText("")
        self.cbb_selecttrain.setMinimumContentsLength(0)
        self.cbb_selecttrain.setDuplicatesEnabled(False)
        self.cbb_selecttrain.setFrame(True)
        self.cbb_selecttrain.setModelColumn(0)
        self.cbb_selecttrain.setObjectName("cbb_selecttrain")
        self.label_footer = QtWidgets.QLabel(Opencv_hw1)
        self.label_footer.setGeometry(QtCore.QRect(20, 570, 121, 21))
        self.label_footer.setObjectName("label_footer")

        self.retranslateUi(Opencv_hw1)
        self.cbb_selecttrain.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Opencv_hw1)

    def retranslateUi(self, Opencv_hw1):
        _translate = QtCore.QCoreApplication.translate
        Opencv_hw1.setWindowTitle(_translate("Opencv_hw1", "Hw1_P76087081_陳氏愛"))
        self.btn_OK.setText(_translate("Opencv_hw1", "OK"))
        self.btn_cancel.setText(_translate("Opencv_hw1", "Cancel"))
        self.opencv_group.setTitle(_translate("Opencv_hw1", "Introduction to Image Processing, Computer Vision and Deep Learning"))
        self.imgprocess_group.setTitle(_translate("Opencv_hw1", "1. Image Processing"))
        self.btn_loadimg.setText(_translate("Opencv_hw1", "1.1 Load Image"))
        self.btn_colorcov.setText(_translate("Opencv_hw1", "1.2 Color Conversion"))
        self.btn_imgflipping.setText(_translate("Opencv_hw1", "1.3 Image Flipping"))
        self.btn_blending.setText(_translate("Opencv_hw1", "1.4 Blending"))
        self.adaptive_group.setTitle(_translate("Opencv_hw1", "2. Adaptive Threshold"))
        self.btn_globthreshold.setText(_translate("Opencv_hw1", "2.1 Global Threshold"))
        self.btn_localthreshold.setText(_translate("Opencv_hw1", "2.2 Local Threshold"))
        self.convolution_group.setTitle(_translate("Opencv_hw1", "4. Convolution"))
        self.btn_gaussian.setText(_translate("Opencv_hw1", "4.1 Gaussian"))
        self.btn_sobelX.setText(_translate("Opencv_hw1", "4.2 Sobel X"))
        self.btn_sobelY.setText(_translate("Opencv_hw1", "4.3 Sobel Y"))
        self.btn_magnitude.setText(_translate("Opencv_hw1", "4.4 Magnitude"))
        self.imgtrans_group.setTitle(_translate("Opencv_hw1", "3. Image Transformation"))
        self.inforpara_group.setTitle(_translate("Opencv_hw1", "3.1 Transforms"))
        self.parameter_group.setTitle(_translate("Opencv_hw1", "Parameters"))
        self.label_angle.setText(_translate("Opencv_hw1", "Angle:"))
        self.label_scale.setText(_translate("Opencv_hw1", "Scale:"))
        self.label_ty.setText(_translate("Opencv_hw1", "Ty:"))
        self.label_tx.setText(_translate("Opencv_hw1", "Tx:"))
        self.label_deg.setText(_translate("Opencv_hw1", "deg"))
        self.label_pixel1.setText(_translate("Opencv_hw1", "pixel"))
        self.label_pixel2.setText(_translate("Opencv_hw1", "pixel"))
        self.btn_roscaltran.setText(_translate("Opencv_hw1", "3.1 Rotation, Scaling, Translation"))
        self.btn_prespective.setText(_translate("Opencv_hw1", "3.2 Perspective Transform"))
        self.trainingdata_group.setTitle(_translate("Opencv_hw1", "5. Traning Data"))
        self.btn_showimgtrain.setText(_translate("Opencv_hw1", "5.1 Show Train Image"))
        self.btn_showhyper.setText(_translate("Opencv_hw1", "5.2 Show Hyperparameters"))
        self.btn_trainepoch.setText(_translate("Opencv_hw1", "5.3 Train 1 Epoch"))
        self.btn_showresulttrain.setText(_translate("Opencv_hw1", "5.4 Show Training Result"))
        self.btn_inferencetrain.setText(_translate("Opencv_hw1", "5.5 Inference"))
        self.lineEdit_testimg.setPlaceholderText(_translate("Opencv_hw1", "(0~9999)"))
        self.label_testimg.setText(_translate("Opencv_hw1", "Test Image Index"))
        self.label_footer.setText(_translate("Opencv_hw1", "P76087081_陳氏愛"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Opencv_hw1 = QtWidgets.QWidget()
    ui = Ui_Opencv_hw1()
    ui.setupUi(Opencv_hw1)
    Opencv_hw1.show()
    sys.exit(app.exec_())
