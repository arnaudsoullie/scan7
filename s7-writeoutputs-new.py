#!/usr/bin/env python
# -*- coding: utf-8 -*-

import snap7
import sys

SIEMENS_S71200 = sys.argv[1]
LIGHTS = sys.argv[2]

s7 = snap7.client.Client()
s7.connect(SIEMENS_S71200, 0, 1)
LIGHTS = LIGHTS[::-1]
data1 = bytearray([int(LIGHTS, 2)])
r = s7.write_area(snap7.types.areas['PA'], 0, 0, data1)
print r
s7.disconnect()