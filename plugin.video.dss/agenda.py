import urllib,urllib2,sys,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,re

from lib.utils import xbmcutil
from datetime import datetime

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])

AddonID ='plugin.video.dss'
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'icon.png'))
    
def showList():
    addDir('Janlul Schedule','http://irc.pcstream.net/admin/data_flat.php?iphone=1',1,icon,fanart)
    addDir('BVLS Schedule','http://bvls2013.com/index.html',2,icon,fanart)

def BVLSSched(url):
    link = Get_url(url)
    datestr=re.compile('<span style="text-decoration: underline;"><b>(.+?)</b></span></span></div>').findall(link)[0]
    datestr = "[B][COLOR gold]"+datestr+"[/COLOR][/B]"
    addLink(datestr,'url','mode',icon,fanart)
    match=re.compile('12px;">(.+?)</span></p>.+?#000000">(.+?)</span></b></p>.+?<p><a href=".+?">(.+?)</a></p>',re.DOTALL).findall(link)
    for timestr, name, stream in match:
        name = timestr + " == " + name + " (" + stream + ")"
        addLink(name,'url','mode',icon,fanart)
    
def JanLulSched(url):
    link = Get_url(url)
    match=re.compile('class="odd">(.+?)</td>.+?<td class="odd">(.+?)</td>.+?<td class="odd">(.+?)</td',re.DOTALL).findall(link)
    for timestr, name, stream in match:
        name = timestr + " == " + name + " (" + stream + ")"
        addLink(name,'url','mode',icon,fanart)
    datestr=re.compile('<title>(.+?)</title>').findall(link)[0]
    datestr = "[B][COLOR gold]"+datestr+"[/COLOR][/B]"
    addLink(datestr,'url','mode',icon,fanart)
    match=re.compile('class="even">(.+?)</td>.+?<td class="even">(.+?)</td>.+?<td class="even">(.+?)</td',re.DOTALL).findall(link)
    for timestr, name, stream in match:
        name = timestr + " == " + name + " (" + stream + ")"
        addLink(name,'url','mode',icon,fanart)
		
def Get_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
    


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

if mode==1:JanLulSched(url)
elif mode==2:BVLSSched(url)









