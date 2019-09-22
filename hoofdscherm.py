import urllib.request
import zipfile
import os

from PyQt5.QtWidgets import QFrame, QGridLayout, QMainWindow, QAction
from PyQt5.QtGui import QIcon
from qgis.gui import QgsMapCanvas, QgsMapToolZoom, QgsMapToolPan, QgsMapToolEmitPoint
from qgis.core import QgsProject, QgsVectorLayer, QgsRasterLayer, QgsGeometry, QgsPointXY

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
        self.osm_action = QAction(
            QIcon(":/osm/osm_data"),
            "Zoom In",
            self)
        # Setup action for pan tool
        self.pan_action = QAction(
            QIcon(":/osm/pan"),
            "Pan",
            self)
        # Setup action for ZoomIn tool
        self.zoomIn_action = QAction(
            QIcon(":/osm/ZoomIn"),
            "Zoom in",
            self)
        # Setup action for ZoomOut tool
        self.zoomOut_action = QAction(
            QIcon(":/osm/ZoomOut"),
            "Zoom out",
            self)
        # create toolbar
        self.toolbar = self.addToolBar("Map Tools")
        self.toolbar.addAction(self.osm_action)
        self.toolbar.addAction(self.pan_action)
        self.toolbar.addAction(self.zoomIn_action)
        self.toolbar.addAction(self.zoomOut_action)

        self.osm_action.triggered.connect(self.osm_tool)
        self.pan_action.triggered.connect(self.pan_tool)
        self.zoomIn_action.triggered.connect(self.zoomIn_tool)
        self.zoomOut_action.triggered.connect(self.zoomOut_tool)
   
    def krijg_provincienaam(self, point, mouse_button): 

        layer = self.project.mapLayersByName('Provinciegrenzen')[0]
        feats = [ feat for feat in layer.getFeatures() ]

        geo_pt = QgsGeometry.fromPointXY(QgsPointXY(point.x(), point.y()))

        id = -1

        for feat in feats:
            if geo_pt.within(feat.geometry()):
                id = feat.id()
                provincie = feat.attribute('Provincienaam')
                break

        if id != -1:
            self.download_files(provincie)
        else:
            print ("Geen provincie aangeklikt.")
        
    def osm_tool(self):
        self.tool_osm = QgsMapToolEmitPoint(self.map_canvas)
        self.tool_osm.canvasClicked.connect(self.krijg_provincienaam)
        self.map_canvas.setMapTool(self.tool_osm)
    
    def pan_tool(self):
        self.tool_pan = QgsMapToolPan(self.map_canvas)
        self.map_canvas.setMapTool(self.tool_pan)
        
    def zoomIn_tool(self):
        self.tool_zoomin = QgsMapToolZoom(self.map_canvas, False)
        self.map_canvas.setMapTool(self.tool_zoomin)
        
    def zoomOut_tool(self):
        self.tool_zoomout = QgsMapToolZoom(self.map_canvas, True)
        self.map_canvas.setMapTool(self.tool_zoomout)

    def download_files(self, provincie):
        locatie = r'C:\Users\jeroe\Downloads\PyQGIS3\Projecten\standalone_qgis\shapefiles'

        zip_, headers = urllib.request.urlretrieve(f'http://download.geofabrik.de/europe/netherlands/{provincie.lower()}-latest-free.shp.zip')
        with zipfile.ZipFile(zip_) as zf:
            bestanden = zf.namelist()
            for bestand in bestanden:
                file_pad = os.path.join(locatie, bestand)

                with open(file_pad, 'wb') as f:
                    f.write(zf.read(bestand))
