#
#      Copyright (C) 2013 Sean Poyser
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#


import urllib
import urllib2
import re
import xbmc
import xbmcaddon
import xbmcplugin
import xbmcgui
import datetime
import time
import os
import common

ADDONID  = 'plugin.audio.radiowestland'
ADDON    = xbmcaddon.Addon(ADDONID)
HOME     = ADDON.getAddonInfo('path')
TITLE    = 'Paradise Radio More Music'
VERSION  =  ADDON.getAddonInfo('version')
URL      = 'http://shoutcast.radiowestland.com:8390/listen.pls'
ICON     =  os.path.join(HOME, 'icon.png')
FANART   =  os.path.join(HOME, 'fanart.jpg')
GETTEXT  = ADDON.getLocalizedString


_PLAYNOW     = 100
_REQUEST     = 200
_LETTER      = 300
_TRACK       = 400
_RECORD      = 500
_SLIDESHOW   = 600
_PODCASTS    = 700
_PLAYPODCAST = 800
_NOWPLAYING  = 900

MODE_FREE   = 1000
MODE_SONG   = 1100
MODE_ARTIST = 1200
MODE_IGNORE = 1300


def StartSlideShow():
    import slideshow
    slideshow.Start()


def Play():
    slideshow = (ADDON.getSetting('AUTO') == 'true')

    pl = xbmc.PlayList(xbmc.PLAYLIST_MUSIC)
    pl.clear()    
    pl.add(URL)

    if slideshow:
        #necessary otherwise XBMC gets stuck
        #showing "Working" notification
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

    xbmc.Player().play(pl)

    if slideshow:
        xbmc.sleep(1000)
        StartSlideShow()







def GetRecent(response):
    recent = []

    match = re.compile('color="CCDDDD"><b>(.+?)</b>').findall(response)   
    for artist in match:
        recent.append(artist)
            
    return recent




def IsPlayingRAM():
    if not xbmc.Player().isPlayingAudio():
        return False

    pl         = xbmc.PlayList(xbmc.PLAYLIST_MUSIC)
    label      = pl[0].getLabel().upper()
    return label == 'Paradise Radio More Music'
    

def IsPlaying(message):
    if IsPlayingRAM():
        return True

    dialog = xbmcgui.Dialog()
    if dialog.yesno(TITLE, message,  GETTEXT(30027), '', GETTEXT(30028), GETTEXT(30029)) == 1:
        return False    

    Play()
    return xbmc.Player().isPlayingAudio()






def Main():   
    addDir(GETTEXT(30036), _PLAYNOW,     False)
    #addDir(GETTEXT(30039), _SLIDESHOW,   False)
    

    play = ADDON.getSetting('PLAY')=='true'
    if play and not xbmc.Player().isPlayingAudio():
        Play()



def addLetter(letter):
    thumbnail = ICON#'DefaultPlaylist.png'
    u         = sys.argv[0]
    u        += '?letter=' + letter
    u        += '&mode='   + str(_LETTER)
    liz       = xbmcgui.ListItem(letter, iconImage=thumbnail, thumbnailImage=thumbnail)

    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)


def addDir(name, mode, isFolder):
    thumbnail = ICON
    u         = sys.argv[0] + '?mode=' + str(mode)        
    liz       = xbmcgui.ListItem(name, iconImage=thumbnail, thumbnailImage=thumbnail)

    liz.setProperty('Fanart_Image', FANART)

    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)

   
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



params = get_params()
mode   = None


try:
    mode=int(params['mode'])
except:
    pass

if mode == None:
    Main()

elif mode == _PLAYNOW:
    Play()


elif mode == _REQUEST:
    if IsPlaying(GETTEXT(30030)):
        Request()

elif mode == _LETTER:
    try:
        letter=urllib.unquote_plus(params['letter'])
        RequestLetter(letter)
    except:
        pass

elif mode == _SLIDESHOW:
    if IsPlaying(GETTEXT(30041)):
        StartSlideShow()


elif mode == _TRACK:    
    try:
        url=urllib.unquote_plus(params['url'])
        RequestURL(url)
    except:
        pass



elif mode == MODE_SONG:
    ShowError(GETTEXT(30043))


elif mode == MODE_ARTIST:
    ShowError(GETTEXT(30044))



    
try:    
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
except:
    pass
