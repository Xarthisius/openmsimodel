from openmsimodel.entity.base import Process, Material
from gemd import (
    ProcessTemplate,
    MaterialTemplate,
    PropertyTemplate,
    ParameterTemplate,
    CategoricalBounds,
)

from openmsimodel.entity.base.attributes import _validate_temp_keys, define_attribute


# missing template
class erroneousSubclass5(Material):
    _ATTRS = _validate_temp_keys(TEMPLATE)

    define_attribute(
        _ATTRS,
        template=ParameterTemplate(
            name="Pressure",
            bounds=CategoricalBounds(["0.1-0.2", "0.2-0.3"]),
        ),
    )

    finalize_template(_ATTRS, TEMPLATE)