import sys, urllib2, urllib, os
import xbmcgui, xbmcplugin, xbmc, xbmcaddon

import paths

addon_handle = int(sys.argv[1])
base_url = sys.argv[0]

#pDialog = None
_PERCENT_ = 0
progIncrease = 19

def createProgressBar(title,msg):
    pDialog = xbmcgui.DialogProgress()
    pDialog.create(title, msg)
    return pDialog

def updateProgressBar(pDialog, percent=-1, msg=''):
    global _PERCENT_
    if percent == -1:
        percent = _PERCENT_ + progIncrease
    else:
	    logMessage('hardcoded percentage '+str(percent)+'%')
    _PERCENT_ = percent
    pDialog.update(percent,msg)
	
def addMenuItem(strName, strUrl, bIsPlayable='true', icon=None, fanart=None):
    li = xbmcgui.ListItem(strName)
    if not icon is None :
        iconPath = getIcon(icon)
        li = xbmcgui.ListItem(label=strName, iconImage=iconPath, thumbnailImage=iconPath)
    else :
        li = xbmcgui.ListItem(strName)
    if not fanart is None :
        fanartimg = getFanart(fanart)
        li.setProperty('fanart_image',fanartimg)
    #li.setProperty('IsPlayable', bIsPlayable)
    li.addContextMenuItems([ ('Vernieuwen...', 'Container.Refresh') ])
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=sys.argv[0]+'?play='+strUrl+'&streamName='+strName, listitem=li)

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def logMessage(msg):
    xbmc.log(msg)
	
def endOfList():
    xbmcplugin.endOfDirectory(addon_handle)

def getIcon(streamer):
    icon = os.path.join(paths.iconDir, streamer+'.png')
    if os.path.isfile(icon) :
        icon = icon
    else :
        icon = os.path.join(paths.iconDir, 'default.png')
    return icon
	
def getFanart(streamer):
    fanart = os.path.join(paths.fanartDir, streamer+'.jpg')
    if os.path.isfile(fanart) :
        fanart = fanart
    else :
        fanart = os.path.join(paths.fanartDir, 'default.jpg')
    return fanart

def getTimeout():
    addon = xbmcaddon.Addon('plugin.video.dss')
    reqTimeout = addon.getSetting('reqTimeout')
    print("SETTING: TIMEOUT="+reqTimeout+"sec")
    return int(reqTimeout)

def getResponse(url):
    try:
        response = urllib2.urlopen(url, timeout=getTimeout())
        if response and response.getcode() == 200:
            return response
        else :
            return False
    except:
        return False
