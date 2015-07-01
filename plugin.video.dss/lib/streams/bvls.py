import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,json,base64
from ..utils import bitly, xbmcutil
import urlparse
import random
import xml.etree.ElementTree as ET
from . import veetle
import re

xmlLocation = 'YUhSMGNEb3ZMMlIxZEdOb2MzQnZjblJ6ZEhKbFlXMXpMbU52YlM5NGJXd3ZZblpzY3pJd01UTXVlRzFz'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')


    xbmcutil.updateProgressBar(pBar, 9, 'BVLS - Stream 1')
    addStream('stream1', 'BVLS - Stream 1')
    
    xbmcutil.updateProgressBar(pBar, 18, 'BVLS - Stream 2')
    addStream('stream2', 'BVLS - Stream 2')

    xbmcutil.updateProgressBar(pBar, 27, 'BVLS - Stream 3')
    addStream('stream3', 'BVLS - Stream 3')

    xbmcutil.updateProgressBar(pBar, 36, 'BVLS - Stream 4')
    addStream('stream4', 'BVLS - Stream 4')

    xbmcutil.updateProgressBar(pBar, 45, 'BVLS - Stream 5')
    addStream('stream5', 'BVLS - Stream 5')

    xbmcutil.updateProgressBar(pBar, 54, 'BVLS - Stream 6')
    addStream('stream6', 'BVLS - Stream 6')

    xbmcutil.updateProgressBar(pBar, 63, 'BVLS - Stream 7')
    addStream('stream7', 'BVLS - Stream 7')

    xbmcutil.updateProgressBar(pBar, 72, 'BVLS - Stream 8')
    addStream('stream8', 'BVLS - Stream 8')

    xbmcutil.updateProgressBar(pBar, 81, 'BVLS - Stream 9')
    addStream('stream9', 'BVLS - Stream 9')

    xbmcutil.updateProgressBar(pBar, 90, 'BVLS - Stream 10')
    addStream('stream10', 'BVLS - Stream 10')

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
