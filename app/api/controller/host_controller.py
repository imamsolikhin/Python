"""
Views for the Api app
"""

# third-party imports
from ...helper.utils import response_json, make_request
from ...helper import constants
from ..models.Ont import Ont
from ..schema.OntSchema import ont_schema, onts_schema
from flask_restful import Resource, reqparse

from pprint import pprint
from collections import Counter

import array as arr
import re, socket, logging, types, six, getpass, sys, telnetlib, getopt, ipaddress, os, time, datetime


KEYS = {
	'UP': '\033[B',
	'DW': '\033[C',
	'EN': '\r'
}

parser = reqparse.RequestParser()  # pylint: disable=invalid-name
parser.add_argument('code', type=str)
parser.add_argument('host', type=str)
parser.add_argument('usr', type=str)
parser.add_argument('psw', type=str)

class CheckHost(Resource):
	tn        		= None
	hostname        = None
	usr				= "rudytch"
	psw				= "Sementara2354"
	port            = 23
	hasecho         = False
	status			= True
	message			= None
	response		= None
	data_cmd		= None

	def get(self):
		args = parser.parse_args()
		self.code = args['code']
		self.hostname = args['host']
		self.usr = args['usr']
		self.psw = args['psw']

		self.connect()
		self.disconnect()

		return response_json(self.status, self.message, self.response)

	def connect(self):
		try:
			self.tn = telnetlib.Telnet(self.hostname,self.port,10)
		except socket.error:
			self.status = False
			self.message = "Problem connecting to host ('telnet %s %d')" % (self.hostname, self.port)

		if self.status:
			self.tn.read_until(b"name:")
			self.tn.write(self.usr.encode("ascii")+b"\n")
			self.tn.read_until(b"password:")
			self.tn.write(self.psw.encode("ascii")+b"\n")
			time.sleep(.3)
			self.tn.write(b"y\n")
			self.tn.write(b"\n")
			time.sleep(.3)

			self.response = self.tn.read_very_eager().decode("utf-8")

			if "invalid" in self.response:
				self.status = False
				self.message = "Username or password is invalid"
			else:
				self.status = True
				self.message = "Username or password is valid"

	def disconnect(self):
		if self.tn:
			self.tn.close()
			self.tn = None
