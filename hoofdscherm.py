import os

from PyQt5.QtWidgets import QFrame, QGridLayout, QMainWindow, QAction
from PyQt5.QtGui import QIcon
from qgis.gui import QgsMapCanvas, QgsMapToolZoom
from qgis.core import QgsProject, QgsVectorLayer

class Hoofdscherm(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.setupGui()
        self.project = QgsProject()
        self.ogr_laag_toevoegen(r"C:\Users\jeroe\Downloads\PyQGIS3\Files\data\alaska.shp")
        self.map_canvas.zoomToFullExtent()

    def setupGui(self):
        frame = QFrame(self)
        self.setCentralWidget(frame)
        self.grid_layout = QGridLayout(frame)

        self.map_canvas = QgsMapCanvas()
        self.grid_layout.addWidget(self.map_canvas)

        # Setup action for zoom in tool
        self.zoomin_action = QAction(
            QIcon(":/osm/zoomin_icoon"),
            "Zoom In",
            self)
        # create toolbar
        self.toolbar = self.addToolBar("Map Tools")
        self.toolbar.addAction(self.zoomin_action)

        # connect the tool
        self.zoomin_action.triggered.connect(self.zoom_in)

        # create the map tool
        self.tool_zoomin = QgsMapToolZoom(self.map_canvas, False)

    def ogr_laag_toevoegen(self, pad):
        naam, ext = os.path.basename(pad).split('.')
        laag = QgsVectorLayer(pad, naam, 'ogr')
        self.project.addMapLayer(laag)
        self.map_canvas.setLayers([laag])

    def zoom_in(self):
        self.map_canvas.setMapTool(self.tool_zoomin)
