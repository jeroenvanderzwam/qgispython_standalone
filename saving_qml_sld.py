# als je het niet uitvoert zie je van welke lagen je de qml en de sld opslaat
uitvoeren = True
<<<<<<< HEAD
pad = 'C:\\Users\\jeroe\\OneDrive\\Bureaublad\\Amsterdam_data_postgis_geoserver_openlayers'
=======
locatie = r"D:\Gebruikers\peter\Bureaublad\osm\style"
>>>>>>> 7c75b1256e0788a133f3fc052d4b85de144a1e57

for layer in iface.mapCanvas().layers():
    layerType = layer.type()
    if layerType == QgsMapLayer.VectorLayer:
        name = layer.name()
        print(name)
        if uitvoeren:
            # deze twee paden aanpassen naar behoefte
<<<<<<< HEAD
            pathqml = pad + '\\QML\\' + str(name) + '.qml'  
            pathsld = pad + '\\SLD\\' + str(name) + '.sld'  
=======
            pathqml = locatie + "\\qml\\" + str(name) + '.qml'  
            pathsld = locatie + '\\sld\\' + str(name) + '.sld'  
>>>>>>> 7c75b1256e0788a133f3fc052d4b85de144a1e57
            layer.saveNamedStyle(pathqml)
            layer.saveSldStyle(pathsld)