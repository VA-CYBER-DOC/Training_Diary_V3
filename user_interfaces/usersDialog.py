# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_interfaces\usersDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Users(object):
    def setupUi(self, Dialog_Users):
        Dialog_Users.setObjectName("Dialog_Users")
        Dialog_Users.resize(400, 164)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Users)
        self.buttonBox.setGeometry(QtCore.QRect(110, 130, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.usersComboBox = QtWidgets.QComboBox(Dialog_Users)
        self.usersComboBox.setGeometry(QtCore.QRect(10, 10, 301, 21))
        self.usersComboBox.setObjectName("usersComboBox")

        self.retranslateUi(Dialog_Users)
        self.buttonBox.accepted.connect(Dialog_Users.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog_Users.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog_Users)

    def retranslateUi(self, Dialog_Users):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Users.setWindowTitle(_translate("Dialog_Users", "Dialog"))
