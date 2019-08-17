from qgis.core import *
import sys
import os

from processing.core.Processing import Processing
import processing
from qgis.analysis import QgsNativeAlgorithms

import os
import urllib.request
import zipfile
import tempfile

# Initialiseren van QGIS (zonder gui)
QgsApplication.setPrefixPath(r'C:\Program Files\QGIS 3.4\apps\qgis', True)
app = QgsApplication([], False)
QgsApplication.initQgis()

# nodig voor processing toolbox
Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

# Download en unzip de meeste recente shapefilerint('Downloading file')
temp_bestand = tempfile.mkdtemp()
zip_, headers = urllib.request.urlretrieve('http://download.geofabrik.de/australia-oceania/fiji-latest-free.shp.zip')
with zipfile.ZipFile(zip_) as zf:
    bestanden = zf.namelist()
    for bestand in bestanden:
        if 'roads' in bestand:
            file_pad = os.path.join(temp_bestand, bestand)
            with open(file_pad, 'wb') as f:
                f.write(zf.read(bestand))

            if bestand == 'gis_osm_roads_free_1.shp':
                roads_shp_path = file_pad
                
print(f'Gedownload naar: {roads_shp_path} ')

print('Herprojecteren van de wegen laag')

argumenten = {'INPUT': roads_shp_path,
              'TARGET_CRS': 'EPSG:3460'}

ret = processing.run('qgis:reprojectlayer', argumenten)
output = ret['OUTPUT']

print('Opschonen van de wegen laag')
argumenten = {'input': output, 'type': 1, 'tool':1, 'threshold': 1, 'output': 'output.shp', 
                'error': 'error.shp','GRASS_OUTPUT_TYPE_PARAMETER':0}

# Uitleg van de verschillende argumenten van het algoritme
# processing.algorithmHelp('grass7:v.clean')	   
ret = processing.run('grass7:v.clean', argumenten)
print('Succes')
