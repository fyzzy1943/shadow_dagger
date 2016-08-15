#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
config = configparser.ConfigParser()
config.read('.env')
passkey = config['main']['passkey']
print(passkey)
