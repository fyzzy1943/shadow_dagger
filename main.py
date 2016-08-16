#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from helper.getConfig import config
url = config('main', 'url')
print(url)

from urllib import request

# with request.urlopen(url) as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print(k, v)
#     xml = data.decode('utf-8')

# import xml.etree.ElementTree
# xml = xml.etree.ElementTree.parse('a.xml')
# movies = xml.getiterator('item')
# print(len(movies))
# for movie in movies:
#     pass
    # print(movie.find('title').text)
    # print('link: '+movie.find('link').text)
    # print('author: '+movie.find('author').text)
    # print('category: '+movie.find('category').text)
    # print(movie.find('enclosure').attrib['url'])
    # print(movie.find('pubDate').text)

# from helper.sqlite import test
# test()
import helper.sqlite as db
db.init()
