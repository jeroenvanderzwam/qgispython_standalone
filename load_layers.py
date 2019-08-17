import os

# get the path to a geopackage  e.g. /home/project/data/data.gpkg
path_to_gpkg = os.path.join(QgsProject.instance().homePath(), "GIS_Data.gpkg")
# specify the layernames from the gpkg to load.
vlayerNamesList = ['Landsgrens','Gemeentegrenzen','Provinciegrenzen']

def loadVectorLayers(gpkgPath, vlayerList):
    for layer in vlayerList:
        # append the layername part
        gpkg_layer = gpkgPath + "|layername=" + layer
        # e.g. gpkg_places_layer = "/home/project/data/data.gpkg|layername=places"
        vlayer = QgsVectorLayer(gpkg_layer, layer, "ogr")
        if not vlayer.isValid():
            print("Layer failed to load!")
        else:
            QgsProject.instance().addMapLayer(vlayer)

def loadOSM():
    urlWithParams = 'type=xyz&url=http://a.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0&crs=EPSG3857'
    rlayer = QgsRasterLayer(urlWithParams, 'OpenStreetMap', 'wms')
    if rlayer.isValid():
        QgsProject.instance().addMapLayer(rlayer)
    else:
        print('invalid layer')

loadOSM()
loadVectorLayers(path_to_gpkg,vlayerNamesList)