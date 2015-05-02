from ..utils import bitly, xbmcutil
from . import veetle
import re

sourceSite='http://polepositionv2.nl'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')


    xbmcutil.updateProgressBar(pBar, 33, 'poleposition - Stream 1')
    addStream('BDDS1A', 'poleposition - Stream 1')
    
    xbmcutil.updateProgressBar(pBar, 66, 'poleposition - Stream 2')
    addStream('BDDS2A', 'poleposition - Stream 2')

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()





def addStream(stream, display) :
    streamUrl = findStream(stream) 
    if streamUrl[-4:] == '.flv' :
        print('Veetle')
        veetle.addChannel(display, streamUrl, 'BVLS')
    else :
        print('M3U')
        if (xbmcutil.getResponse(streamUrl)) :
            color = 'green'
        else :
            streamUrl = ''
            color = 'red'
        xbmcutil.addMenuItem('[COLOR '+color+']'+display+'[/COLOR]', streamUrl, 'true', 'BVLS','BVLS')


def findStream(page) :
    page1 = (sourceSite + '/' + page +'.php')
    print page1
    frameHtml = bitly.getPage(page1, sourceSite, bitly.getUserAgent())
    b64coded = bitly.getBaseEncodedString(frameHtml)
    print b64coded
    streamUrl = bitly.getStreamUrl(b64coded)
    print streamUrl
    return streamUrl
    

