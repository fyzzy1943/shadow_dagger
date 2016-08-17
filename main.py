#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os
import helper.sqlite as db
import helper.xml as x

db.init()

while True:
    print('mission start. as %s'% time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    x.section = 'hdsky'
    x.build()
    x.execute()

    x.section = 'cmct'
    x.build()
    x.execute()

    print('mission complete. sleep 5min.')
    time.sleep(60*5)
os.system('pause')
