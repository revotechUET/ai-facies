from .biostratigraphy.biostratigraphy import biostratigraphy
from .vertical_proximity.vertical_proximity import vertical_proximity
from .lateral_proximity.lateral_proximity import lateral_proximity
from .stacking_pattern.stacking_pattern import stacking_pattern


def modifier_set1(data):
    biostratigraphy(data)
    vertical_proximity(data)
    lateral_proximity(data)
    stacking_pattern(data)
