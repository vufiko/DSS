from ..utils import bitly, xbmcutil
from . import veetle
import re

sourceSite = 'http://www.streamoftheday.com'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 32, 'Stream of the Day - Stream 1')
    tmp = getLink('index')
    veetle.addChannel('Stream of the Day - Stream  1', tmp, 'sotd')

    xbmcutil.updateProgressBar(pBar, 64, 'Stream of the Day - Stream 2')
    tmp = getLink('stream2')
    veetle.addChannel('Stream of the Day - Stream 2', tmp, 'sotd')

    xbmcutil.updateProgressBar(pBar, 80, 'Stream of the Day - Stream 3')
    tmp = getLink('stream3')
    veetle.addChannel('Stream of the Day - Stream 3', tmp, 'sotd')

    xbmcutil.updateProgressBar(pBar, 98, 'Stream of the Day - Stream 4')
    tmp = getLink('stream4')
    veetle.addChannel('Stream of the Day - Stream 4', tmp, 'sotd')

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()

def getLink(streamName) :
    pageContent = bitly.getPage(sourceSite + '/' + streamName + '.html', sourceSite, bitly.getUserAgent())
    veetleId = findVeetleId(pageContent)
    iframeSource = bitly.getPage("http://www.streamoftheday.com/streamx.php?id="+veetleId, bitly.getUserAgent())
    base64 = bitly.getBaseEncodedString(iframeSource)
    return bitly.getStreamUrl(base64)

def findVeetleId(url):
    _regex_getM3u = re.compile('src="http://www\.streamoftheday\.com/streamx\.php\?id\=(.*?)" name="iframe_name"', re.DOTALL)
    streamId = _regex_getM3u.search(url).group(1)
    return streamId

