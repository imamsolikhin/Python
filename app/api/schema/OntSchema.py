"""
Schemas for the Api app
"""

# local imports
from ...config.db import marshmallow

class OntSchema(marshmallow.Schema):
    """
    This class represents the ont schema.
    """
    class Meta:
        fields = (
            'Code', 'HostCode', 'Sn', 'Version',
            'SoftwareVersion', 'EquipmentId',
            'FrameId', 'SlotId', 'PortId',
            'Remark', 'ActiveStatus',
            'CreatedBy', 'CreatedDate',
            'UpdatedBy', 'UpdatedDate',
            'InActiveBy', 'InActiveDate'
        )

# pylint: disable=invalid-name
ont_schema = OntSchema()
onts_schema = OntSchema(many=True)
