# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pop_up.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Pop_Up(object):
    def __init__(self, parent):
        super(Ui_Pop_Up, self).__init__()
        
    def setupUi(self, Pop_Up):
        Pop_Up.setObjectName("Pop_Up")
        Pop_Up.resize(200, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Pop_Up)
        self.buttonBox.setGeometry(QtCore.QRect(10, 260, 180, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.bladeren = QtWidgets.QPushButton(Pop_Up)
        self.bladeren.setGeometry(QtCore.QRect(130, 190, 60, 20))
        self.bladeren.setObjectName("bladeren")
        self.tekst_provincie = QtWidgets.QLabel(Pop_Up)
        self.tekst_provincie.setGeometry(QtCore.QRect(10, 10, 180, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tekst_provincie.setFont(font)
        self.tekst_provincie.setObjectName("tekst_provincie")
        self.lineEdit = QtWidgets.QLineEdit(Pop_Up)
        self.lineEdit.setGeometry(QtCore.QRect(10, 190, 110, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.tekst_ProvincieNaam = QtWidgets.QLabel(Pop_Up)
        self.tekst_ProvincieNaam.setGeometry(QtCore.QRect(10, 40, 180, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tekst_ProvincieNaam.setFont(font)
        self.tekst_ProvincieNaam.setObjectName("tekst_ProvincieNaam")
        self.tekst_opslaglocatie = QtWidgets.QLabel(Pop_Up)
        self.tekst_opslaglocatie.setGeometry(QtCore.QRect(10, 150, 180, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tekst_opslaglocatie.setFont(font)
        self.tekst_opslaglocatie.setObjectName("tekst_opslaglocatie")

        self.retranslateUi(Pop_Up)
        self.buttonBox.accepted.connect(Pop_Up.accept)
        self.buttonBox.rejected.connect(Pop_Up.reject)
        QtCore.QMetaObject.connectSlotsByName(Pop_Up)

    def retranslateUi(self, Pop_Up):
        _translate = QtCore.QCoreApplication.translate
        Pop_Up.setWindowTitle(_translate("Pop_Up", "Dialog"))
        self.bladeren.setText(_translate("Pop_Up", "..."))
        self.tekst_provincie.setText(_translate("Pop_Up", "Geselecteerde Provincie:"))
        self.tekst_ProvincieNaam.setText(_translate("Pop_Up", "TextLabel"))
        self.tekst_opslaglocatie.setText(_translate("Pop_Up", "Opslaglocatie:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pop_Up = QtWidgets.QDialog()
    ui = Ui_Pop_Up()
    ui.setupUi(Pop_Up)
    Pop_Up.show()
    sys.exit(app.exec_())

