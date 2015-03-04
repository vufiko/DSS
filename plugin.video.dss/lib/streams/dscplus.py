from ..utils import bitly, xbmcutil
from . import veetle

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, msg='DSC+ 1')
    dsc1 = bitly.getLink('dsc1')
    veetle.addChannel('DSC+ - Stream 1', dsc1, 'dsc')

    xbmcutil.updateProgressBar(pBar, msg='DSC+ 2')
    dsc2 = bitly.getLink('dsc2')
    veetle.addChannel('DSC+ - Stream 2', dsc2, 'dsc')

    xbmcutil.updateProgressBar(pBar, msg='DSC+ 3')
    dsc3 = bitly.getLink('dsc3')
    veetle.addChannel('DSC+ - Stream 3', dsc3, 'dsc')

    xbmcutil.updateProgressBar(pBar, msg='DSC+ 4')
    dsc4 = bitly.getLink('dsc4')
    veetle.addChannel('DSC+ - Stream 4', dsc4, 'dsc')

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()
