import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,json,base64
import urlparse
import random
import xml.etree.ElementTree as ET
import socket, sys, os

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

AddonID ='plugin.video.janlultv'
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'icon.png'))
    
def menu():
    addDir('Janlul Schedule','http://www.ikkijkonline.nl/api/j7F5GfnZ8uJ76Fp2/stream_guide/janlul',98,icon,fanart)
    addLink('janlul 1 TV','janlul1',99,icon,fanart)
    addLink('janlul 2 TV','janlul2',99,icon,fanart)
    addLink('janlul 3 TV','janlul3',99,icon,fanart)
    addLink('janlul 4 TV','janlul4',99,icon,fanart)
    addLink('janlul 5 TV','janlul5',99,icon,fanart)
    addLink('janlul 6 TV','janlul6',99,icon,fanart)
    addLink('janlul 7 TV','janlul7',99,icon,fanart)
    addLink('janlul 8 TV','janlul8',99,icon,fanart)
    addLink('janlul 9 TV','janlul9',99,icon,fanart)
    addLink('janlul 10 TV','janlul10',99,icon,fanart)
    addLink('janlul 11 TV','janlul11',99,icon,fanart)
    addLink('janlul 12 TV','janlul12',99,icon,fanart)
    addLink('janlul 13 TV','janlul13',99,icon,fanart)
    addLink('janlul 14 TV','janlul14',99,icon,fanart)
    addLink('janlul 15 TV','janlul15',99,icon,fanart) 
    
def JanLulSched(url):
    link = Get_url(url)
    match=re.compile('<tr><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td></tr>',re.DOTALL).findall(link)
    for timestr, name, stream in match:
        name = timestr + " == " + name + " (" + stream + ")"
        strUrl = 'plugin://plugin.video.janlultv/none'
        intern = getLinkByName(stream)
        addLink(name,intern,99,icon,fanart)
        print addLink

def getLinkByName(stream) :
    compare = stream
    if compare == 'Janlul 1' :
        site = 'janlul1'
    elif compare == 'Janlul 2' :
        site = 'janlul2'
    elif compare == 'Janlul 3' :
        site = 'janlul3'
    elif compare == 'Janlul 4' :
        site = 'janlul4'
    elif compare == 'Janlul 5' :
        site = 'janlul5'
    elif compare == 'Janlul 6' :
        site = 'janlul6'
    elif compare == 'Janlul 7' :
        site = 'janlul7'
    elif compare == 'Janlul 8' :
        site = 'janlul8'
    elif compare == 'Janlul 9' :
        site = 'janlul9'
    elif compare == 'Janlul 10' :
        site = 'janlul10'
    elif compare == 'Janlul 11' :
        site = 'janlul11'
    elif compare == 'Janlul 12' :
        site = 'janlul12'
    elif compare == 'Janlul 13' :
        site = 'janlul13'
    elif compare == 'Janlul 14' :
        site = 'janlul14'
    elif compare == 'Janlul 15' :
        site = 'janlul15'
    return site
    
def GetJanlulStream(name,stream):
    streamUrl = getUrlByName(stream)
    print streamUrl
    if streamUrl[-4:] == '.m3u' :
       getUrl = re.compile("http://veetle.com/index.php/hls/streamMbrFast/(.*?)/stream.m3u", re.DOTALL)
       streamId = getUrl.search(streamUrl).group(1)
       url = 'http://veetle.com/index.php/hls/streamMbrFast/'+streamId + '/stream.m3u8'
    else :
        url = streamUrl
    playlist = xbmc.PlayList(1)
    xbmc.executebuiltin('XBMC.Notification('+name+' , Loading Stream !! ,5000,'+icon+')')
    playlist.clear()
    listitem = xbmcgui.ListItem(name + " - " + url, iconImage=icon, thumbnailImage=icon)
    listitem.setInfo("Video", {"Title":name})
    listitem.setProperty('mimetype', 'video/x-msvideo')
    listitem.setProperty('IsPlayable', 'true')
    playlist.add(url,listitem)
    xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
    xbmcPlayer.play(playlist)

def Get_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Linux; U; Android 4.2.2; nl-nl; GT-P5110 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
   
def Play(name,url):  
    ok=True
    liz=xbmcgui.ListItem(name, iconImage=icon,thumbnailImage=icon); liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
    xbmc.Player().play(url, liz, False)
    return ok

def addLink(name,url,mode,iconimage,fanart,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDir(name,url,mode,iconimage,fanart,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

xmlLocation = 'YUhSMGNEb3ZMMkpwZEd4NUxtTnZiUzlxWVc1c2RXeDBkZz09'

def getUrlByName(name):
    req = urllib2.Request(getStreamUrl(getStreamUrl(xmlLocation)) ,None)
    response = urllib2.urlopen(req)
    data = response.read()
    response.close()
    root = ET.fromstring(data)
    streams = root.findall("stream")
    for stream in streams:
        if stream.find("name").text == name:
            return stream.find("url").text
    return ''

def getStreamUrl(baseEncoded):
    return base64.b64decode(baseEncoded)

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]    
        return param
           
params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None

try:url=urllib.unquote_plus(params["url"])
except:pass
try:name=urllib.unquote_plus(params["name"])
except:pass
try:mode=int(params["mode"])
except:pass
try:iconimage=urllib.unquote_plus(params["iconimage"])
except:pass
print "Mode: "+str(mode);print "URL: "+str(url);print "Name: "+str(name);print "IconImage: "+str(iconimage)

if mode==None or url==None or len(url)<1:menu()
elif mode==98:JanLulSched(url)
elif mode==99:GetJanlulStream(name,url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
