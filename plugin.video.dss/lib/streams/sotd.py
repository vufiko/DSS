from ..utils import bitly, xbmcutil
from . import veetle
import re

sourceSite = 'http://www.streamoftheday.com'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 32, 'Stream of the Day - Stream 1')
    sotd_stream1 = getLink('sotd1', sourceSite)
    veetle.addChannel('Stream of the Day - Stream  1', sotd_stream1, 'sotd')

    xbmcutil.updateProgressBar(pBar, 64, 'Stream of the Day - Stream 2')
    sotd_stream2 = getLink('sotd2', sourceSite)
    veetle.addChannel('Stream of the Day - Stream 2', sotd_stream2, 'sotd')

    xbmcutil.updateProgressBar(pBar, 98, 'Stream of the Day - Stream 3')
    sotd_stream3 = getLink('sotd3', sourceSite)
    veetle.addChannel('Stream of the Day - Stream 3', sotd_stream3, 'sotd')

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()

def getLink(streamName, referer=None) :
    userAgent = bitly.getUserAgent()
    pageContent = bitly.getPage(bitly.getSourceUrl(streamName), referer, userAgent)
    veetleId = findVeetleId(pageContent)
    iframeSource = bitly.getPage("http://www.streamoftheday.com/streamx.php?id="+veetleId, referer, userAgent)
    base64 = bitly.getBaseEncodedString(iframeSource)
    return bitly.getStreamUrl(base64)

def findVeetleId(url):
    _regex_getM3u = re.compile('src="http://www\.streamoftheday\.com/streamx\.php\?id\=(.*?)" name="iframe_name"', re.DOTALL)
    streamId = _regex_getM3u.search(url).group(1)
    return streamId

