from qgis.core import *

QgsApplication.setPrefixPath(r'C:\Program Files\QGIS 3.4\apps\qgis')

qgs = QgsApplication([], False)

qgs.initQgis()

laag = QgsVectorLayer(r'D:\Documents\6_GIS\_Basis GIS Data\Rotterdam\Rotterdam_en_omgeving.shp',
                      'naam',
                      'ogr')
print(laag.isValid())

qgs.exitQgis()
