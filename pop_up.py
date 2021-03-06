import urllib.request
import zipfile
import os
import shutil
import time
import signal

import processing

from PyQt5 import QtCore, QtGui, QtWidgets
from qgis.core import *
from qgis.utils import *

class Ui_Pop_Up(QtWidgets.QDialog):
    def __init__(self, parent, provincie):
        self.provincie = provincie
        super(Ui_Pop_Up, self).__init__()

    def __del__(self):
        temp_path = os.getcwd() + "\\temp"
        while True:
            try:
                if os.path.isdir(temp_path):
                    shutil.rmtree(temp_path)
            except WindowsError:
                time.sleep(2)
            else:
                break
        
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

    def read_style(self, type, naam):
        try:
            pad = f'styling/{type}'
            with open(pad + '/' + naam + f'.{type}', 'r') as f:
                return f.read()
        except FileNotFoundError:
            return ''

    def download_files(self):
        self.Pop_Up.reject()

        # maken van temp folder
        temp_path = os.getcwd() + "\\temp"
        if not os.path.isdir(temp_path): 
            os.mkdir(temp_path)
        
        # downloaden van de zipfile
        zip_, _ = urllib.request.urlretrieve(f'http://download.geofabrik.de/europe/netherlands/{self.provincie.lower()}-latest-free.shp.zip')
        with zipfile.ZipFile(zip_) as zf:
            bestanden = zf.namelist()
            for bestand in bestanden:
                file_pad = os.path.join(temp_path, bestand) 
                with open(file_pad, 'wb') as f:
                    f.write(zf.read(bestand))
        
        shapes = []
        for bestand in os.listdir(temp_path):
            file_pad = os.path.join(temp_path, bestand)
            if os.path.splitext(file_pad)[1] == '.shp':        
                pad, bestand = os.path.split(file_pad)
                
                laag = QgsVectorLayer(file_pad, 'temp','ogr')
                # Punten
                if laag.wkbType() == 1:
                    shape = os.path.join(pad, '1_' + bestand)
                # Lijnen
                elif laag.wkbType() == 5:
                    shape = os.path.join(pad, '2_' + bestand)
                # Polygonen
                elif laag.wkbType() == 6:
                    shape = os.path.join(pad, '3_' + bestand)

                writer = QgsVectorFileWriter.writeAsVectorFormat(laag, shape,'utf-8',driverName='ESRI Shapefile')
                shapes.append(shape)

        # Shapefiles omzetten naar gpkg
        processing.run("native:package", 
                        {'LAYERS': shapes,
                        'OUTPUT':os.path.join(self.lineEdit.text(), f'{self.provincie}.gpkg'),
                        'OVERWRITE':False})
        # Mooie styling van Peter meegeven
        style_laag = QgsVectorLayer(f"{os.path.join(self.lineEdit.text(), self.provincie)}.gpkg|layername=layer_styles","style","ogr")

        style_laag.startEditing()
        for elem in style_laag.getFeatures():  
            if elem.attributes()[3] != NULL:
                style_laag.changeAttributeValue(elem.id(), 6, self.read_style('qml', elem.attributes()[3]))
                style_laag.changeAttributeValue(elem.id(), 7, self.read_style('sld', elem.attributes()[3]))

        style_laag.commitChanges()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pop_Up = QtWidgets.QDialog()
    ui = Ui_Pop_Up()
    ui.setupUi(Pop_Up)
    Pop_Up.show()
    sys.exit(app.exec_())