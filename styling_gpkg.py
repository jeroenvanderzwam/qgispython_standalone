style_laag = QgsVectorLayer(r"C:\Users\jeroe\Downloads\PyQGIS3\Projecten\standalone_qgis\shapefiles\Zeeland.gpkg|layername=layer_styles","style","ogr")
field_names = [f.name() for f in style_laag.fields()]

print(field_names)

for elem in style_laag.getFeatures():  
   #print(dict(zip(field_names, elem.attributes())))
   feat = QgsFeature(style_laag.fields())
   print(elem.attributes())
   feat.setAttributes(list(range(2, 14)))
   (res, outFeats) = style_laag.dataProvider().addFeatures([feat])

QgsProject.instance().addMapLayer(style_laag)