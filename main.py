#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import helper.sqlite as db
import helper.xml as x

db.init()

x.section = 'hdsky'
x.build()
x.execute()

x.section = 'cmct'
x.build()
x.execute()

print('done.')
