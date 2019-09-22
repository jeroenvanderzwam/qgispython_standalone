laag = QgsVectorLayer(r"C:\Users\jeroe\Downloads\PyQGIS3\Projecten\standalone_qgis\shapefiles\gis_osm_places_free_1.shp",'Kerken en shit','ogr')
gpkgPad = r'C:\Users\jeroe\Desktop\test.gpkg'

options = QgsVectorFileWriter.SaveVectorOptions()
options.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteLayer 
options.layerName = "_".join(laag.name().split(' '))
_writer = QgsVectorFileWriter.writeAsVectorFormat(laag, gpkgPad, options)
if _writer:
    print(laag.name(), _writer)
    
del _writer