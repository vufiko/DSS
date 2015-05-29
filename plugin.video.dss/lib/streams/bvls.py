from ..utils import bitly, xbmcutil
from . import veetle
import re

sourceSite='http://bvls2013.com'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')


    #xbmcutil.updateProgressBar(pBar, 9, 'BVLS - Stream 1')
    #addStream('stream1', 'BVLS - Stream 1')
    
    #xbmcutil.updateProgressBar(pBar, 18, 'BVLS - Stream 2')
    #addStream('stream2', 'BVLS - Stream 2')

    xbmcutil.updateProgressBar(pBar, 27, 'BVLS - Stream 3')
    addStream('stream3', 'BVLS - Stream 3')

    xbmcutil.updateProgressBar(pBar, 36, 'BVLS - Stream 4')
    addStream('stream4', 'BVLS - Stream 4')

    xbmcutil.updateProgressBar(pBar, 45, 'BVLS - Stream 5')
    addStream('stream5', 'BVLS - Stream 5')

    xbmcutil.updateProgressBar(pBar, 54, 'BVLS - Stream 6')
    addStream('stream6', 'BVLS - Stream 6')

    xbmcutil.updateProgressBar(pBar, 63, 'BVLS - Stream 7')
    addStream('stream7', 'BVLS - Stream 7')

    xbmcutil.updateProgressBar(pBar, 72, 'BVLS - Stream 8')
    addStream('stream8', 'BVLS - Stream 8')

    xbmcutil.updateProgressBar(pBar, 81, 'BVLS - Stream 9')
    addStream('stream9', 'BVLS - Stream 9')

    xbmcutil.updateProgressBar(pBar, 90, 'BVLS - Stream 10')
    addStream('stream10', 'BVLS - Stream 10')

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
    page1 = resolveIframe(sourceSite + '/' + page +'.html')
    if(page1[:4] != 'http') :
        page1 = sourceSite + '/' + page1
    frameHtml = bitly.getPage(page1, sourceSite, bitly.getUserAgent())
    b64coded = bitly.getBaseEncodedString(frameHtml)
    print b64coded
    streamUrl = bitly.getStreamUrl(b64coded)
    return streamUrl
    
def resolveIframe(page) :
    pagecontent = bitly.getPage(page, sourceSite, bitly.getUserAgent())
    print pagecontent
    match = re.compile('id\=\"iframe\" allowfullscreen\=\"true\" src\=\"(.*?)\"\ ', re.DOTALL)
    for name in match:
        iframesrc = name
        return iframesrc
    return page
