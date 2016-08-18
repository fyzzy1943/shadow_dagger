import urllib.request, os, time
import helper.sqlite as db

from helper.getConfig import config

section = 'default'

def build():
    url = config(section, 'url')

    with urllib.request.urlopen(url) as f:
        data = f.read()
        # print('Status:', f.status, f.reason)
        if f.status!=200:
            print('wrong code:', f.status)

        with open('torrent.xml', 'w', encoding='utf-8') as file:
            file.write(data.decode('utf-8'))

def download(url, title):
    t_name = config(section, 'name')+'_'+str(db.getID(title))+'.torrent'
    fullname = os.path.join(config(section, 'dir'), t_name)
    urllib.request.urlretrieve(url, fullname)

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
            print('a new %s torrent: %s'% (section, title))
            with open('torrent.log', 'a') as file:
                file.write('a new %s torrent: %s @ %s'% (section, title, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            db.insert(title, link, section, enclosure)
            download(enclosure, title)
