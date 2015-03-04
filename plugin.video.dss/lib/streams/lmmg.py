from ..utils import bitly, xbmcutil
from . import veetle

sourceSite="http://laatmijmaargaan.nl/"

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 32, 'LMMG - Stream 1')
    lmmg1 = bitly.getLink('lmmg1', sourceSite)
    veetle.addChannel('LaatMijMaarGaan - Stream 1', lmmg1, 'lmmg')

    xbmcutil.updateProgressBar(pBar, 64, 'LMMG - Stream 2')
    lmmg2 = bitly.getLink('lmmg2', sourceSite)
    veetle.addChannel('LaatMijMaarGaan - Stream 2', lmmg2, 'lmmg')
	
    xbmcutil.updateProgressBar(pBar, 96, 'LMMG - Stream 3')
    lmmg3 = bitly.getLink('lmmg3', sourceSite)
    veetle.addChannel('LaatMijMaarGaan - Stream 3', lmmg3, 'lmmg')

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()
