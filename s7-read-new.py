#!/usr/bin/env python
# -*- coding: utf-8 -*-

import snap7
import sys

SIEMENS_S71200 = sys.argv[1]	

s7 = snap7.client.Client()
s7.connect(SIEMENS_S71200, 0, 1)
r = s7.read_area(snap7.types.areas['PE'], 0, 0, 1)
rr = bin(r[0])
rrr = rr[2:]
while len(rrr) < 8:
  rrr = '0' + rrr

Input0 = rrr[7]
Input1 = rrr[6]
Input2 = rrr[5]
Input3 = rrr[4]
Input4 = rrr[3]
Input5 = rrr[2]
Input6 = rrr[1]
Input7 = rrr[0]

s = s7.read_area(snap7.types.areas['PA'], 0, 0, 1)
ss = bin(s[0])
sss = ss[2:]
while len(sss) < 6:
  sss = '0' + sss


Output5 = sss[0]
Output4 = sss[1]
Output3 = sss[2]
Output2 = sss[3]
Output1 = sss[4]
Output0 = sss[5]

print '=== Inputs ==='
print "Input 0 : " + Input0
print "Input 1 : " + Input1
print "Input 2 : " + Input2
print "Input 3 : " + Input3
print "Input 4 : " + Input4 
print "Input 5 : " + Input5
print "Input 6 : " + Input6 
print "Input 7 : " + Input7

print '===Outputs==='
print "Output 0 : " + Output0
print "Output 1 : " + Output1
print "Output 2 : " + Output2
print "Output 3 : " + Output3
print "Output 4 : " + Output4 
print "Output 5 : " + Output5

s7.disconnect()