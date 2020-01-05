from qgis.core import *
import os

uitvoeren = True

# pad naar de gpkg aanpassen
style_laag = QgsVectorLayer(r"C:\Users\jeroe\OneDrive\Bureaublad\utrecht_osm\Utrecht.gpkg|layername=layer_styles","style","ogr")

# functie die de styling files inleest
def read_style(type, naam):
   try:
      pad = f'styling/{type}'
      with open(pad + '/' + naam + f'.{type}', 'r') as f:
         return f.read()
   except FileNotFoundError:
      return ''

# elem.attributes()[3] is de naam van de laag. Deze moet gelijk zijn aan de sld
style_laag.startEditing()
for elem in style_laag.getFeatures():  
   if elem.attributes()[3] != NULL:
      print(elem.attributes()[3])
      if uitvoeren:
         style_laag.changeAttributeValue(elem.id(), 6, read_style('qml', elem.attributes()[3]))
         style_laag.changeAttributeValue(elem.id(), 7, read_style('sld', elem.attributes()[3]))

style_laag.commitChanges()

QgsProject.instance().addMapLayer(style_laag)