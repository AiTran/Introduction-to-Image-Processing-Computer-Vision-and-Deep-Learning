# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\HW2_interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget_HW2(object):
    def setupUi(self, Widget_HW2):
        Widget_HW2.setObjectName("Widget_HW2")
        Widget_HW2.resize(500, 380)
        Widget_HW2.setMinimumSize(QtCore.QSize(500, 380))
        Widget_HW2.setMaximumSize(QtCore.QSize(500, 380))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cvHw1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Widget_HW2.setWindowIcon(icon)
        self.group_opencvdl = QtWidgets.QGroupBox(Widget_HW2)
        self.group_opencvdl.setGeometry(QtCore.QRect(20, 20, 451, 311))
        self.group_opencvdl.setObjectName("group_opencvdl")
        self.group_stereo2 = QtWidgets.QGroupBox(self.group_opencvdl)
        self.group_stereo2.setGeometry(QtCore.QRect(20, 40, 211, 111))
        self.group_stereo2.setObjectName("group_stereo2")
        self.btn_disparity2 = QtWidgets.QPushButton(self.group_stereo2)
        self.btn_disparity2.setGeometry(QtCore.QRect(20, 40, 171, 41))
        self.btn_disparity2.setObjectName("btn_disparity2")
        self.group_BS = QtWidgets.QGroupBox(self.group_opencvdl)
        self.group_BS.setGeometry(QtCore.QRect(20, 190, 211, 111))
        self.group_BS.setObjectName("group_BS")
        self.btn_BS = QtWidgets.QPushButton(self.group_BS)
        self.btn_BS.setGeometry(QtCore.QRect(20, 40, 171, 41))
        self.btn_BS.setObjectName("btn_BS")
        self.group_AR = QtWidgets.QGroupBox(self.group_opencvdl)
        self.group_AR.setGeometry(QtCore.QRect(250, 200, 181, 101))
        self.group_AR.setObjectName("group_AR")
        self.btn_AR = QtWidgets.QPushButton(self.group_AR)
        self.btn_AR.setGeometry(QtCore.QRect(20, 30, 141, 41))
        self.btn_AR.setObjectName("btn_AR")
        self.group_FT = QtWidgets.QGroupBox(self.group_opencvdl)
        self.group_FT.setGeometry(QtCore.QRect(250, 40, 181, 151))
        self.group_FT.setObjectName("group_FT")
        self.btn_preprocessing = QtWidgets.QPushButton(self.group_FT)
        self.btn_preprocessing.setGeometry(QtCore.QRect(20, 30, 141, 41))
        self.btn_preprocessing.setObjectName("btn_preprocessing")
        self.btn_videotracking = QtWidgets.QPushButton(self.group_FT)
        self.btn_videotracking.setGeometry(QtCore.QRect(20, 90, 141, 41))
        self.btn_videotracking.setObjectName("btn_videotracking")
        self.label_myname = QtWidgets.QLabel(Widget_HW2)
        self.label_myname.setGeometry(QtCore.QRect(30, 340, 221, 21))
        self.label_myname.setObjectName("label_myname")

        self.retranslateUi(Widget_HW2)
        QtCore.QMetaObject.connectSlotsByName(Widget_HW2)

    def retranslateUi(self, Widget_HW2):
        _translate = QtCore.QCoreApplication.translate
        Widget_HW2.setWindowTitle(_translate("Widget_HW2", "HW2_P76087081_TranThiAi"))
        self.group_opencvdl.setTitle(_translate("Widget_HW2", "OpenCVDL"))
        self.group_stereo2.setTitle(_translate("Widget_HW2", "1. Stereo"))
        self.btn_disparity2.setText(_translate("Widget_HW2", "1.1 Disparity"))
        self.group_BS.setTitle(_translate("Widget_HW2", "2. Background Subtraction"))
        self.btn_BS.setText(_translate("Widget_HW2", "2.1 Background Subtraction"))
        self.group_AR.setTitle(_translate("Widget_HW2", "4. Augmented Reality"))
        self.btn_AR.setText(_translate("Widget_HW2", "4.1 Augmented Reality"))
        self.group_FT.setTitle(_translate("Widget_HW2", "3. Feature Tracking"))
        self.btn_preprocessing.setText(_translate("Widget_HW2", "3.1 Preprocessing"))
        self.btn_videotracking.setText(_translate("Widget_HW2", "3.2 Video Tracking"))
        self.label_myname.setText(_translate("Widget_HW2", "HW2_P76087081_TranThiAi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget_HW2 = QtWidgets.QWidget()
    ui = Ui_Widget_HW2()
    ui.setupUi(Widget_HW2)
    Widget_HW2.show()
    sys.exit(app.exec_())
