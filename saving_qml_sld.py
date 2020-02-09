# als je het niet uitvoert zie je van welke lagen je de qml en de sld opslaat
uitvoeren = True
pad = 'C:\\Users\\jeroe\\OneDrive\\Bureaublad\\Amsterdam_data_postgis_geoserver_openlayers'

for layer in iface.mapCanvas().layers():
    layerType = layer.type()
    if layerType == QgsMapLayer.VectorLayer:
        name = layer.name()
        print(name)
        if uitvoeren:
            # deze twee paden aanpassen naar behoefte
            pathqml = locatie + "\\qml\\" + str(name) + '.qml'  
            pathsld = locatie + '\\sld\\' + str(name) + '.sld'  
            layer.saveNamedStyle(pathqml)
            layer.saveSldStyle(pathsld)