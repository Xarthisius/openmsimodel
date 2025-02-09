from openmsimodel.entity.base import Process, Material
from gemd import (
    ProcessTemplate,
    MaterialTemplate,
    PropertyTemplate,
    ParameterTemplate,
    CategoricalBounds,
)

from openmsimodel.entity.base.attributes import (
    _validate_temp_keys,
    define_attribute,
    finalize_template,
)


# missing _ATTRS b)
class erroneousSubclass7(Material):
    TEMPLATE = MaterialTemplate(
        name="erroneousSubclass7",
    )

    finalize_template(_ATTRS, TEMPLATE)
