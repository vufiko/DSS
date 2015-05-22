import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,json,base64
import urlparse
import random
import xml.etree.ElementTree as ET

import socket, sys, os



base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

sourceSite = 'http://www.janlul.com/'
xmlLocation = 'YUhSMGNEb3ZMM0JoYzNSbFltbHVMbU52YlM5eVlYY3VjR2h3UDJrOVUzQjVSbGwyT1drPQ=='

AddonID ='plugin.video.janlultv'
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'icon.png'))
    
def menu():
    addDir('Janlul Schedule','http://irc.pcstream.net/admin/data_flat.php?iphone=1',1,icon,fanart)
    addLink('janlul 1 TV','janlul1',2,icon,fanart)
    addLink('janlul 2 TV','janlul2',2,icon,fanart)
    addLink('janlul 3 TV','janlul3',2,icon,fanart)
    addLink('janlul 4 TV','janlul4',2,icon,fanart)
    addLink('janlul 5 TV','janlul5',2,icon,fanart)
    addLink('janlul 6 TV','janlul6',2,icon,fanart)
    addLink('janlul 7 TV','janlul7',2,icon,fanart)
    addLink('janlul 8 TV','janlul8',2,icon,fanart)
    addLink('janlul 9 TV','janlul9',2,icon,fanart)
    addLink('janlul 10 TV','janlul10',2,icon,fanart)
    addLink('janlul 11 TV','janlul11',2,icon,fanart)
    addLink('janlul 12 TV','janlul12',2,icon,fanart)
    addLink('janlul 13 TV','janlul13',2,icon,fanart)
    addLink('janlul 14 TV','janlul14',2,icon,fanart)
    addLink('janlul 15 TV','janlul15',2,icon,fanart) 
    


def JanLulSched(url):
    link = Get_url(url)
    match=re.compile('class="odd">(.+?)</td>.+?<td class="odd">(.+?)</td>.+?<td class="odd">(.+?)</td',re.DOTALL).findall(link)
    for timestr, name, stream in match:
        name = timestr + " == " + name + " (" + stream + ")"
        addLink(name,'url','mode',icon,fanart)
    



   

def GetJanlulStream(name,stream):
    streamUrl = findStream(stream)
    url = streamUrl
    playlist = xbmc.PlayList(1)
    playlist.clear()
    listitem = xbmcgui.ListItem(name + " - " + url, iconImage=icon, thumbnailImage=icon)
    listitem.setInfo("Video", {"Title":name})
    listitem.setProperty('mimetype', 'video/x-msvideo')
    listitem.setProperty('IsPlayable', 'true')
    playlist.add(url,listitem)
    xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
    xbmcPlayer.play(playlist)


def findStream(page) :
    page1 = getSourceUrl(page)
    page1content = Get_url(page1)
    streamUrl = page1content
    if streamUrl[-4:] == '.m3u' :
        streamUrl = streamUrl + '8'
    return streamUrl


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
elif mode==1:JanLulSched(url)
elif mode==2:GetJanlulStream(name,url)

elif mode==100:Play(name,url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
