from ..utils import bitly, xbmcutil
from . import veetle

sourceSite='http://www.sport-x.net/'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')


    xbmcutil.updateProgressBar(pBar, 9, 'Sportx - Stream 1')
    tmp = bitly.getLink('sportx1', sourceSite)
    veetle.addChannel('sportx - Stream 1', tmp, 'sportx')

    xbmcutil.updateProgressBar(pBar, 18, 'Sportx - Stream 2')
    tmp = bitly.getLink('sportx2', sourceSite)
    veetle.addChannel('sportx - Stream 2', tmp, 'sportx')

    xbmcutil.updateProgressBar(pBar, 27, 'Sportx - Stream 3')
    tmp = bitly.getLink('sportx3', sourceSite)
    veetle.addChannel('sportx - Stream 3', tmp, 'sportx')

    xbmcutil.updateProgressBar(pBar, 36, 'Sportx - Stream 4')
    tmp = bitly.getLink('sportx4', sourceSite)
    veetle.addChannel('sportx - Stream 4', tmp, 'sportx')

    xbmcutil.updateProgressBar(pBar, 45, 'Sportx - Stream 5')
    tmp = bitly.getLink('sportx5', sourceSite)
    veetle.addChannel('sportx - Stream 5', tmp, 'sportx')

    xbmcutil.updateProgressBar(pBar, 54, 'Sportx - Stream 6')
    tmp = bitly.getLink('sportx6', sourceSite)
    veetle.addChannel('sportx - Stream 6', tmp, 'sportx')

    xbmcutil.updateProgressBar(pBar, 63, 'Sport-x - Stream 7')
    tmp = bitly.getLink('sportx7', sourceSite)
    veetle.addChannel('sportx - Stream 7', tmp, 'sportx')

    xbmcutil.updateProgressBar(pBar, 72, 'Sport-x - Stream 8')
    tmp = bitly.getLink('sportx8', sourceSite)
    veetle.addChannel('sportx - Stream 8', tmp, 'sportx')

    xbmcutil.updateProgressBar(pBar, 81, 'Sportx - Stream 9')
    tmp = bitly.getLink('sportx9', sourceSite)
    veetle.addChannel('sportx - Stream 9', tmp, 'sportx')

    xbmcutil.updateProgressBar(pBar, 90, 'Sportx - Stream 10')
    tmp = bitly.getLink('sportx10', sourceSite)
    veetle.addChannel('sportx - Stream 10', tmp, 'sportx')

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()
