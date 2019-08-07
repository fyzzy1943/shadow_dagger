import os, time
import helper.sqlite as db
from urllib import request

from helper.getConfig import config

section = 'default'


def build():
    url = config(section, 'url')

    # print(url)
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36')
    with request.urlopen(req) as f:
        data = f.read()
        print('Request Status:', f.status, f.reason)
        # exit
        if f.status != 200:
            print('wrong code:', f.status)

        with open('torrent.xml', 'w', encoding='utf-8') as file:
            file.write(data.decode('utf-8'))


def download(url, title):
    t_name = config(section, 'name') + '_' + str(db.getID(title)) + '.torrent'
    fullname = os.path.join(config(section, 'dir'), t_name)

    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36')

    with request.urlopen(req) as f:
        data = f.read()
        print('Download Status:', f.status, f.reason)
        if f.status != 200:
            print('wrong code:', f.status)

        with open(fullname, 'wb') as file:
            file.write(data)

    # request.urlretrieve(url, fullname)


def execute():
    import xml.etree.ElementTree
    xml = xml.etree.ElementTree.parse('torrent.xml')
    for movie in xml.getiterator('item'):
        title = movie.find('title').text
        link = movie.find('link').text
        enclosure = movie.find('enclosure').attrib['url']

        if db.has(title):
            continue
        else:
            print('a new %s torrent: %s' % (section, title))
            with open('torrent.log', 'a') as file:
                file.write('a new %s torrent: %s @ %s\n' % (
                section, title, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            db.insert(title, link, section, enclosure)
            download(enclosure, title)
