import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,json,base64
from ..utils import bitly, xbmcutil
import urlparse
import random
import xml.etree.ElementTree as ET
from . import veetle
import re

xmlLocation = 'YUhSMGNEb3ZMMlIxZEdOb2MzQnZjblJ6ZEhKbFlXMXpMbU52YlM5NGJXd3ZjMjkwWkM1NGJXdz0='

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 32, 'Stream of the Day - Stream 1')
    addStream('index', 'Stream of the Day - Stream  1')
    

    xbmcutil.updateProgressBar(pBar, 64, 'Stream of the Day - Stream 2')
    addStream('stream2', 'Stream of the Day - Stream  2')

    xbmcutil.updateProgressBar(pBar, 80, 'Stream of the Day - Stream 3')
    addStream('stream3', 'Stream of the Day - Stream  3')

    xbmcutil.updateProgressBar(pBar, 98, 'Stream of the Day - Stream 4')
    addStream('stream4', 'Stream of the Day - Stream  4')

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

