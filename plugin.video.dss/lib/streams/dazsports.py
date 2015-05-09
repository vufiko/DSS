from ..utils import bitly, xbmcutil
from . import veetle, sopcast
import urllib2, re

sourceSite='http://dazsports.org'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    
    xbmcutil.updateProgressBar(pBar, 30, 'DazSports 3')
    tmp = findStream('player3')
    veetle.addChannel('DazSports - Stream 3', tmp, 'daz')

    
    xbmcutil.updateProgressBar(pBar, 49, 'DazSports 4')
    tmp = findStream('player4')
    veetle.addChannel('DazSports - Stream 4', tmp, 'daz')

    xbmcutil.updateProgressBar(pBar, 98, 'DazSports 5')
    tmp = findStream('player5')
    veetle.addChannel('DazSports - Stream 5', tmp, 'daz')

    
    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()



def findStream(stream):
    page = bitly.getPage(sourceSite + '/' + stream + '.php', sourceSite, bitly.getUserAgent())
    match=re.compile('src="(.+?).php"' ).findall(page)[0]
    match = (match + '.php')
    frameHtml = bitly.getPage(sourceSite + '/'+ match, bitly.getUserAgent())
    base64 = bitly.getBaseEncodedString(frameHtml)
    return bitly.getStreamUrl(base64)
