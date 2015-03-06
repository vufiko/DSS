from ..utils import bitly, xbmcutil
from . import veetle
import urllib2, re

sourceSite='http://footdirect24.com'

def addStreams():
    #xbmcutil.addMenuItem('DAZ Sports 1', 'micast://')
    #xbmcutil.addMenuItem('DAZ Sports 2', 'micast://')
    print("IP OF MICAST = " + getMicastIp())
    ipAddress = getMicastIp()
    print('micastip='+ipAddress)
    
    addMicast(ipAddress, 'footdirect24-streams 1', 'sat78', 'sportx1', 'sportx1')
    addMicast(ipAddress, 'footdirect24-streams 3', 'sporttv4', 'sportx3', 'sportx3')
    addMicast(ipAddress, 'footdirect24-streams 4', 'live5', 'sportx4', 'sportx4')
    addMicast(ipAddress, 'footdirect24-streams 5', 'my6', 'sportx5', 'sportx5')
    addMicast(ipAddress, 'footdirect24-streams 6', 'sporttv22', 'sportx6', 'sportx6')
    addMicast(ipAddress, 'footdirect24-streams 7', 'my88', 'sportx7', 'sportx7')
    addMicast(ipAddress, 'footdirect24-streams 8', 'my99', 'sportx8', 'sportx8')

    
    xbmcutil.endOfList()

def addMicast(ipAddress, displayName, micastId, icon=None, fanart=None):
    rtmp_url = 'rtmp://'+ipAddress+':443/liveedge/ playpath='+micastId+' swfUrl=http://turbocast.tv/images/player.swf live=1 pageUrl=http://micast.tv/chn2.php?ch='+micastId
    xbmcutil.addMenuItem(displayName, rtmp_url, 'true', icon, fanart)

def getMicastIp():
    strContent = getPage('http://micast.tv/chn2.php')
    strDec = getDecString(strContent)
    strIp = getPage('http://connexa.org/decode_micast.php?decoded='+strDec)
    return strIp

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
