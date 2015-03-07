from ..utils import bitly, xbmcutil
from . import veetle
import re

sourceSite='http://www.bvls2013.com/'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')


    xbmcutil.updateProgressBar(pBar, 9, 'BVLS - Stream 1')
    tmp = findStream('stream1')
    veetle.addChannel('BVLS - Stream 1', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 18, 'BVLS - Stream 2')
    tmp = findStream('stream2')
    veetle.addChannel('BVLS - Stream 2', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 27, 'BVLS - Stream 3')
    tmp = findStream('stream3')
    veetle.addChannel('BVLS - Stream 3', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 36, 'BVLS - Stream 4')
    tmp = findStream('stream4')
    veetle.addChannel('BVLS - Stream 4', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 45, 'BVLS - Stream 5')
    tmp = findStream('stream5')
    veetle.addChannel('BVLS - Stream 5', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 54, 'BVLS - Stream 6')
    tmp = findStream('stream6')
    veetle.addChannel('BVLS - Stream 6', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 63, 'BVLS - Stream 7')
    tmp = findStream('stream7')
    veetle.addChannel('BVLS - Stream 7', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 72, 'BVLS - Stream 8')
    tmp = findStream('stream8')
    veetle.addChannel('BVLS - Stream 8', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 81, 'BVLS - Stream 9')
    tmp = findStream('stream9')
    veetle.addChannel('BVLS - Stream 9', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 90, 'BVLS - Stream 10')
    tmp = findStream('stream10')
    veetle.addChannel('BVLS - Stream 10', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()

def findStream(stream):
    page = bitly.getPage(sourceSite + '/' + stream + '.html', sourceSite, bitly.getUserAgent())
    match=re.compile('src="(.+?)" id="myfr"').findall(page)[0]
    frameHtml = bitly.getPage(match,sourceSite, bitly.getUserAgent())
    base64 = bitly.getBaseEncodedString(frameHtml)
    return bitly.getStreamUrl(base64)
