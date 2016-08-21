#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os
import helper.sqlite as db
import helper.xml as x

db.init()

x.section = 'hdsky'
x.build()
x.execute()

x.section = 'cmct'
x.build()
x.execute()

with open('mission.log', 'a') as file:
	file.write('mission complete. @ %s\n'% time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
