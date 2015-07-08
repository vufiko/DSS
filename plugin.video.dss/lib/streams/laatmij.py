import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,json,base64
from ..utils import bitly, xbmcutil
import urlparse
import random
import xml.etree.ElementTree as ET
from . import veetle
import re



xmlLocation = 'YUhSMGNEb3ZMMlIxZEdOb2MzQnZjblJ6ZEhKbFlXMXpMbU52YlM5NGJXd3ZiR0ZoZEcxcGFpNTRiV3c9'

def addStreams() :
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van Streams...')


    xbmcutil.updateProgressBar(pBar, 15, 'Laatmijmaargaan.nl - stream 1')
    addStream('stream1', 'Laatmijmaargaan.nl - Stream 1')

    xbmcutil.updateProgressBar(pBar, 30, 'Laatmijmaargaan.nl - stream 2')
    addStream('stream2', 'Laatmijmaargaan.nl - Stream 2')

    xbmcutil.updateProgressBar(pBar, 45, 'Laatmijmaargaan.nl - stream 3')
    addStream('stream3', 'Laatmijmaargaan.nl - Stream 3')

    xbmcutil.updateProgressBar(pBar, 60, 'Laatmijmaargaan.nl - stream 4')
    addStream('stream4', 'Laatmijmaargaan.nl - Stream 4')

    xbmcutil.updateProgressBar(pBar, 75, 'Laatmijmaargaan.nl - stream 5')
    addStream('stream5', 'Laatmijmaargaan.nl - Stream 5')

    xbmcutil.updateProgressBar(pBar, 90, 'Laatmijmaargaan.nl - stream 6')
    addStream('stream6', 'Laatmijmaargaan.nl - Stream 6')



    xbmcutil.endOfList()


def addStream(stream, display) :
    streamUrl = getUrlByName(stream) 
    if streamUrl[-4:] == '.flv' :
        print('Veetle')
        veetle.addChannel(display, streamUrl, 'laatmij')
    else :
        print('M3U')
        if (xbmcutil.getResponse(streamUrl)) :
            color = 'green'
        else :
            streamUrl = ''
            color = 'red'
        xbmcutil.addMenuItem('[COLOR '+color+']'+display+'[/COLOR]', streamUrl, 'true', 'laatmij','laatmij')


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