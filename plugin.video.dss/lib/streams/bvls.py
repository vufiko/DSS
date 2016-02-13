from ..utils import bitly, xbmcutil, xmlreader, sos
from . import veetle
import re

sourceSite='http://bvls2016.sc/'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')


    xbmcutil.updateProgressBar(pBar, 9, 'BVLS - Stream 1')
    addStream('stream1', 'BVLS - Stream 1')
    
    xbmcutil.updateProgressBar(pBar, 18, 'BVLS - Stream 2')
    addStream('stream2', 'BVLS - Stream 2')

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

    xbmcutil.updateProgressBar(pBar, 91, 'BVLS - Stream 10')
    addStream('stream10', 'BVLS - Stream 10')

    xbmcutil.updateProgressBar(pBar, 95, 'BVLS - Stream 11')
    addStream('stream11', 'BVLS - Stream 10')

    xbmcutil.updateProgressBar(pBar, 98, 'BVLS - Stream 12')
    addStream('stream12', 'BVLS - Stream 12')

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
    try :
        url = sourceSite+page+'.html'
        url2 = sos.GetStream(url)
        page1 = sourceSite+url2
        frameHtml = bitly.getPage(page1, sourceSite, bitly.getUserAgent())
        b64coded = bitly.getBaseEncodedString(frameHtml)
        print b64coded
        streamUrl = bitly.getStreamUrl(b64coded)
        print streamUrl
        return streamUrl
    except :
        return page
    
def resolveIframe(page) :
    pagecontent = bitly.getPage(page, sourceSite, bitly.getUserAgent())
    regIframe = re.compile('id\=\"iframe\" allowfullscreen\=\"true\" src\=\"(.*?)\"\ ', re.DOTALL)
    iframesrc = regIframe.search(pagecontent).group(1)
    return iframesrc
    return page
