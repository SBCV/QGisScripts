import qgis
from qgis.utils import iface
from qgis.core import *

layers = [tree_layer.layer() for tree_layer in QgsProject.instance().layerTreeRoot().findLayers()]

for layer in layers:
    layerType = layer.type()

    if layerType == QgsMapLayer.VectorLayer:

        single_symbol_renderer = layer.renderer()
        symbol = single_symbol_renderer.symbol()
        symbol_layer = symbol.symbolLayers()[0]

        # Revert setDataDefinedProperty()
        symbol_layer.dataDefinedProperties().clear()

        layer.triggerRepaint()
