from ..utils import bitly, xbmcutil
from . import veetle

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 49, 'ChahuzoTV - Stream 1')
    ctv1 = bitly.getLink('ctv1')
    veetle.addChannel('ChahuzoTV - Stream 1', ctv1)

    xbmcutil.updateProgressBar(pBar, 98, 'ChahuzoTV - Stream 2')
    ctv2 = bitly.getLink('ctv2')
    veetle.addChannel('ChahuzoTV - Stream 2', ctv2)

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()
