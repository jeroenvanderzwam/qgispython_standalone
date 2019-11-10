from PyQt5.QtWidgets import QApplication
from qgis.core import QgsApplication
import os

from processing.core.Processing import Processing

from qgis.analysis import QgsNativeAlgorithms

from hoofdscherm import Hoofdscherm

app = QApplication([])

qgs = QgsApplication([], False)
qgs.setPrefixPath(os.environ['QGIS_PREFIX_PATH'], True)

Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

qgs.initQgis()

hoofd = Hoofdscherm()
hoofd.show()
app.exec_()
hoofd = None
QgsApplication.exitQgis()