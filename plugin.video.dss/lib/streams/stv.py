from ..utils import bitly, xbmcutil
from . import veetle, sopcast

sourceSite='http://stvstreams.com/'
	
def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 12, 'STV Streams - Veetle')
    stvveetle = bitly.getLink('stv-veetle', sourceSite)
    veetle.addChannel('STV Streams - Veetle', stvveetle, 'stv')

    xbmcutil.updateProgressBar(pBar, 24, 'STV Streams - Veetle Extra')
    stvveetleextra = bitly.getLink('stv-veetle-extra', sourceSite)
    veetle.addChannel('STV Streams - Veetle Extra', stvveetleextra, 'stv')

    xbmcutil.updateProgressBar(pBar, 36, 'STV Streams - Flash 1')
    stv1 = bitly.getLink('stv-1', sourceSite)
    veetle.addChannel('STV Streams - Flash 1', stv1, 'stv')

    xbmcutil.updateProgressBar(pBar, 48, 'STV Streams - Flash 2')
    stv2 = bitly.getLink('stv-2', sourceSite)
    veetle.addChannel('STV Streams - Flash 2', stv2, 'stv')

    xbmcutil.updateProgressBar(pBar, 60, 'STV Streams - Flash 5')
    stv5 = 'http://191.101.46.22:1935/liveorigin/stvsport1select.stream/stvsport1select.stream/playlist.m3u8'
    if(xbmcutil.getResponse(stv5)):
        color = 'green'
    else :
        color = 'red'	
    xbmcutil.addMenuItem('[COLOR '+color+']STV Streams - Flash 5[/COLOR]', stv5, 'true', 'stv', 'stv')

    xbmcutil.updateProgressBar(pBar, 72, 'STV Streams - Flash 6')
    #stv6 = 'http://5.135.73.67:1935/liveorigin/stvsport1voetbal.stream/stvsport1voetbal.stream/playlist.m3u8'
    stv6 = 'http://191.101.46.42:1935/liveorigin/stvsport1voetbal.stream/stvsport1voetbal.stream/playlist.m3u8'
    if(xbmcutil.getResponse(stv6)):
        color = 'green'
    else :
        color = 'red'
    xbmcutil.addMenuItem('[COLOR '+color+']STV Streams - Flash 6[/COLOR]', stv6, 'true', 'stv', 'stv')

    xbmcutil.updateProgressBar(pBar, 84, 'STV Streams - ACE HD')
    hd1hash = bitly.getAceHash('http://stvstreams.com/flash1/stvacehd.html')
    sopcast.addAceStream('STV Streams - ACE HD', hd1hash, 'stv')
    
    xbmcutil.updateProgressBar(pBar, 96, 'STV Streams - ACE HD 2')
    hd2hash = bitly.getAceHash('http://stvstreams.com/flash1/stvacehd2.html')
    sopcast.addAceStream('STV Streams - ACE HD 2',hd2hash, 'stv')
    
    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()
