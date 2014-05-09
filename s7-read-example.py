#!/usr/bin/env python
# -*- coding: utf-8 -*-

import snap7
import pprint

SIEMENS_S71200 = 'XX.XX.XX.XX'

class Siemens(object):

	def __init__(self, host):
		self.client = snap7.client.Client()
		self.client.connect(SIEMENS_S71200, 0, 1)

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


s7 = Siemens(SIEMENS_S71200)

print 'Valeurs des inputs'
for i in range(0, 7):
	print 'Valeur input ' + str(i) + ' : ' + str(s7.read_input(i))

print '\r\nValeur des outputs'
for i in range(0, 7):
	print 'Valeur output ' + str(i) + ' : ' + str(s7.read_output(i))

s7.close()








