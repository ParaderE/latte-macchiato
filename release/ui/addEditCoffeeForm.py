# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addCoffeForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(694, 270)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 220, 651, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 40, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 60, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(190, 160, 60, 16))
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(361, 40, 81, 16))
        self.label_4.setObjectName("label_4")
        self.sort = QtWidgets.QLineEdit(Dialog)
        self.sort.setGeometry(QtCore.QRect(10, 60, 111, 21))
        self.sort.setObjectName("sort")
        self.roast = QtWidgets.QLineEdit(Dialog)
        self.roast.setGeometry(QtCore.QRect(10, 110, 111, 21))
        self.roast.setObjectName("roast")
        self.is_ground = QtWidgets.QComboBox(Dialog)
        self.is_ground.setGeometry(QtCore.QRect(190, 60, 111, 26))
        self.is_ground.setEditable(False)
        self.is_ground.setObjectName("is_ground")
        self.is_ground.addItem("")
        self.is_ground.addItem("")
        self.price = QtWidgets.QSpinBox(Dialog)
        self.price.setGeometry(QtCore.QRect(10, 180, 111, 24))
        self.price.setMinimum(1)
        self.price.setMaximum(10000)
        self.price.setObjectName("price")
        self.volume = QtWidgets.QSpinBox(Dialog)
        self.volume.setGeometry(QtCore.QRect(190, 180, 111, 24))
        self.volume.setMinimum(1)
        self.volume.setMaximum(10000)
        self.volume.setProperty("value", 1)
        self.volume.setObjectName("volume")
        self.description = QtWidgets.QTextEdit(Dialog)
        self.description.setGeometry(QtCore.QRect(360, 60, 311, 141))
        self.description.setObjectName("description")
        self.id = QtWidgets.QSpinBox(Dialog)
        self.id.setGeometry(QtCore.QRect(70, 10, 48, 24))
        self.id.setObjectName("id")
        self.label_id = QtWidgets.QLabel(Dialog)
        self.label_id.setGeometry(QtCore.QRect(10, 10, 60, 16))
        self.label_id.setObjectName("label_id")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sort"))
        self.label_2.setText(_translate("Dialog", "Roast"))
        self.label_3.setText(_translate("Dialog", "Is ground"))
        self.label_5.setText(_translate("Dialog", "Price"))
        self.label_6.setText(_translate("Dialog", "Volume"))
        self.label_4.setText(_translate("Dialog", "Description"))
        self.sort.setPlaceholderText(_translate("Dialog", "Sort"))
        self.roast.setPlaceholderText(_translate("Dialog", "Roast"))
        self.is_ground.setCurrentText(_translate("Dialog", "Yes"))
        self.is_ground.setItemText(0, _translate("Dialog", "Yes"))
        self.is_ground.setItemText(1, _translate("Dialog", "No"))
        self.label_id.setText(_translate("Dialog", "ID"))
