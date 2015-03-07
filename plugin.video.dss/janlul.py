from ..utils import bitly, xbmcutil
from . import veetle
import re

sourceSite = 'http://janlul.com/channel'

def addStreams():
    pBar = xbmcutil.createProgressBar('Steun Janlul SMS "donate stream" naar 7733', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 16, 'JanLul 1')
    tmp = findStream('jl1')
    veetle.addChannel('JanLul.com - Stream 1', tmp, 'janlul')

    xbmcutil.updateProgressBar(pBar, 32, 'JanLul 2')
    tmp = findStream('jl2')
    veetle.addChannel('JanLul.com - Stream 2', tmp, 'janlul')

    xbmcutil.updateProgressBar(pBar, 48, 'JanLul 3')
    tmp = findStream('jl3')
    veetle.addChannel('JanLul.com - Stream 3', tmp, 'janlul')

    xbmcutil.updateProgressBar(pBar, 64, 'JanLul 4')
    tmp = findStream('jl4')
    veetle.addChannel('JanLul.com - Stream 4', tmp, 'janlul')

    xbmcutil.updateProgressBar(pBar, 80, 'JanLul 5')
    tmp = findStream('jl5')
    veetle.addChannel('JanLul.com - Stream 5', tmp, 'janlul')

    xbmcutil.updateProgressBar(pBar, 96, 'JanLul 6')
    tmp = findStream('jl6')
    veetle.addChannel('JanLul.com - Stream 6', tmp, 'janlul')

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()

def findStream(stream):
    page = bitly.getPage(sourceSite + '/' + stream + '.html', sourceSite, bitly.getUserAgent())
    match=re.compile('src="(.+?)" name="iframe_name"').findall(page)[0]
    frameHtml = bitly.getPage(match,sourceSite, bitly.getUserAgent())
    base64 = bitly.getBaseEncodedString(frameHtml)
    return bitly.getStreamUrl(base64)
