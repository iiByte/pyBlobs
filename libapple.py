from urllib.request import urlopen, Request
import json
from colorama import Fore
import os

class iDevice():
	def __init__(self, indentifier):
		self.indentifier = indentifier
		self.ipswURL = "https://api.ipsw.me/v4/device/{}?type=ipsw".format(indentifier)
		print("Requesting for {}...".format(indentifier))
		self.HTTPSReq = Request(self.ipswURL, headers={'Accept': 'application/json'})
		print("Got response.")
		self.JSONlist = json.loads(urlopen(self.HTTPSReq).read())
		self.firmwares = self.JSONlist["firmwares"]
		self.signed = {}

		for ver in self.firmwares:
			curFirmware = ver["version"]
			curSigned = ver["signed"]
			self.signed[curFirmware] = curSigned

	def __str__(self):
		columns = int(os.popen('stty size', 'r').read().split()[1])
		padding = [(columns//2)-6,(columns - columns//2)-5]

		line1 = "-"*padding[0]+"Device Info"+"-"*padding[1]
		line2 = "Name:{:>75}".format(self.JSONlist["name"])
		line3 = "Indentifier:{:>68}".format(self.JSONlist["identifier"])
		line4 = "Board Config:{:>67}".format(self.JSONlist["boardconfig"])
		line5 = "Platform:{:>71}".format(self.JSONlist["platform"])
		line6 = "-"*columns

		returnVal = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5 + "\n" + line6+ "\n" 
		
		return returnVal
