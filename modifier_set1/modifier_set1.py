from modifier_set1.biostratigraphy.biostratigraphy import biostratigraphy
from modifier_set1.vertical_proximity.vertical_proximity import vertical_proximity
from modifier_set1.lateral_proximity.lateral_proximity import lateral_proximity
from modifier_set1.stacking_pattern.stacking_pattern import stacking_pattern


def modifier_set1(data):
    biostratigraphy(data)
    vertical_proximity(data)
    lateral_proximity(data)
    stacking_pattern(data)
