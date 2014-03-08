#!/usr/bin/python2

'''
@author Allen Choong Chieng Hoon
@date	2014-03-02


This is the script contains the functions related to scanmem. The functions now included
are changing the address offset.
'''

import json

def readCheatlist(filename):
	content = None
	with open(filename,'r') as f:
		content = f.read()
	
	data = json.JSONDecoder().decode(content)
	return data
	
def offsetAdd(data,num):
	'''Change add the offset of the address'''
	for x in data['cheat_list']:
		x[3] = hex(int(x[3],16) + num)[2:]
	return data
	
def offsetAdjustTo(data,num1,num2):
	'''Adjust the offset from num1 to num2'''
	offsetAdd(data,num2-num1)
	return data
	
def writeCheatlist(data,filename):
	obj = json.JSONEncoder().encode(data)
	with open(filename,'w') as f:
		f.write(obj)
