from qgis.core import *

from processing.core.Processing import Processing
import processing
from qgis.analysis import QgsNativeAlgorithms

# Initialiseren van QGIS
QgsApplication.setPrefixPath(r'C:\Program Files\QGIS 3.4\apps\qgis', True)
app = QgsApplication([], False)
QgsApplication.initQgis()

# nodig voor processing toolbox
Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
    
print('Herprojecteren van de wegen laag')

argumenten = {'INPUT': r"C:\Users\jeroe\Downloads\PyQGIS3\Projecten\standalone_qgis\data\gis_osm_roads_free_1.shp",
              'TARGET_CRS': 'EPSG:3460',
              'OUTPUT': "memory:layer"}

ret = processing.run('qgis:reprojectlayer', argumenten)
output = ret['OUTPUT']

