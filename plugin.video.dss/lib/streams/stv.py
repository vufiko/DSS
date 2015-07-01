import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,json,base64
from ..utils import bitly, xbmcutil
import urlparse
import random
import xml.etree.ElementTree as ET
from . import veetle
import re

xmlLocation = 'YUhSMGNEb3ZMMlIxZEdOb2MzQnZjblJ6ZEhKbFlXMXpMbU52YlM5NGJXd3ZjM1IyYzNSeVpXRnRjeTU0Yld3PQ=='
	
def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 12, 'STV Streams - Veetle')
    addStream('stvveetle', 'STV Streams - Veetle')

    xbmcutil.updateProgressBar(pBar, 24, 'STV Streams - Veetle Extra')
    addStream('stvveetleextra', 'STV Streams - Veetle Extra')
    

    xbmcutil.updateProgressBar(pBar, 36, 'STV Streams - Flash 1')
    addStream('stvflash1', 'STV Streams - Flash 1')
    

    xbmcutil.updateProgressBar(pBar, 48, 'STV Streams - Flash 2')
    addStream('stvflash2', 'STV Streams - Flash 2')


    xbmcutil.updateProgressBar(pBar, 56, 'STV Streams - Flash 5')
    addStream('stvflash5', 'STV Streams - Flash 5')
    

    xbmcutil.updateProgressBar(pBar, 64, 'STV Streams - Flash 6')
    addStream('stvflash6', 'STV Streams - Flash 6')
    

    
    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()


def addStream(stream, display) :
    streamUrl = getUrlByName(stream) 
    if streamUrl[-4:] == '.flv' :
        print('Veetle')
        veetle.addChannel(display, streamUrl, 'stv')
    else :
        print('M3U')
        if bitly.getResponse(streamUrl) :
            color = 'green'
        else :
            streamUrl = ''
            color = 'red'
        xbmcutil.addMenuItem('[COLOR '+color+']'+display+'[/COLOR]', streamUrl, 'true', 'stv','stv')

    
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
    

    

