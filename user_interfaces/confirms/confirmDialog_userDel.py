# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_interfaces\confirmDialog_userDel.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Confirm_User_Del(object):
    def setupUi(self, Dialog_Confirm_User_Del):
        Dialog_Confirm_User_Del.setObjectName("Dialog_Confirm_User_Del")
        Dialog_Confirm_User_Del.resize(362, 79)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Confirm_User_Del)
        self.buttonBox.setGeometry(QtCore.QRect(90, 40, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog_Confirm_User_Del)
        self.label.setGeometry(QtCore.QRect(0, 10, 371, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog_Confirm_User_Del)
        self.buttonBox.accepted.connect(Dialog_Confirm_User_Del.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog_Confirm_User_Del.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog_Confirm_User_Del)

    def retranslateUi(self, Dialog_Confirm_User_Del):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Confirm_User_Del.setWindowTitle(_translate("Dialog_Confirm_User_Del", "Dialog"))
        self.label.setText(_translate("Dialog_Confirm_User_Del", "Вы уверенны? Все данные пользователя будут удаленны"))
