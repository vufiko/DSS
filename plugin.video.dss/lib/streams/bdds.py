from ..utils import bitly, xbmcutil
from . import veetle
import re

sourceSite = 'http://www.polepositionv2.nl'

def addStreams() :
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van Streams...')

    xbmcutil.updateProgressBar(pBar, 49, 'Poleposition - Stream 1')
    addStream('ijs1', 'Poleposition - Stream 1')

    xbmcutil.updateProgressBar(pBar, 98, 'Poleposition - Stream 2')
    addStream('ijs2', 'Poleposition - Stream 2')

    xbmcutil.endOfList()


def addStream(stream, display) :
    streamUrl = findStream(stream) 
    if streamUrl[-4:] == '.flv' :
        veetle.addChannel(display, streamUrl, 'Poleposition')
    else :
        if bitly.getResponse(streamUrl) :
            color = 'green'
        else :
            streamUrl = ''
            color = 'red'
        xbmcutil.addMenuItem('[COLOR '+color+']'+display+'[/COLOR]', streamUrl, 'true', 'pole','pole')


def findStream(page) :
    ua = bitly.getUserAgent()
    page1 = resolveIframe(sourceSite + '/' + page +'.html')
    page2 = resolveIframe(page1)
    page2content = bitly.getPage(page2, sourceSite, ua)
    b64coded = bitly.getBaseEncodedString(page2content)
    streamUrl = bitly.getStreamUrl(b64coded)
    return streamUrl
    
def resolveIframe(page) :
    try :
        if(page[:4] != 'http') :
            page = sourceSite + '/' + page
        userAgent = bitly.getUserAgent()
        pagecontent = bitly.getPage(page, sourceSite, userAgent)
        regIframe = re.compile('iframe src="(.*)" name="iframe_name"')
        iframesrc = regIframe.search(pagecontent).group(1)
        return iframesrc
    except :
        return page
