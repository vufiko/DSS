from ..utils import bitly, xbmcutil
from . import veetle
import re

sourceSite = 'http://www.janlul.com/'

def addStreams() :
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van Streams...')


    xbmcutil.updateProgressBar(pBar, 15, 'JanLul.com - stream 1')
    addStream('janlul1', 'JanLul.com - Stream 1')

    xbmcutil.updateProgressBar(pBar, 30, 'JanLul.com - stream 2')
    addStream('janlul2', 'JanLul.com - Stream 2')

    xbmcutil.updateProgressBar(pBar, 45, 'JanLul.com - stream 3')
    addStream('janlul3', 'JanLul.com - Stream 3')

    xbmcutil.updateProgressBar(pBar, 60, 'JanLul.com - stream 4')
    addStream('janlul4', 'JanLul.com - Stream 4')

    xbmcutil.updateProgressBar(pBar, 75, 'JanLul.com - stream 5')
    addStream('janlul5', 'JanLul.com - Stream 5')

    xbmcutil.updateProgressBar(pBar, 90, 'JanLul.com - stream 6')
    addStream('janlul6', 'JanLul.com - Stream 6')

    xbmcutil.updateProgressBar(pBar, 90, 'JanLul.com - stream 7')
    addStream('janlul7', 'JanLul.com - Stream 7')

    xbmcutil.updateProgressBar(pBar, 90, 'JanLul.com - stream 8')
    addStream('janlul8', 'JanLul.com - Stream 8')

    xbmcutil.updateProgressBar(pBar, 90, 'JanLul.com - stream 9')
    addStream('janlul9', 'JanLul.com - Stream 9')

    xbmcutil.updateProgressBar(pBar, 90, 'JanLul.com - stream 10')
    addStream('janlul10', 'JanLul.com - Stream 10')

    xbmcutil.endOfList()
    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')

    

def addStream(stream, display) :
    streamUrl = findStream(stream) 
    if streamUrl[-4:] == '.flv' :
        print('Veetle')
        veetle.addChannel(display, streamUrl, 'janlul')
    else :
        print('M3U')
        if (xbmcutil.getResponse(streamUrl)) :
            color = 'blue'
        else :
            streamUrl = ''
            color = 'red'
        xbmcutil.addMenuItem('[COLOR '+color+']'+display+'[/COLOR]', streamUrl, 'true', 'janlul','janlul')


def findStream(page) :
    page1 = bitly.getSourceUrl(page)
    page1content = bitly.getPage(page1, sourceSite, bitly.getUserAgent())
    streamUrl = page1content
    if streamUrl[-4:] == '.m3u' :
        streamUrl = streamUrl + '8'
    return streamUrl
