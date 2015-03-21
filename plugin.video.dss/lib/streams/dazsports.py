from ..utils import bitly, xbmcutil
from . import veetle, sopcast
import urllib2, re

sourceSite='http://dazsports.org'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')
    #xbmcutil.addMenuItem('DAZ Sports 1', 'micast://')
    #xbmcutil.addMenuItem('DAZ Sports 2', 'micast://')
    print("IP OF MICAST = " + getMicastIp())
    ipAddress = getMicastIp()
    #Micast ip decoder tested
    #addMicast(ipAddress, 'Sports 1', 'esportestv29D2', 'daz', 'daz')
    #addMicast(ipAddress, 'Sports 2', 'esportestv3FSr', 'daz', 'daz')
    #addMicast(ipAddress, 'Sports 3', 'sporttv1', 'daz', 'daz')
    addMicast(ipAddress, 'DAZ Sports 3', 'dazsports3stR', 'daz', 'daz')
    #addMicast(ipAddress, 'DAZ Sports 4', 'daz2I2S', 'daz', 'daz')
    #addMicast(ipAddress, 'DAZ Sports 5', 'daz1yZ1', 'daz', 'daz')
    
    xbmcutil.updateProgressBar(pBar, 49, 'DazSports 4')
    daz_stream4 = bitly.getLink('daz4', sourceSite)
    veetle.addChannel('DazSports - Stream 4', daz_stream4, 'daz')

    xbmcutil.updateProgressBar(pBar, 98, 'DazSports 5')
    daz_stream5 = bitly.getLink('daz5', sourceSite)
    veetle.addChannel('DazSports - Stream 5', daz_stream5, 'daz')    
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
