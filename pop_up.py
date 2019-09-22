import urllib.request
import zipfile
import os

import processing

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Pop_Up(QtWidgets.QDialog):
    def __init__(self, parent, provincie):
        self.provincie = provincie
        super(Ui_Pop_Up, self).__init__()
        
    def setupUi(self, Pop_Up):
        self.Pop_Up = Pop_Up
        Pop_Up.setObjectName("Pop_Up")
        Pop_Up.resize(300, 189)
        self.gridLayout = QtWidgets.QGridLayout(Pop_Up)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        self.tekst_provincie = QtWidgets.QLabel(Pop_Up)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tekst_provincie.setFont(font)
        self.tekst_provincie.setObjectName("tekst_provincie")
        self.gridLayout.addWidget(self.tekst_provincie, 0, 0, 1, 2)
        self.tekst_ProvincieNaam = QtWidgets.QLabel(Pop_Up)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tekst_ProvincieNaam.setFont(font)
        self.tekst_ProvincieNaam.setObjectName("tekst_ProvincieNaam")
        self.gridLayout.addWidget(self.tekst_ProvincieNaam, 1, 0, 1, 2)
        self.tekst_opslaglocatie = QtWidgets.QLabel(Pop_Up)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tekst_opslaglocatie.setFont(font)
        self.tekst_opslaglocatie.setObjectName("tekst_opslaglocatie")
        self.gridLayout.addWidget(self.tekst_opslaglocatie, 3, 0, 1, 2)
        self.bladeren = QtWidgets.QPushButton(Pop_Up)
        self.bladeren.setObjectName("bladeren")
        self.gridLayout.addWidget(self.bladeren, 4, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Pop_Up)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(Pop_Up)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 2)

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
        self.Pop_Up.reject()

        shapes = []
        zip_, headers = urllib.request.urlretrieve(f'http://download.geofabrik.de/europe/netherlands/{self.provincie.lower()}-latest-free.shp.zip')
        with zipfile.ZipFile(zip_) as zf:
            bestanden = zf.namelist()
            for bestand in bestanden:
                file_pad = os.path.join(self.lineEdit.text(), bestand)
                if os.path.splitext(file_pad)[1] == '.shp':
                    shapes.append(file_pad)
                with open(file_pad, 'wb') as f:
                    f.write(zf.read(bestand))

        processing.run("native:package", 
                        {'LAYERS': shapes,
                        'OUTPUT':os.path.join(self.lineEdit.text(), f'{self.provincie}.gpkg'),
                        'OVERWRITE':False})


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pop_Up = QtWidgets.QDialog()
    ui = Ui_Pop_Up()
    ui.setupUi(Pop_Up)
    Pop_Up.show()
    sys.exit(app.exec_())

