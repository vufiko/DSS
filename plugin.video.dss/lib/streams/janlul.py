import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,json,base64
from ..utils import bitly, xbmcutil
import urlparse
import random
import xml.etree.ElementTree as ET
from . import veetle
import re



xmlLocation = 'YUhSMGNEb3ZMMlIxZEdOb2MzQnZjblJ6ZEhKbFlXMXpMbU52YlM5NGJXd3ZhbUZ1YkhWc0xuaHRiQT09'

def addStreams() :
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van Streams...')


    xbmcutil.updateProgressBar(pBar, 15, 'JanLul.com - stream 1')
    addStream('janlul1', 'JanLul.com - Stream 1')

    xbmcutil.updateProgressBar(pBar, 30, 'JanLul.com - stream 2')
    addStream('janlul2', 'JanLul.com - Stream 2')

    xbmcutil.updateProgressBar(pBar, 45, 'JanLul.com - stream 3')
    addStream('janlul3', 'JanLul.com - Stream 3')

    xbmcutil.updateProgressBar(pBar, 60, 'JanLul.com - stream 4')
    addStream('janlul4', 'JanLul.com - Stream 4')

    xbmcutil.updateProgressBar(pBar, 75, 'JanLul.com - stream 5')
    addStream('janlul5', 'JanLul.com - Stream 5')

    xbmcutil.updateProgressBar(pBar, 90, 'JanLul.com - stream 6')
    addStream('janlul6', 'JanLul.com - Stream 6')



    xbmcutil.endOfList()


def addStream(stream, display) :
    streamUrl = getUrlByName(stream) 
    if streamUrl[-4:] == '.flv' :
        print('Veetle')
        veetle.addChannel(display, streamUrl, 'janlul')
    else :
        print('M3U')
        if (xbmcutil.getResponse(streamUrl)) :
            color = 'green'
        else :
            streamUrl = ''
            color = 'red'
        xbmcutil.addMenuItem('[COLOR '+color+']'+display+'[/COLOR]', streamUrl, 'true', 'janlul','janlul')


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


    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()
