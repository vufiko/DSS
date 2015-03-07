import sys, urllib2, urllib
import xbmcgui
import xbmcplugin, xbmcaddon
import urlparse
import paths
import agenda

import socket, sys

from lib.streams import *
from lib.utils import *

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

pDialog = xbmcgui.DialogProgress()
_PERCENT_ = 0
progIncrease = 19

xbmcplugin.setContent(addon_handle, 'movies')

addon = xbmcaddon.Addon('plugin.video.dss')
newFeatures = addon.getSetting('newFeatures')

def addSubMenu(internal, readable):
    print 'adding ' + internal
    url = build_url({'site': internal})
    icon = xbmcutil.getIcon(internal)
    li = xbmcgui.ListItem(label=readable, iconImage=icon, thumbnailImage=icon)
    fanart = xbmcutil.getFanart(internal)
    li.setProperty('fanart_image',fanart)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

def mainMenu():
    addSubMenu('agenda','[COLOR yellow]Wedstrijd Schema[/COLOR]')
    addSubMenu('janlul','Janlul')
    addSubMenu('daz','DAZ Sports')
    addSubMenu('stv','STV Streams')
    addSubMenu('13stream','13stream')
    addSubMenu('bvls','BVLS2013')
    addSubMenu('sotd','Stream of the Day')
    if newFeatures == "true":
        addSubMenu('sportx','Footdirect24')
    addDummyItem('')
    addDummyItem('[COLOR green]Online Stream[/COLOR]')
    addDummyItem('[COLOR red]Offline Stream[/COLOR]')
    addDummyItem('[COLOR yellow]Luister ook naar paradiseradio.org[/COLOR]')
    xbmcplugin.endOfDirectory(addon_handle)

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)
    
def addDummyItem(labelString, icon=False, iconName = '', fanart=False, fanartName=''):
    if icon:
        iconimg = xbmcutil.getIcon(iconName)
        li = xbmcgui.ListItem(label=labelString, iconImage=iconimg, thumbnailImage=iconimg)
    else:
        li = xbmcgui.ListItem(label=labelString)

    li.setProperty('IsPlayable','false')
    if fanart:
        fanartimg = xbmcutil.getFanart(fanartName)
        li.setProperty('fanart_image',fanartimg)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url='plugin://plugin.video.dss/none', listitem=li)

argSite = args.get('site', None)
playUrl = args.get('play', None)
p2pMode = args.get('mode', None)
streamName = args.get('streamName', None)


if argSite is None:
    if playUrl is None :
        mainMenu()
    else :
        if p2pMode is not None :
            playUrl[0] = str(playUrl[0]) + "&mode=" + str(p2pMode[0])
        while xbmc.Player().isPlaying():
            xbmc.Player().stop()
            xbmc.sleep(5)
        pl=xbmc.PlayList(1)
        pl.clear()
        #credits = os.path.join(paths.videoDir, 'credits.mp4')
        #li = xbmcgui.ListItem('Credits')
        #li.setProperty('IsPlayable','true')
        #xbmc.PlayList(1).add(credits, li)
        li = xbmcgui.ListItem(str(streamName[0]))
        li.setProperty('IsPlayable', 'true')
        xbmc.PlayList(1).add(str(playUrl[0]), li)
        xbmc.Player().play(pl)
else:
    site = argSite[0]
    pDialog.create('Dutch Sports Streams', 'Laden van streams...')
    if site == 'agenda':
        agenda.showList()
    elif site == 'janlul': #Janlul.com
        janlul.addStreams()
    elif site == 'daz': #DazSports.org
        dazsports.addStreams()
    elif site == 'stv': #STV-Streams.com
        stv.addStreams()
    elif site == 'ctv':
        ctv.addStreams()
    elif site == 'sotd': #sports-streams.com
        sotd.addStreams()
    elif site == 'bvls': #bvls2013.com
        bvls.addStreams()
    elif site == '13stream':
        sopcast.add13Stream()
    elif site == 'sportx': #sport-x.net
        sportx.addStreams()
    
    

    xbmcplugin.endOfDirectory(addon_handle)
