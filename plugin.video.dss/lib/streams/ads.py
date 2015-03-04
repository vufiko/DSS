from ..utils import bitly, xbmcutil
from . import veetle

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 49, 'Achterdijn Sports - Stream 1')
    ads1 = bitly.getLink('ads1')
    veetle.addChannel('Achterdijn Sports - Stream 1', ads1, 'ads')

    xbmcutil.updateProgressBar(pBar, 98, 'Achterdijn Sports - Stream 2')
    ads2 = bitly.getLink('ads2')
    veetle.addChannel('Achterdijn Sports - Stream 2', ads2, 'ads')

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()
