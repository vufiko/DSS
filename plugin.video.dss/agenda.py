import urllib2, xbmcgui, xbmcplugin, urllib, sys
import xml.etree.ElementTree as ET
from datetime import datetime

from lib.utils import *

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])

def showList():
    req = urllib2.Request('http://irc.pcstream.net/admin/data_flat.php?iphone=1')
    response = urllib2.urlopen(req)
    data = response.read()
    response.close()
    root = ET.fromstring(data)
    bodies = root.findall('body')
    for body in bodies :
        tables = body.findall('table')
        for table in tables :
            for tbody in table.findall('tbody') :
                for tr in tbody.findall('tr') :
                    tdata = tr.findall('td')
                    dtime = tdata[0].text
                    dt = datetime.strptime(dtime, "%Y-%m-%d %H:%M:%S")
                    dtime = str(dt.day).rjust(2,'0') + '-' + str(dt.month).rjust(2,'0') + ' ' + str(dt.hour).rjust(2,'0') + ':' + str(dt.minute).rjust(2,'0')
                    ev = tdata[1].text
                    streamer = tdata[2].text
                    strName = '['+dtime + '] ' + ev + ' - [I]'+ streamer + '[/I]'
                    strUrl = 'plugin://plugin.video.dss/none'
                    intern = getLinkByName(streamer)
                    addSubMenu(intern, strName)

def addSubMenu(internal, readable):             
    url = build_url({'site': internal})         
    icon = xbmcutil.getIcon(internal)           
    li = xbmcgui.ListItem(label=readable, iconImage=icon, thumbnailImage=icon)
    fanart = xbmcutil.getFanart(internal)                                     
    li.setProperty('fanart_image',fanart)                                     
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

def build_url(query):                                                                                       
    return base_url + '?' + urllib.urlencode(query) 

def getLinkByName(streamname) :
    compare = streamname[0:3]
    if compare == 'str' :
        site = 'janlul'
    elif compare == 'daz' :
        site = 'daz'
    elif compare == 'Pol' :
        site = 'bdds'
    elif compare == 'Dsp' :
        site = 'daz'
    elif compare == 'stv' :
        site = 'stv'
    elif compare == 'STV' :
        site = 'stv'
    elif compare == 'bvl' :
        site = 'bvls'
    elif compare == 'Str' :
        site = 'sotd'
    elif compare == 'SOT' :
        site = 'sotd'
    else :
        site = 'tvguide'
    return site
