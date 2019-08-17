import os

from PyQt5.QtWidgets import QFrame, QGridLayout, QMainWindow, QAction
from PyQt5.QtGui import QIcon
from qgis.gui import QgsMapCanvas, QgsMapToolZoom
from qgis.core import QgsProject, QgsVectorLayer, QgsRasterLayer

import resources

class Hoofdscherm(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.setupGui()

        self.project = QgsProject()
        urlWithParams = 'type=xyz&url=http://a.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0&crs=EPSG3857'
        rlaag = QgsRasterLayer(urlWithParams, 'OpenStreetMap', 'wms')
        if rlaag.isValid():
            self.project.addMapLayer(rlaag)
        else:
            print('invalid layer')

        path_to_gpkg = os.path.join(QgsProject.instance().homePath(), "GIS_Data_3857.gpkg")

        vlayerNamesList = ['Landsgrens','Gemeentegrenzen','Provinciegrenzen']
        
        lagen = []
        for layer in vlayerNamesList:
            gpkg_layer = path_to_gpkg + "|layername=" + layer

            vlaag = QgsVectorLayer(gpkg_layer, layer, "ogr")
            if not vlaag.isValid():
                print("Layer failed to load!")
            else:
                self.project.addMapLayer(vlaag)
                lagen.append(vlaag)

            self.map_canvas.setLayers( lagen + [rlaag])

        extent = lagen[0].extent()
        self.map_canvas.setExtent(extent)

    def setupGui(self):
        frame = QFrame(self)
        frame.setMinimumSize(1400, 800)

        self.setCentralWidget(frame)
        
        self.grid_layout = QGridLayout(frame)

        self.map_canvas = QgsMapCanvas()
        self.grid_layout.addWidget(self.map_canvas)

        # Setup action for zoom in tool
        self.zoomin_action = QAction(
            QIcon(":/osm/osm_data"),
            "Zoom In",
            self)
        # create toolbar
        self.toolbar = self.addToolBar("Map Tools")
        self.toolbar.addAction(self.zoomin_action)

        self.zoomin_action.triggered.connect(self.zoom_in)

        self.tool_zoomin = QgsMapToolZoom(self.map_canvas, False)

    def zoom_in(self):
        self.map_canvas.setMapTool(self.tool_zoomin)
