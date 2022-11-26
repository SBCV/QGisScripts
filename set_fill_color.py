import qgis
from qgis.utils import iface
from qgis.core import *
from PyQt5.QtGui import QColor

target_field_name = "fill"

# Data defined properties override the fill color and
#  could hide the changes applied by this script.
clear_data_defined_properties = True

layers = [tree_layer.layer() for tree_layer in QgsProject.instance().layerTreeRoot().findLayers()]

for layer in layers:
    # print(layer.name())

    if layer.type() != QgsMapLayer.VectorLayer:
        continue

    # Note: One can not use "layer.fields()" to read the values,
    #  since these are stored alongside the features (and not fields)
    layer_fields = layer.fields()
    fill_index = layer_fields.indexFromName(target_field_name)

    single_symbol_renderer = layer.renderer()
    symbol = single_symbol_renderer.symbol()
    symbol_layer = symbol.symbolLayers()[0]

    if clear_data_defined_properties:
        symbol_layer.dataDefinedProperties().clear()

    # Use the first feature as reference
    reference_feature = next(layer.getFeatures())
    available_attributes = reference_feature.attributes()
    if len(available_attributes) == 0:
        continue

    # The fill attribute is a hex-string representing the color
    fill_attribute = available_attributes[fill_index]
    
    color = QColor(fill_attribute)  
    symbol_layer.setFillColor(color)
    layer.triggerRepaint()
