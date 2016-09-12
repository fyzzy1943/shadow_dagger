#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os
import helper.sqlite as db
import helper.xml as x
from helper.getConfig import allSection

db.init()

for section in allSection():
	x.section = section
	x.build()
	x.execute()

with open('mission.log', 'a') as file:
	file.write('mission complete. @ %s\n'% time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
