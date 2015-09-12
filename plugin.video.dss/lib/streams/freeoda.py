from ..utils import bitly, xbmcutil
from . import veetle
import re

sourceSite = 'http://sports.freeoda.com'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')


    xbmcutil.updateProgressBar(pBar, 9, 'sports.freeoda.com - Stream 1')
    addStream('index', 'sports.freeoda.com - Stream 1')
    
    xbmcutil.updateProgressBar(pBar, 18, 'sports.freeoda.com - Stream 2')
    addStream('stream2', 'sports.freeoda.com - Stream 2')

    xbmcutil.updateProgressBar(pBar, 27, 'sports.freeoda.com - Stream 3')
    addStream('stream3', 'sports.freeoda.com - Stream 3')

    xbmcutil.updateProgressBar(pBar, 36, 'sports.freeoda.com - Stream 4')
    addStream('stream4', 'sports.freeoda.com - Stream 4')

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
    page1 = sourceSite + '/' + page +'.html'
    print page1
    pagecontent = bitly.getPage(page1, sourceSite, bitly.getUserAgent())
    #print pagecontent
    try :
        match = re.compile("file: \(\'(.+?)\'").findall(pagecontent)
        print match
        for name in match:
            streamUrl = name
            print streamUrl
            return streamUrl
        else :
            match = re.compile("file: window.atob \(\'(.+?)\'").findall(pagecontent)
            print match
            for name in match:
                print 'b64coded = '+ name
                streamUrl = bitly.getStreamUrl(name)
                print streamUrl
            return streamUrl
    except :
    #iframesrc = regIframe.search(pagecontent).group(1)
    #print 'iframesrc2 = '+ iframesrc
    #streamUrl = 'http:'+ iframesrc
        return page


def resolveIframe(page) :
    pagecontent = bitly.getPage(page)
    match=re.compile('src="(.+?)" id="myfr"').findall(pagecontent)
    for name in match:
        name = name
        return name
    return page
