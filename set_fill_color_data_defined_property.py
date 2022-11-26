import qgis
from qgis.utils import iface
from qgis.core import *

target_field_name = "fill"

layers = [tree_layer.layer() for tree_layer in QgsProject.instance().layerTreeRoot().findLayers()]

for layer in layers:
    layerType = layer.type()
    if layerType == QgsMapLayer.VectorLayer:

        single_symbol_renderer = layer.renderer()

        symbol = single_symbol_renderer.symbol()
        symbol_layer = symbol.symbolLayers()[0]
        data_defined = QgsProperty.fromField(target_field_name)  

        symbol_layer.setDataDefinedProperty(QgsSymbolLayer.PropertyFillColor, data_defined)
        layer.triggerRepaint()