"""
Routing urls for the Api app
"""

# third-party imports
from flask import Blueprint
from flask_restful import Api

# local imports
# from .resources import ApiResource
from ..api.controller.monitor_controller import OltSnmp
from ..api.controller.host_controller import CheckHost
from ..api.controller.ont_controller import OntAuotFind

# pylint: disable=invalid-name
api_host = Blueprint('api', __name__)
api = Api(api_host)

api.add_resource(CheckHost, '/checkhost', methods=['GET'], endpoint='checkhost')
api.add_resource(OntAuotFind, '/autofind', methods=['GET'], endpoint='config')
api.add_resource(OltSnmp, '/monitor-olt', methods=['GET'], endpoint='oltsnmp')
