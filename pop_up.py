import urllib.request
import zipfile
import os

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Pop_Up(object):
    def __init__(self, parent, provincie):
        self.provincie = provincie
        super(Ui_Pop_Up, self).__init__()
        
    def setupUi(self, Pop_Up):
        self.Pop_Up = Pop_Up
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
        self.buttonBox.accepted.connect(self.download_files)
        self.buttonBox.rejected.connect(Pop_Up.reject)
        QtCore.QMetaObject.connectSlotsByName(Pop_Up)

        self.bladeren.clicked.connect(self.select_folder)

    def retranslateUi(self, Pop_Up):
        _translate = QtCore.QCoreApplication.translate
        Pop_Up.setWindowTitle(_translate("Pop_Up", "Dialog"))
        self.bladeren.setText(_translate("Pop_Up", "..."))
        self.tekst_provincie.setText(_translate("Pop_Up", "Geselecteerde Provincie:"))
        self.tekst_ProvincieNaam.setText(_translate("Pop_Up", self.provincie))
        self.tekst_opslaglocatie.setText(_translate("Pop_Up", "Opslaglocatie:"))

    def select_folder(self):
        file = str(QtWidgets.QFileDialog.getExistingDirectory(self.Pop_Up, "Select Directory"))
        self.lineEdit.setText(file)

    def download_files(self):
        print(self.provincie)
        zip_, headers = urllib.request.urlretrieve(f'http://download.geofabrik.de/europe/netherlands/{self.provincie.lower()}-latest-free.shp.zip')
        with zipfile.ZipFile(zip_) as zf:
            bestanden = zf.namelist()
            for bestand in bestanden:
                file_pad = os.path.join(self.lineEdit.text(), bestand)

                with open(file_pad, 'wb') as f:
                    f.write(zf.read(bestand))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pop_Up = QtWidgets.QDialog()
    ui = Ui_Pop_Up()
    ui.setupUi(Pop_Up)
    Pop_Up.show()
    sys.exit(app.exec_())

