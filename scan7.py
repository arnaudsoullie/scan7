#!/usr/bin/env python
# -*- coding: utf-8 -*-

import snap7

# OptionParser imports
from optparse import OptionParser

import logging
logging.basicConfig()

# Script version
VERSION = '0.1a'

# Options definition (I stole this options parsing thing from Thomas Debize but he's OK with it
option_0 = { 'name' : ('-t', '--target'), 'help' : 'IP address of the PLC', 'nargs' : 1 }
option_1 = { 'name' : ('-s', '--scan'), 'help' : 'Scan the PLC for information', 'nargs' : 0 }
option_2 = { 'name' : ('-r', '--read'), 'help' : 'Read some data from the PLC {inputs | outputs}', 'nargs' : 1 }
option_3 = { 'name' : ('-w', '--write'), 'help' : 'Write data to the PLC', 'nargs' : 2 }

options = [option_1, option_2, option_3, option_0]

class Siemens(object):

	def __init__(self, host):
		self.client = snap7.client.Client()
		self.client.connect(host, 0, 1)

	def read_all_inputs(self):
		i = 1
		inputs = list()
		while True:
			try:
				r = self.client.read_area(snap7.types.areas['PE'], 0, i, 1)
				i = i + 1
				inputs.append(r[0])
				print 'Value at #' + str(i) + str(r[0])
			except ZeroDivisionError:
				print 'YOLO'
			except:
				print 'Unexpected error when reading input #' + str(i)
		return inputs

	def read_input(self, i):
		r = self.client.read_area(snap7.types.areas['PE'], 0, i, 1)
		return r[0] == 1

	def read_output(self, i):
		r = self.client.read_area(snap7.types.areas['PA'], 0, i, 1)
		return r[0] == 1

	def write_output(self, area, data):
		data = bytearray([0x01])		
		r = self.client.write_area(snap7.types.areas['PA'], 0, 0, data)
		return r

	def close(self):
		self.client.disconnect()

def main(options, arguments):
	global VERSION

	print 'scan7.py version %s\n' % VERSION

	# Parse options
	if (options.target == None):
		parser.error('Please specify a target')

	if (options.read == None and options.write == None and options.scan == None):
		parser.error('Please specify an action : read, write or scan')

	if ((options.read and options.write) or (options.read and options.scan) or (options.write and options.scan)):
		parser.error('Please choose one action only ! Make up your mind !')

	# Actually do something usefull here
	s7 = Siemens(options.target)
	datas = snap7.types.areas
	for i in datas:
		print str(i) + ' :: ' + str(datas[i])
	for i in range(0,100):
		print str(i) + '::' + str(s7.client.read_area(snap7.types.areas['PA'], 0, i, 1))
		

	if (options.read):
		if (options.read == 'inputs'):
			inputs = s7.read_all_inputs()
			for i in range(0, len(inputs)):
				print 'Input #' + str(i) + ' : ' + str(inputs(i))
		elif (options.read == 'output'):
			outputs = s7.read_all_outputs()
			for i in range(0, len(outputs)):
				print 'Output #' + str(i) + ' : ' + str(outputs(i))
		else:
			parser.error('Valid data to be read : "inputs" or "outputs"')

	s7.close()

	return None

if __name__ == "__main__" :
	parser = OptionParser()
	for option in options:
		param = option['name']
		del option['name']
		parser.add_option(*param, **option)

	options, arguments = parser.parse_args()
	main(options, arguments)