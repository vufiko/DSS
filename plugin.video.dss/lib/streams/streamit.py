from ..utils import xbmcutil, bitly
import urllib2, re

import xml.etree.ElementTree as ET


sourceSite2= 'https://www.youtube.com/embed/BQN63he0m_w?autoplay=1 '

def addStreams() :
    try :
        pagecontent = bitly.getPage(sourceSite2)
        regIframe = re.compile('<a href="http://www.youtube.com/watch\?v=(.*?)">', re.DOTALL)
        streamUrl = regIframe.search(pagecontent).group(1)
        NameIframe = re.compile('<title>(.*?)- YouTube</title>', re.DOTALL)
        name = NameIframe.search(pagecontent).group(1)
        streamXml= 'plugin://plugin.video.youtube/play/?video_id='+ streamUrl
    except :
        streamXml= 'plugin://plugin.video.dss/none'
        name= 'STREAMIT NL'
    xbmcutil.addMenuItem('[COLOR red]Controleer Youtube voor uitzending[/COLOR]','plugin://plugin.video.dss/none' , 'true', None, None)
    xbmcutil.addMenuItem('[COLOR yellow]'+name+'[/COLOR]',streamXml , 'true', None, None)
