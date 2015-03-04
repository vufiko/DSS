from ..utils import bitly, xbmcutil
from . import veetle

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 32, 'Mooi dat het zo kan 1')
    mdhzk1 = bitly.getLink('mdhzk1')
    veetle.addChannel('Mooi dat het zo kan - Stream 1', mdhzk1, 'mdhzk')

    xbmcutil.updateProgressBar(pBar, 64, 'Mooi dat het zo kan 2')
    mdhzk2 = bitly.getLink('mdhzk2')
    veetle.addChannel('Mooi dat het zo kan - Stream 2', mdhzk2, 'mdhzk')

    xbmcutil.updateProgressBar(pBar, 96, 'Mooi dat het zo kan 3')
    mdhzk3 = bitly.getLink('mdhzk3')
    veetle.addChannel('Mooi dat het zo kan - Stream 3', mdhzk3, 'mdhzk')

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()
