# from qgis.core import *

# from processing.core.Processing import Processing
# import processing
# from qgis.analysis import QgsNativeAlgorithms

# Initialiseren van QGIS (zonder gui)
# QgsApplication.setPrefixPath(r'C:\Program Files\QGIS 3.4\apps\qgis', True)
# app = QgsApplication([], False)
# QgsApplication.initQgis()

# nodig voor processing toolbox
# Processing.initialize()
# QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
    
# print('Herprojecteren van de wegen laag')

# argumenten = {'INPUT': roads_shp_path,
#               'TARGET_CRS': 'EPSG:3460',
#               'OUTPUT': "memory:layer"}

# ret = processing.run('qgis:reprojectlayer', argumenten)
# output = ret['OUTPUT']

# print('Opschonen van de wegen laag')
# argumenten = {'input': output, 'type': 1, 'tool':1, 'threshold': 1, 
#               'output': 'shapefiles/output.shp', 
#               'error': 'shapefiles/error.shp',
#               'GRASS_OUTPUT_TYPE_PARAMETER':0}

# Uitleg van de verschillende argumenten van het algoritme
# processing.algorithmHelp('grass7:v.clean')
# 	   
# processing.run('grass7:v.clean', argumenten)
# print('Succes')
