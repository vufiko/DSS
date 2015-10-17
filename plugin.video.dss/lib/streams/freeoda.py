from ..utils import bitly, xbmcutil
from . import veetle
import re

sourceSite = 'http://belgiumanddutch.gq'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')


    xbmcutil.updateProgressBar(pBar, 9, 'belgiumanddutch - Stream 1')
    addStream('skysports1', 'belgiumanddutch - Stream 1')
    
    xbmcutil.updateProgressBar(pBar, 18, 'belgiumanddutch - Stream 2')
    addStream('skysports2', 'belgiumanddutch - Stream 2')

    xbmcutil.updateProgressBar(pBar, 27, 'belgiumanddutch - Stream 3')
    addStream('skysports3', 'belgiumanddutch - Stream 3')

    xbmcutil.updateProgressBar(pBar, 36, 'belgiumanddutch - Stream 4')
    addStream('skysports4', 'belgiumanddutch - Stream 4')

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()

def addStream(stream, display) :
    streamUrl = findStream(stream) 
    if streamUrl[-4:] == '.flv' :
        print('Veetle')
        veetle.addChannel(display, streamUrl, 'freeoda')
    else :
        print('M3U')
        if (xbmcutil.getResponse(streamUrl)) :
            color = 'green'
        else :
            streamUrl = ''
            color = 'red'
        xbmcutil.addMenuItem('[COLOR '+color+']'+display+'[/COLOR]', streamUrl, 'true', 'freeoda','freeoda')

def findStream(page) :
    page1 = sourceSite + '/skysports/' + page +'.php'
    print page1
    pagecontent = bitly.getPage(page1, sourceSite, bitly.getUserAgent())
    #print pagecontent
    try :
        frameHtml = bitly.getPage(page1, sourceSite, bitly.getUserAgent())
        b64coded = bitly.getBaseEncodedString(frameHtml)
        print b64coded
        streamUrl = bitly.getStreamUrl(b64coded)
        print streamUrl
        return streamUrl
    except :
        return page


def resolveIframe(page) :
    pagecontent = bitly.getPage(page)
    match=re.compile('src="(.+?)" id="myfr"').findall(pagecontent)
    for name in match:
        name = name
        return name
    return page
