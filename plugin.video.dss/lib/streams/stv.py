from ..utils import bitly, xbmcutil
from . import veetle, sopcast
import re
import base64

sourceSite = 'http://www.sportstv.me'
p2pSite = 'http://p2pcast.tv'
p2p = "http://p2pcast.tv/stream.php?id="
	
def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 50, 'sportstv.me - Stream4')
    addStream('stream4', 'sportstv.me - Stream4')
    #xbmcutil.updateProgressBar(pBar, 12, 'sportstv.me - Stream2')
    #addStream('stream2', 'sportstv.me - Stream2')
    


    
    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()


def addStream(stream, display) :
    streamUrl = findStream(stream) 
    if streamUrl[-4:] == '.flv' :
        print('Veetle')
        veetle.addChannel(display, streamUrl, 'stv')
    else :
        print('M3U')
        if bitly.getResponse(streamUrl) :
            color = 'green'
        else :
            streamUrl = ''
            color = 'red'
        xbmcutil.addMenuItem('[COLOR '+color+']'+display+'[/COLOR]', streamUrl, 'true', 'stv','stv')

    

def findStream(page) :
    page1 = resolveIframe(sourceSite +  '/'+ page + '.html')
    print page1
    if(page1[:4] != 'http') :
            page1 = sourceSite + '/' + page1
    frameHtml = bitly.getPage(page1, sourceSite, bitly.getUserAgent())
    try :
        p2pcast = re.compile('<script type=\'text/javascript\'>id=\'(.*?)\'', re.DOTALL)
        p2pcast = p2pcast.search(frameHtml).group(1)
        print p2pcast
        getp2pcast = resolvep2p(p2pcast)
        streamUrl = getp2pcast
    except :
        b64coded = bitly.getBaseEncodedString(frameHtml)
        streamUrl = bitly.getStreamUrl(b64coded)
        print streamUrl
    return streamUrl
    
def resolveIframe(page) :
    try :
        if(page[:4] != 'http') :
            page = sourceSite + '/' + page 
        pagecontent = bitly.getPage(page, sourceSite, bitly.getUserAgent())
        #print pagecontent
        regIframe = re.compile('iframe\ src\=\"(.*?)\"\ allowfullscreen\=\"true\"', re.DOTALL)
        iframesrc = regIframe.search(pagecontent).group(1)
        return iframesrc
    except :
        return page

def resolvep2p(page) :
    try :
        page1 = p2p + page +  '&live=1&p2p=0&stretching=uniform'
        print page1
        pagecontent = bitly.getPage(page1,p2pSite, bitly.getUserAgent())
        print pagecontent
        regIframe = re.compile('curl = "(.*?)\";', re.DOTALL)
        iframesrc = regIframe.search(pagecontent).group(1)
        print 'iframesrc = '+iframesrc
        url = base64.b64decode(iframesrc)
        print url
        return url
    except :
        return page
    
    

    

