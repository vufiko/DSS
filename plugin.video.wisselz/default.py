import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,json,base64
import urlparse
import random
import socket, sys, os



base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

sourceSite = 'http://www.wisselz.com/'


AddonID ='plugin.video.wisselz'
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'icon.png'))
    
def menu():
    addDir('Select a Stream','http://www.wisselz.com',99999999,icon,fanart)
     
    


def WisselzSched(url):
    link = Get_url(url)
    match=re.compile('<option value=\'(.+?)\'>(.+?)</option>',re.DOTALL).findall(link)
    for stream, name in match:
        name = " (" + name + ")"
        strUrl = 'plugin://plugin.video.wisselz/none'
        intern = getLinkByName(stream)
        addLink(name,intern,intern,icon,fanart)




def getLinkByName(stream) :
    compare = stream[0:3].lower()
    if compare == (stream) :
        site = (stream)
    else :
        site = (stream)
    return site
    


   

def GetWisselzStream(name,stream):
    print stream + "stream print"
    streamUrl = findStream(stream)
    veetleUrl = 'plugin://plugin.video.veetle/?channel='+streamUrl
    playlist = xbmc.PlayList(1)
    playlist.clear()
    listitem = xbmcgui.ListItem(name + " - " + url, iconImage=icon, thumbnailImage=icon)
    listitem.setInfo("Video", {"Title":name})
    listitem.setProperty('mimetype', 'video/x-msvideo')
    listitem.setProperty('IsPlayable', 'true')
    playlist.add(veetleUrl,listitem)
    xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
    xbmcPlayer.play(playlist)

def addMenuItem(strName, strUrl, bIsPlayable='true', icon=None, fanart=None):
    li = xbmcgui.ListItem(strName)
    if not icon is None :
        iconPath = icon
        li = xbmcgui.ListItem(label=strName, iconImage=iconPath, thumbnailImage=iconPath)
    else :
        li = xbmcgui.ListItem(strName)
    if not fanart is None :
        fanartimg = fanart
        li.setProperty('fanart_image',fanartimg)
    #li.setProperty('IsPlayable', bIsPlayable)
    li.addContextMenuItems([ ('Vernieuwen...', 'Container.Refresh') ])
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=sys.argv[0]+'?play='+strUrl+'&streamName='+strName, listitem=li)



def findStream(page) :
    page1 = Get_url("http://www.wisselz.com/?stream=" + page)
    page1content = getBaseEncodedString(page1)
    streamUrl = page1content
    return streamUrl

def getBaseEncodedString(url):
    _regex_getM3u = re.compile("http://(.*?)/flv/(.*?)/1.flv", re.DOTALL)
    streamId = _regex_getM3u.search(url).group(2)
    return streamId


def Get_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
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




def getSourceUrl(name):
    url = getUrlByName(name)
    return url











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
elif mode==99999999:WisselzSched(url)
elif mode== mode :GetWisselzStream(name,url)




xbmcplugin.endOfDirectory(int(sys.argv[1]))
