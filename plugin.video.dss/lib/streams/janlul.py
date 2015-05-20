from ..utils import bitly, xbmcutil
from . import veetle
import re

sourceSite = 'http://www.janlul.com/'

def addStreams() :
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van Streams...')


    xbmcutil.updateProgressBar(pBar, 15, 'JanLul.com - stream 1')
    addStream('stream1', 'JanLul.com - Stream 1')

    xbmcutil.updateProgressBar(pBar, 30, 'JanLul.com - stream 2')
    addStream('stream2', 'JanLul.com - Stream 2')

    xbmcutil.updateProgressBar(pBar, 45, 'JanLul.com - stream 3')
    addStream('stream3', 'JanLul.com - Stream 3')

    xbmcutil.updateProgressBar(pBar, 60, 'JanLul.com - stream 4')
    addStream('stream4', 'JanLul.com - Stream 4')

    xbmcutil.updateProgressBar(pBar, 75, 'JanLul.com - stream 5')
    addStream('stream5', 'JanLul.com - Stream 5')

    xbmcutil.updateProgressBar(pBar, 90, 'JanLul.com - stream 6')
    addStream('stream6', 'JanLul.com - Stream 6')

    xbmcutil.updateProgressBar(pBar, 90, 'JanLul.com - stream 8')
    addStream('stream8', 'JanLul.com - Stream 8')


    xbmcutil.endOfList()


def addStream(stream, display) :
    streamUrl = findStream(stream) 
    if streamUrl[-4:] == '.flv' :
        print('Veetle')
        veetle.addChannel(display, streamUrl, 'janlul')
    else :
        print('M3U')
        if (xbmcutil.getResponse(streamUrl)) :
            color = 'green'
        else :
            streamUrl = ''
            color = 'red'
        xbmcutil.addMenuItem('[COLOR '+color+']'+display+'[/COLOR]', streamUrl, 'true', 'janlul','janlul')


def findStream(page) :
    page1 = resolveIframe(sourceSite + page +'.php')
    print page1
    page2 = resolveIframe2(page1)
    print page1
    page2content = bitly.getPage(page2, sourceSite, bitly.getUserAgent())
    b64coded = bitly.getBaseEncodedString(page2content)
    streamUrl = bitly.getStreamUrl(b64coded)
    return streamUrl
    
def resolveIframe(page) :
    try :
        if(page[:4] != 'http') :
            page = sourceSite + '/' + page
        pagecontent = bitly.getPage(page, sourceSite, bitly.getUserAgent())
        regIframe = re.compile('embed\ src\=\"(.*?)\"\ name\=\"iframe_name\"', re.DOTALL)
        iframesrc = regIframe.search(pagecontent).group(1)
        return iframesrc
    except :
        return page

def resolveIframe2(pagex) :
    try :
        if(pagex[:4] != 'http') :
            pagex = sourceSite + '/' + pagex
        pagecontent = bitly.getPage(pagex, sourceSite, bitly.getUserAgent())
        regIframe = re.compile('iframe\ src\=\"(.*?)\"\ name\=\"iframe_name\"', re.DOTALL)
        iframesrc = regIframe.search(pagecontent).group(1)
        return iframesrc
    except :
        return pagex


    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()
