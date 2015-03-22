from ..utils import bitly, xbmcutil
from . import veetle, sopcast
import re

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

    xbmcutil.updateProgressBar(pBar, 56, 'STV Streams - Flash 5')
    stv5 = bitly.getLink('stv-5', sourceSite)
    veetle.addChannel('STV Streams - Flash 5', stv5, 'stv')

    xbmcutil.updateProgressBar(pBar, 64, 'STV Streams - Flash 6')
    stv6 = bitly.getLink('stv-6', sourceSite)
    veetle.addChannel('STV Streams - Flash 6', stv6, 'stv')

    
    xbmcutil.updateProgressBar(pBar, 84, 'STV Streams - ACE HD')
    hd1hash = bitly.getAceHash('http://stvstreams.com/flash1/stvacehd.html')
    sopcast.addAceStream('STV Streams - ACE HD', hd1hash, 'stv')
    
    xbmcutil.updateProgressBar(pBar, 96, 'STV Streams - ACE HD 2')
    hd2hash = bitly.getAceHash('http://stvstreams.com/flash1/stvacehd2.html')
    sopcast.addAceStream('STV Streams - ACE HD 2',hd2hash, 'stv')
    
    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()

