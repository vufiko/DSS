import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,json,base64
from ..utils import bitly, xbmcutil
import urlparse
import random
import xml.etree.ElementTree as ET
from . import veetle
import re

xmlLocation = 'YUhSMGNEb3ZMMlIxZEdOb2MzQnZjblJ6ZEhKbFlXMXpMbU52YlM5NGJXd3ZjM0J2Y25ReExuaHRiQT09'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 30, 'Sport 1 Voetbal - HD')
    addStream('stream1', 'Sport 1 Voetbal - HD')
    

    xbmcutil.updateProgressBar(pBar, 60, 'Sport 1 Voetbal - SD')
    addStream('stream2', 'Sport 1 Voetbal - SD')



    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()

def addStream(stream, display) :
    streamUrl = getUrlByName(stream) 
    if streamUrl[-4:] == '.flv' :
        print('Veetle')
        veetle.addChannel(display, streamUrl, 'BVLS')
    else :
        print('M3U')
        if (xbmcutil.getResponse(streamUrl)) :
            color = 'green'
        else :
            streamUrl = ''
            color = 'red'
        xbmcutil.addMenuItem('[COLOR '+color+']'+display+'[/COLOR]', streamUrl, 'true', 'BVLS','BVLS')


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

