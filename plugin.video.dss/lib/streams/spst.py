from ..utils import bitly, xbmcutil
from . import veetle


sourceSite = 'http://paradiseradio.org'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 33, 'dss 1')
    dss1 = 'http://66.90.103.76:8620/'
    if(xbmcutil.getResponse(dss1)):
        color = 'green'
    else :
        color = 'red'
    xbmcutil.addMenuItem('[COLOR '+color+']paradiseradio.org - Paradise Radio[/COLOR]', dss1, 'true', 'paradise', 'paradise')
	
    xbmcutil.updateProgressBar(pBar, 66, 'dss 2')
    dss2 = 'http://66.90.103.76:8390/'
    if(xbmcutil.getResponse(dss2)):
        color = 'green'
    else :
        color = 'red'
    xbmcutil.addMenuItem('[COLOR '+color+']radiowestland.com - Radio Westland[/COLOR]', dss2, 'true', 'westland', 'westland')

    
    
    
    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()
		
