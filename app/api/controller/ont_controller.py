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

class OntAuotFind(Resource):
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

		if self.tn:
			# check Current Config OLT
			self.data_cmd = []
			self.data_cmd.append("enable")
			self.data_cmd.append("display ont autofind all")
			self.runCommand()

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
			time.sleep(1)

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

	def runCommand(self):
		self.response = []
		prmNo = 0
		prmHostCode = ""
		prmSn = ""
		prmVersion = ""
		prmSoftwareVersion = ""
		prmEquipmentId = ""
		prmFrameId = ""
		prmSlotId = ""
		prmPortId = ""

		for i in range(0,len(self.data_cmd)):
			self.tn.write(telnetlib.IAC + telnetlib.WILL + telnetlib.ECHO)
			self.tn.write(self.data_cmd[i].encode("ascii")+b'\n')
			time.sleep(1)
			while True:
				time.sleep(1)
				data = self.tn.read_very_eager().decode("utf-8").replace("'","").replace("\r","").split("\n")
				ont_list = ["Number:","OntSN:","OntVersion:","F/S/P:","OntEquipmentID:","OntSoftwareVersion:"]

				for x in range(0,len(data)):
					if data[x] != "":
						prmHostCode = self.code
						if ont_list[0] in data[x].replace("\x1b[37D","").replace("---- More ( Press Q to break ) ----","").replace(" ",""):
							prmNo = data[x].replace("\x1b[37D","").replace("---- More ( Press Q to break ) ----","").replace(" ","").replace(ont_list[0],"")
						if ont_list[1] in data[x].replace("\x1b[37D","").replace("---- More ( Press Q to break ) ----","").replace(" ",""):
							prmSn = data[x].replace("\x1b[37D","").replace("---- More ( Press Q to break ) ----","").replace(" ","").replace(ont_list[1],"")
						if ont_list[2] in data[x].replace("\x1b[37D","").replace("---- More ( Press Q to break ) ----","").replace(" ",""):
							prmVersion = data[x].replace("\x1b[37D","").replace("---- More ( Press Q to break ) ----","").replace(" ","").replace(ont_list[2],"")
						if ont_list[3] in data[x].replace("\x1b[37D","").replace("---- More ( Press Q to break ) ----","").replace(" ",""):
							data_fps = data[x].replace("\x1b[37D","").replace("---- More ( Press Q to break ) ----","").replace(" ","").replace(ont_list[4],"")
							data_arr = data_fps.split(":")[1].split("/")
							print(data_arr)
							prmFrameId = data_arr[0]
							prmSlotId = data_arr[1]
							prmPortId = data_arr[2]
						if ont_list[4] in data[x].replace("\x1b[37D","").replace("---- More ( Press Q to break ) ----","").replace(" ",""):
							prmEquipmentId = data[x].replace("\x1b[37D","").replace("---- More ( Press Q to break ) ----","").replace(" ","").replace(ont_list[4],"")
						if ont_list[5] in data[x].replace("\x1b[37D","").replace("---- More ( Press Q to break ) ----","").replace(" ",""):
							prmSoftwareVersion = data[x].replace("\x1b[37D","").replace("---- More ( Press Q to break ) ----","").replace(" ","").replace(ont_list[5],"")

						if prmHostCode !="" and prmSn !="" and prmVersion !="" and prmSoftwareVersion !="" and prmEquipmentId !="" and prmFrameId !="" and prmSlotId !="" and prmPortId !="":
							source = Ont(
								Code = str(prmHostCode)+"-"+str(prmSn),
								HostCode = prmHostCode,
								Sn = prmSn,
								Version = prmVersion,
								SoftwareVersion = prmSoftwareVersion,
								EquipmentId = prmEquipmentId,
								FrameId = prmFrameId,
								SlotId = prmSlotId,
								PortId = prmPortId,
								ActiveStatus = 1
							)
							source.delete()
							source.save()

							self.response.append([
								prmHostCode,
								prmSn,
								prmVersion,
								prmSoftwareVersion,
								prmEquipmentId,
								prmFrameId,
								prmSlotId,
								prmPortId
							])
							prmNo = 0
							prmHostCode = ""
							prmSn = ""
							prmVersion = ""
							prmSoftwareVersion = ""
							prmEquipmentId = ""
							prmFrameId = ""
							prmSlotId = ""
							prmPortId = ""

					x=x+1

				if "#" in data[len(data)-1]:
					break
				elif "More" in data[len(data)-1]:
					self.tn.write(KEYS['EN'].encode("ascii")+b"\n")
					time.sleep(.2)
				else :
					self.tn.write(KEYS['EN'].encode("ascii")+b"\n")
					time.sleep(.2)
			i=i+1
			# print(Ont().list())
