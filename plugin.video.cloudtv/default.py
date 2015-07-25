import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,json,base64
import urlparse
import random
import socket, sys, os
from resources.lib.BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
icons = xbmc.translatePath("special://home/addons/plugin.video.cloudtv/resources/icons/")
icon = xbmc.translatePath("special://home/addons/plugin.video.cloudtv/icon.png")
plugin_handle = int(sys.argv[1])
mode = sys.argv[2]

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])




AddonID ='plugin.video.cloudtv'
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'icon.png'))
    


     
def categorie():
    addDir('TV NL', 'plugin://plugin.video.cloudtv/?xcat9x',icon)
    addDir('Regionaal NL', 'plugin://plugin.video.cloudtv/?xcat3x',icon)
    addDir('Lokaal NL', 'plugin://plugin.video.cloudtv/?xcat5x',icon)
    addDir('Sport INT', 'plugin://plugin.video.cloudtv/?xcat4x',icon)
    addDir('Muziek INT', 'plugin://plugin.video.cloudtv/?xcat1x',icon)
    addDir('American Channels', 'plugin://plugin.video.cloudtv/?xcat6x',icon)
    #addDir('Kultuur', 'plugin://plugin.video.cloudtv/?xcat7x',icon)
    #addDir('Entertainment', 'plugin://plugin.video.cloudtv/?xcat8x',icon)
    #addDir('Ongesoorteerd', 'plugin://plugin.video.cloudtv/?xcat2x',icon)
    #addDir('Ongesoorteerd 2', 'plugin://plugin.video.cloudtv/?xcat9x',icon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))    




def addLink(name,url,mode,iconimage,fanart,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def add_video_item(title,url,img):
    url = 'plugin://plugin.video.cloudtv/?playcloud=' + url + '***' + title + '***' + img
    listitem = xbmcgui.ListItem(title, iconImage=img, thumbnailImage=img)
    listitem.setProperty('IsPlayable', 'false')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem)
    return

def playginico():
    xbmcPlayer = xbmc.Player()
    idx = mode.replace("?playcloud=", "").replace("###", "|").replace("#x#", "?").replace("#h#", "http://").split('***')
    xbmc.executebuiltin('XBMC.Notification('+idx[1]+' , Loading Stream !! ,5000,'+idx[2]+')')
    listitem = xbmcgui.ListItem( idx[1], iconImage=idx[2], thumbnailImage=idx[2])
    playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
    playlist.clear()
    url = idx[0]
    print url
    playlist.add( url, listitem )
    xbmcPlayer.play(playlist,None,False)
    sys.exit(0)

    playlist = xbmc.PlayList(1)
    playlist.clear()
    listitem = xbmcgui.ListItem(name + " - " + url, iconImage=icon, thumbnailImage=icon)
    listitem.setInfo("Video", {"Title":name})
    listitem.setProperty('mimetype', 'video/x-msvideo')
    listitem.setProperty('IsPlayable', 'true')
    playlist.add(veetleUrl,listitem)
    xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
    xbmcPlayer.play(playlist)



def addDir(name,url,iconimage):
    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setProperty( "Fanart_Image", icon )
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)



def getSourceUrl(name):
    url = getUrlByName(name)
    return url


def get_url(url):
        response = urllib2.urlopen(url)
        link=response.read()
        response.close()
        return link

def main():	
    xcat = 0
    if 'xcat1' in mode: 
        url = "http://pastebin.com/raw.php?i=bS65z1nd"
    elif 'xcat2' in mode: 
        url = "http://pastebin.com/raw.php?i=btzgYK5X"
    elif 'xcat3' in mode: 
        url = "http://pastebin.com/raw.php?i=U2vNXe4s"
    elif 'xcat4' in mode: 
        url = "http://pastebin.com/raw.php?i=tLWLYU0Y"
    elif 'xcat5' in mode: 
        url = "http://pastebin.com/raw.php?i=n1s2VMXd"
    elif 'xcat6' in mode: 
        url = "http://pastebin.com/raw.php?i=xfx9Dq2X"
    elif 'xcat7' in mode: 
        url = "http://pastebin.com/raw.php?i=n1s2VMXd"
    elif 'xcat8' in mode: 
        url = "http://pastebin.com/raw.php?i=n1s2VMXd"
    elif 'xcat9' in mode: 
        url = "http://pastebin.com/raw.php?i=nvDYYJ5x"
    else:
        categorie()
        sys.exit(0)




    link = get_url(url)
    soup = BeautifulSOAP(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)

    items = soup.findAll("item")
    for item in items:
            try:
                videoTitle=item.title.string
            except: pass
            try:
                if item.thumbnail.string == 'none': thumbnail = icon	
                elif 'http://' in item.thumbnail.string: thumbnail = item.thumbnail.string 
                else: thumbnail = icons + item.thumbnail.string   
            except:
                thumbnail = icon
            try:
                url= item.link.string
            except: pass

            add_video_item(videoTitle,url,thumbnail)
    xbmcplugin.endOfDirectory(plugin_handle)
    sys.exit(0)


if 'playcloud' in mode:
    playginico()
else:
    main()

