### Dit is een standalone python qgis applicatie. Gebouwd in windows. Hiervoor is het wel noodzakelijk dat QGIS is geinstalleerd. Daarnaast is het belangrijk dat er padvariabelen ingesteld worden voor de applicatie kan worden gebruikt. Kijk hieronder voor meer informatie.

    SET OSGEO4W_ROOT=C:\OSGeo4W64
    call "%OSGEO4W_ROOT%"\bin\o4w_env.bat
    call "%OSGEO4W_ROOT%"\apps\grass\grass76\etc\env.bat

    path %PATH%;%OSGEO4W_ROOT%\apps\qgis\bin
    path %PATH%;%OSGEO4W_ROOT%\apps\grass\grass76\lib
    path %PATH%;%OSGEO4W_ROOT%\apps\Qt5\bin
    path %PATH%;%OSGEO4W_ROOT%\apps\Python37\Scripts

    set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python
    set PYTHONHOME=%OSGEO4W_ROOT%\apps\Python37
    set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python\plugins\processing
    set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python\plugins

    set QT_QPA_PLATFORM_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\Qt5\plugins\platforms
    set QGIS_PREFIX_PATH=%OSGEO4W_ROOT%\apps\qgis

    set GDAL_DATA=%OSGEO4W_ROOT%\share\gdal
