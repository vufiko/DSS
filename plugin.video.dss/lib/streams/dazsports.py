import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,json,base64
from ..utils import bitly, xbmcutil
import urlparse
import random
import xml.etree.ElementTree as ET
from . import veetle
import re

xmlLocation = 'YUhSMGNEb3ZMMlIxZEdOb2MzQnZjblJ6ZEhKbFlXMXpMbU52YlM5NGJXd3ZaR0Y2YzNCdmNuUnpMbmh0YkE9PQ=='

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')
    xbmcutil.updateProgressBar(pBar, 33, 'DazSports 3')
    addStream('player3','DazSports - Stream 3')
   
    xbmcutil.updateProgressBar(pBar, 66, 'DazSports 4')
    addStream('player4','DazSports - Stream 4')
    
    xbmcutil.updateProgressBar(pBar, 99, 'DazSports 5')
    addStream('player5','DazSports - Stream 5')
    xbmcutil.endOfList()

    
def addStream(stream, display) :
    streamUrl = getUrlByName(stream) 
    if streamUrl[-4:] == '.flv' :
        veetle.addChannel(display, streamUrl, 'daz')
    else :
        if bitly.getResponse(streamUrl) :
            color = 'green'
        else :
            streamUrl = ''
            color = 'red'
        xbmcutil.addMenuItem('[COLOR '+color+']'+display+'[/COLOR]', streamUrl, 'true', 'daz','daz')


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
