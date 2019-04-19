from modifier_set2.upper_boundary.upper_boundary import upper_boundary
from modifier_set2.lower_boundary.lower_boundary import lower_boundary
from modifier_set2.associated_facies.associated_facies import associated_facies


def modifier_set2(data):
    for i in range(0, 2):
        associated_facies(data, i + 1)
        lower_boundary(data, i + 1)
        upper_boundary(data, i + 1)
