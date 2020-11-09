"""
Views for the Api app
"""

# third-party imports
from ...helper.utils import response_json, make_request
from ...helper import constants
from flask_restful import Resource, reqparse

from easysnmp import Session
from pprint import pprint

import array as arr
import re, socket, logging, types, six, getpass, sys, telnetlib, getopt, ipaddress, os, time, datetime


KEYS = {
	'UP': '\033[B',
	'DW': '\033[C',
	'EN': '\r'
}

parser = reqparse.RequestParser()  # pylint: disable=invalid-name
parser.add_argument('code', type=str)

class OltSnmp(Resource):
	tn        		= None
	hostname        = "172.16.222.81"
	port            = 23
	oid         	= False
	status			= True
	message			= None
	response		= None
	data_cmd		= None

	def get(self):
		try:
			session = Session(hostname=self.hostname, community='public', version=2, timeout=1, retries=3)
			# oid = {'value': oid}
			# result = {}
			# for k in oid:
			#     result[k] = session.get(oid[k]).value
			return response_json(True, "Connection Success", self.response)
			# return response_json(self.status, self.message, self.response)
		except (TimeoutError, NameError, ReferenceError):
			return response_json(True, "Connection Error", self.response)
