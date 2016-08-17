#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import helper.sqlite as db
import helper.url as url

db.init()
xml = url.getXML()
file = open('torrent.xml', 'w', encoding='utf-8')
file.write(xml)
file.close()

import xml.etree.ElementTree
xml = xml.etree.ElementTree.parse('torrent.xml')
movies = xml.getiterator('item')
for movie in movies:
    title = movie.find('title').text
    link = movie.find('link').text
    author = movie.find('author').text
    category = movie.find('category').text
    enclosure = movie.find('enclosure').attrib['url']
    date = movie.find('pubDate').text

    if db.has(title):
        continue
    else:
        db.insert(title, link, author, category, enclosure, date)
        url.download(enclosure, title)

print('done.')
