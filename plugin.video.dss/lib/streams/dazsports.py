from ..utils import bitly, xbmcutil
from . import veetle, sopcast
import urllib2, re

sourceSite='http://dazsports.org'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')
    xbmcutil.updateProgressBar(pBar, 33, 'DazSports 3')
    addStream('player3','DazSports - Stream 3')
   
    xbmcutil.updateProgressBar(pBar, 66, 'DazSports 4')
    addStream('player4','DazSports - Stream 4')
    
    xbmcutil.updateProgressBar(pBar, 99, 'DazSports 5')
    addStream('player5','DazSports - Stream 5')
    xbmcutil.endOfList()

    
def addStream(stream, display) :
    streamUrl = findStream(stream) 
    if streamUrl[-4:] == '.flv' :
        veetle.addChannel(display, streamUrl, 'daz')
    else :
        if bitly.getResponse(streamUrl) :
            color = 'green'
        else :
            streamUrl = ''
            color = 'red'
        xbmcutil.addMenuItem('[COLOR '+color+']'+display+'[/COLOR]', streamUrl, 'true', 'daz','daz')


def findStream(page) :
    ua = bitly.getUserAgent()
    page1 = resolveIframe(sourceSite + '/' + page +'.php')
    pagecontent = bitly.getPage(sourceSite + '/' + page1, sourceSite, ua)
    b64coded = bitly.getBaseEncodedString(pagecontent)
    streamUrl = bitly.getStreamUrl(b64coded)
    return streamUrl
    
def resolveIframe(page) :
    try :
        if(page[:4] != 'http') :
            page = sourceSite + '/' + page
        userAgent = bitly.getUserAgent()
        pagecontent = bitly.getPage(page, sourceSite, userAgent)
        regIframe = re.compile('<iframe(.*?)src="(.*?)"(.*?)><\/iframe>', re.DOTALL)
        iframesrc = regIframe.search(pagecontent).group(2)
        return iframesrc
    except :
        return page
