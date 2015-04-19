from ..utils import bitly, xbmcutil
from . import veetle, sopcast
import re


sourceSite = 'http://stvstreams.com'
	
def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 12, 'STV Streams - Veetle')
    addStream('stvveetle', 'STV Streams - Veetle')

    xbmcutil.updateProgressBar(pBar, 24, 'STV Streams - Veetle Extra')
    addStream('stvveetleextra', 'STV Streams - Veetle Extra')
    

    xbmcutil.updateProgressBar(pBar, 36, 'STV Streams - Flash 1')
    addStream('stvflash1', 'STV Streams - Flash 1')
    

    xbmcutil.updateProgressBar(pBar, 48, 'STV Streams - Flash 2')
    addStream('stvflash2', 'STV Streams - Flash 2')


    xbmcutil.updateProgressBar(pBar, 56, 'STV Streams - Flash 5')
    addStream('stvflash5', 'STV Streams - Flash 5')
    

    xbmcutil.updateProgressBar(pBar, 64, 'STV Streams - Flash 6')
    addStream('stvflash6', 'STV Streams - Flash 6')
    

    
    xbmcutil.updateProgressBar(pBar, 84, 'STV Streams - ACE HD')
    hd1hash = bitly.getAceHash('http://stvstreams.com/flash1/stvacehd.html')
    sopcast.addAceStream('STV Streams - ACE HD', hd1hash, 'stv')
    
    xbmcutil.updateProgressBar(pBar, 96, 'STV Streams - ACE HD 2')
    hd2hash = bitly.getAceHash('http://stvstreams.com/flash1/stvacehd2.html')
    sopcast.addAceStream('STV Streams - ACE HD 2',hd2hash, 'stv')
    
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
    page1 = resolveIframe(sourceSite + '/streams/' + page +'.html')
    frameHtml = bitly.getPage(page1, sourceSite, bitly.getUserAgent())
    b64coded = bitly.getBaseEncodedString(frameHtml)
    print b64coded
    streamUrl = bitly.getStreamUrl(b64coded)
    print streamUrl
    return streamUrl
    
def resolveIframe(page) :
    try :
        if(page[:4] != 'http') :
            page = sourceSite + '/' + page
        userAgent = bitly.getUserAgent()
        pagecontent = bitly.getPage(page, sourceSite, userAgent)
        regIframe = re.compile('iframe\ src\=\"(.*?)\"\ allowfullscreen\=\"true\"', re.DOTALL)
        iframesrc = regIframe.search(pagecontent).group(1)
        return iframesrc
    except :
        return page


    
    

    

