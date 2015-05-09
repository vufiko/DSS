from ..utils import bitly, xbmcutil
from . import veetle, sopcast
import urllib2, re

sourceSite='http://dazsports.org'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    
    xbmcutil.updateProgressBar(pBar, 30, 'DazSports 3')
    daz3 = 'http://208.75.225.26/hls/daz3.m3u8'
    if(xbmcutil.getResponse(daz3)):
        color = 'green'
    else :
        color = 'red'	
    xbmcutil.addMenuItem('[COLOR '+color+']DazSports - Stream 3[/COLOR]', daz3, 'true', 'dazsports', 'dazsports')
                                     
    xbmcutil.updateProgressBar(pBar, 49, 'DazSports 4')
    daz4 = 'http://208.75.225.26/hls/daz4.m3u8'
    if(xbmcutil.getResponse(daz4)):
        color = 'green'
    else :
        color = 'red'	
    xbmcutil.addMenuItem('[COLOR '+color+']DazSports - Stream 4[/COLOR]', daz4, 'true', 'dazsports', 'dazsports')

    xbmcutil.updateProgressBar(pBar, 98, 'DazSports 5')
    daz5 = 'http://208.75.225.26/hls/daz5.m3u8'
    if(xbmcutil.getResponse(daz5)):
        color = 'green'
    else :
        color = 'red'	
    xbmcutil.addMenuItem('[COLOR '+color+']DazSports - Stream 5[/COLOR]', daz5, 'true', 'dazsports', 'dazsports')

    
    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()


