import urllib.request, os
import helper.sqlite as db

from helper.getConfig import config

def getXML():
    url = config('hdsky', 'url')

    with urllib.request.urlopen(url) as f:
        data = f.read()
        # print('Status:', f.status, f.reason)
        if f.status!=200:
            print('wrong code:', f.status)

        return data.decode('utf-8')

def download(url, title):
    t_name = config('hdsky', 'name')+'_'+str(db.getID(title))+'.torrent'
    fullname = os.path.join(config('hdsky', 'dir'), t_name)
    urllib.request.urlretrieve(url, fullname)
