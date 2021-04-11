## Teste 02 - Utilizando somente o setting##
## 
##

#Cabecalho do algoritmo
import pycurl
import numpy as np
import urllib3
import json
import time
import sys

try:
	from io import BytesIO
except ImportError:
	from StringIO import StringIO as BytesIO
try:
	from urllib.parse import urlencode
except ImportError:
	from urllib import urlencode


configDefault = {
				'setting':		{   'rpm' : '300',
								  'laser' : 'on',
								 'return' : 'Strongest'},
		 		'setting/fov':	{ 'start' : '0',
		 			  			    'end' : '359'},
	  	 		'setting/host': {  'addr' : '255.255.255.255',
								  'dport' : '2368',
		 			  			   'tpor' : '8309'},
	  			'setting/net':  {  'addr' : '192.168.1.201',
								   'mask' : '255.255.255.0',
							    'gateway' : '192.168.1.2',
								   'dhcp' : 'off'}
								}

for k,i in configDefault.items():
	for j in i.keys():
		ans = input("Insira " + k + ":" + j + " (default: " + configDefault[k][j] + "[ENTER]): ")
		if not ans == '':
			print(ans)
			configDefault[k][j] = ans






# print(configDefault)




# Funcao de entrada de dados do sensor
# s = ...
# url = ...
# pf = ...
# buf = ...
# def sensor_do(s, url, pf, buf):
# 	s.setopt(s.URL, url)
# 	s.setopt(s.POSTFIELDS, pf)
# 	s.setopt(s.WRITEDATA, buf)
# 	s.perform()

# 	rcode = s.getinfo(s.RESPONSE_CODE)
# 	success = rcode in range(200, 207)
# 	print ('%s %s: %d (%s)' % (url, pf, rcode, 'OK' if success else 'ERROR'))
# 	return success

# URL do sensor
# Base_URL = 'http://192.168.1.200/cgi/'

# ???
# sensor = pycurl.Curl()
# buffer = BytesIO()

# Setando as configuracoes do sensor
# rc = sensor_do(sensor, Base_URL+'reset', urlencode({'data':'reset_system'}), buffer)
# if rc:
# 	time.sleep(10)
# 	for k,v in configDefault.items():
# 		for j in v.items():
# 			rc = sensor_do(sensor, Base_URL + k, urlencode(dict([j])), buffer)
# 			if not rc:
# 				break
# 			time.sleep(1)
# if rc:
# 	rc = sensor_do(sensor, Base_URL+'save', urlencode({'data':'submit'}), buffer)
# if rc:
# 	time.sleep(10)


import xmltodict

ros_launch = open('ros.launch','r')

entrada = xmltodict.parse(ros_launch.read())


for item in entrada['launch']['arg']:
	for v in configDefault.values():
		for j,i in v.items():
			if item['@name'] == j:
				item['@default'] = i
        
# for item in [entrada['launch']['arg'],]:
# 	if item['@name'] == 'rpm':
# 		item['@default'] = '300'

entrada = xmltodict.unparse(entrada)
print(entrada)



# response = urllib3.urlopen(Base_URL + 'status.json')
# if response:
# 	status = json.loads(response.read())
# 	print (status)
	# ('Motor: %s \nAtividade do Sensor: %s \nTipo de retorno: %s \n'\
	# 'Inicio FOV: %s \nTermino FOV: %s \n' % (status['motor']['rpm'], status['laser']['state'],
	# status['return']['...'], status['start']['...'], status['end']['...']))


# sensor.close()


# Ta melhorando :)