from ..utils import bitly, xbmcutil
from . import veetle
import urllib2

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 16, 'Sports-streams 1')
    spst1 = bitly.getLink('spst1', 'http://www.bvls2013.com/')
    veetle.addChannel('Sports-streams - Stream 1', spst1, 'spst')
    ipAddress = getMicastIp()
    print('micastip='+ipAddress)
    addMicast(ipAddress, 'Sports-streams 2', 'sports2pI6', 'spst', 'spst')
    addMicast(ipAddress, 'Sports-streams 3', 'sports4WfN', 'spst', 'spst')

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()
	
def addMicast(ipAddress, displayName, micastId, icon=None, fanart=None):
    rtmp_url = 'rtmp://'+ipAddress+':443/liveedge/ playpath='+micastId+' swfUrl=http://turbocast.tv/images/player.swf live=1 pageUrl=http://micast.tv/chn2.php?ch='+micastId
    xbmcutil.addMenuItem(displayName, rtmp_url, 'true', icon, fanart)

def getMicastIp():
    strContent = getPage('http://micast.tv/chn.php')
    strDec = getDecString(strContent)
    print(strDec)
    strIp = getPage('http://connexa.org/decode_micast.php?decoded='+strDec)
    return strIp

def getPage(page):
    url = page
    try:
        #headers = {'User-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0'}
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'nl,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'deflate', 'Connection': 'keep-alive'}
        req = urllib2.Request(url ,None, headers)
        response = urllib2.urlopen(req, timeout=xbmcutil.getTimeout())
        data = response.read()
        response.close()
        return data
    except :
        return ''
        print('We failed to open '+url)

def getDecString(content):
    try:
        find_dec = re.compile("dec\(\"(.*?)\"\)" , re.DOTALL)
        decoded = find_dec.search(content).group(1)
        return decoded
    except:
        return ''
