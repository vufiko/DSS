from ..utils import bitly, xbmcutil
from . import veetle
import re

sourceSite='http://dazsports.org'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    
    xbmcutil.updateProgressBar(pBar, 30, 'DazSports 3')
    addStream('streamplayer3', 'DazSports - Stream 3')

    
    xbmcutil.updateProgressBar(pBar, 49, 'DazSports 4')
    addStream('streamplayer4', 'DazSports - Stream 4')

    xbmcutil.updateProgressBar(pBar, 98, 'DazSports 5')
    addStream('streamplayer5', 'DazSports - Stream 5')

    
    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()



def addStream(stream, display) :
    streamUrl = findStream(stream) 
    if streamUrl[-4:] == '.flv' :
        print('Veetle')
        veetle.addChannel(display, streamUrl, 'DazSports')
    else :
        print('M3U')
        if (xbmcutil.getResponse(streamUrl)) :
            color = 'green'
        else :
            streamUrl = ''
            color = 'red'
        xbmcutil.addMenuItem('[COLOR '+color+']'+display+'[/COLOR]', streamUrl, 'true', 'DazSports','DazSports')


def findStream(page) :
    page1 = (sourceSite + '/' + page +'.php')
    if(page1[:4] != 'http') :
        page1 = sourceSite + '/' + page1
    frameHtml = bitly.getPage(page1, sourceSite, bitly.getUserAgent())
    b64coded = bitly.getBaseEncodedString(frameHtml)
    print b64coded
    streamUrl = bitly.getStreamUrl(b64coded)
    print streamUrl
    return streamUrl
    
def resolveIframe(page) :
    try :
        if(page[:4] != 'http') :
            page = sourceSite + '/' + page
        pagecontent = bitly.getPage(page, sourceSite, bitly.getUserAgent())
        match=re.compile('src="(.+?).php"' ).findall(page)[0]
        match = (match + '.php')
        iframesrc = match.search(pagecontent).group(1)
        return iframesrc
    except :
        return page
