from ..utils import xbmcutil, bitly
import urllib2, re

import xml.etree.ElementTree as ET

def add13Stream():
    addSopStream('13th Stream 1', '106491', '13stream')
    addSopStream('13th Stream 2', '106492', '13stream')
	
def addStreams():
    #TEST
    #addAceStream('TEST','')
    #foxsports = bitly.resolveTorrentTv('http://torrent-tv.ru/torrent-online.php?translation=9218')
    #try:
    #    addAceStream('Fox Sports 2 NL ',foxsports)
    #except:
    #    xbmcutil.logMessage('Fox Sports 2 NL is offline')
    #addSopStream('Rusia Sport', '116041')
    addSopStream('DSC+1', '150004')
    addAceStream('Dazsports','4016bc0b052c0e113ab51d635c66ca1669da0440')
    addAceStream('Dazsports 2','d293c82146aa6c2904e45ff305ae0f38dc5b329d')
    addAceStream('Dazsports 3','6b5c073b86fb29ffc73f47231f30068d223a4d3d')
    addAceStream('YES','8f9ea6a3e2c20cf2c8173b3e9d0795de70a26893')
    addAceStream('Stream Of The Day','27feca99304539891f6a8362a0f14fc0cdb8c24d')

def addSopStream(name, SopId='106491', internal=None):
    if(checkSopStream(SopId)):
        info = getSopInfo(SopId)
        displayName = '[COLOR green]'+name+' ['+info+'][/COLOR]'
        p2pUrl = 'plugin://plugin.video.p2p-streams/?url='+SopId+'&mode=2&name='+name.replace(' ', '+')
    else :
        displayName = '[COLOR red]'+name+'[/COLOR]'
        p2pUrl = 'plugin://plugin.video.dss/none'
    xbmcutil.addMenuItem(displayName, p2pUrl, 'true', internal, internal)
	
def addAceStream(name, aceId, internal=None):
    aceUrl = 'plugin://plugin.video.p2p-streams/?url='+aceId+'&mode=1&name='+name.replace(' ', '+')
    xbmcutil.addMenuItem(name, aceUrl, 'true', internal, internal)

def getSopInfo(sopId):
    req = urllib2.Request('http://www.sopcast.com/chlist.xml')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0')
    response = urllib2.urlopen(req)
    content=response.read()
    tree = ET.fromstring(content)
    for channel in tree.findall(".//channel/[@id='"+sopId+"']") :
        users = channel.find("user_count").text
        bitrate = channel.find("kbps").text
        streamtype = channel.find("stream_type").text    
    return streamtype+' - '+ bitrate + 'kbps ('+users+' users)'

def getSopStream(id):
    content = getUrl("http://www.sopcast.com/chlist.xml")
    tEntries = re.compile('<item>sop://(.+?):3912/'+str(id)+'</item>').findall(content)
    return tEntries[0]
  
def getUrl(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

def checkSopStream(id):    
    print 'do check: ' 
    try:
        getSopStream(id)
        return True
    except:
        return False
