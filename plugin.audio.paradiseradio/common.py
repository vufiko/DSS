import urllib
import geturllib
import os
import xbmc
import xbmcaddon

ADDONID = 'plugin.audio.paradiseradio'

geturllib.SetCacheDir(os.path.join(xbmc.translatePath(xbmcaddon.Addon(ADDONID).getAddonInfo('profile')).decode('utf-8'), 'cache'))


def GetHTML(url, useCache = True, referer=None):
    if useCache:
        html = geturllib.GetURL(url, 1800, referer=referer)
    else:
        html = geturllib.GetURLNoCache(url, referer=referer)

    html  = html.replace('\n', '')
    return html