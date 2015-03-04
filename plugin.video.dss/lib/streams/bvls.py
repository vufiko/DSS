from ..utils import bitly, xbmcutil
from . import veetle

sourceSite='http://www.bvls2013.com/'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')


    xbmcutil.updateProgressBar(pBar, 9, 'BVLS - Stream 1')
    tmp = bitly.getLink('bvls1', sourceSite)
    veetle.addChannel('BVLS - Stream 1', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 18, 'BVLS - Stream 2')
    tmp = bitly.getLink('bvls2', sourceSite)
    veetle.addChannel('BVLS - Stream 2', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 27, 'BVLS - Stream 3')
    tmp = bitly.getLink('bvls3', sourceSite)
    veetle.addChannel('BVLS - Stream 3', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 36, 'BVLS - Stream 4')
    tmp = bitly.getLink('bvls4', sourceSite)
    veetle.addChannel('BVLS - Stream 4', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 45, 'BVLS - Stream 5')
    tmp = bitly.getLink('bvls5', sourceSite)
    veetle.addChannel('BVLS - Stream 5', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 54, 'BVLS - Stream 6')
    tmp = bitly.getLink('bvls6', sourceSite)
    veetle.addChannel('BVLS - Stream 6', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 63, 'BVLS - Stream 7')
    tmp = bitly.getLink('bvls7', sourceSite)
    veetle.addChannel('BVLS - Stream 7', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 72, 'BVLS - Stream 8')
    tmp = bitly.getLink('bvls8', sourceSite)
    veetle.addChannel('BVLS - Stream 8', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 81, 'BVLS - Stream 9')
    tmp = bitly.getLink('bvls9', sourceSite)
    veetle.addChannel('BVLS - Stream 9', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 90, 'BVLS - Stream 10')
    tmp = bitly.getLink('bvls10', sourceSite)
    veetle.addChannel('BVLS - Stream 10', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()
