from ..utils import bitly, xbmcutil
from . import veetle, sopcast
import urllib2, re

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 16, 'Sports-streams 1')
    spst1 = bitly.getLink('spst1', 'http://www.bvls2013.com/')
    veetle.addChannel('Sports-streams - Stream 1', spst1, 'spst')
    print("IP OF MICAST = " + getMicastIp())
    ipAddress = getMicastIp()
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
    strIp = GetIP(strDec)
    return strIp
	
def GetIP(xcoded):
    return ''.join([chr(ord(c) ^ 123) for c in xcoded])

def getPage(page):
    url = page
    try:
        #headers = {'User-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0'}
        req = urllib2.Request(url ,None)
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
