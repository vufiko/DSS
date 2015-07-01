import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,json,base64
from ..utils import bitly, xbmcutil
import urlparse
import random
import xml.etree.ElementTree as ET
from . import veetle
import re

xmlLocation = 'YUhSMGNEb3ZMMlIxZEdOb2MzQnZjblJ6ZEhKbFlXMXpMbU52YlM5NGJXd3ZjRzlzWlM1NGJXdz0='

def addStreams() :
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van Streams...')

    xbmcutil.updateProgressBar(pBar, 15, 'Poleposition - Stream 1')
    addStream('ijs1', 'Poleposition - Stream 1')

    xbmcutil.updateProgressBar(pBar, 30, 'Poleposition - Stream 2')
    addStream('ijs2', 'Poleposition - Stream 2')

    xbmcutil.updateProgressBar(pBar, 45, 'Poleposition - Stream 3')
    addStream('ijs3', 'Poleposition - Stream 3')

    xbmcutil.updateProgressBar(pBar, 60, 'Poleposition - Stream 4')
    addStream('ijs4', 'Poleposition - Stream 4')

    xbmcutil.updateProgressBar(pBar, 75, 'Poleposition - Stream 5')
    addStream('ijs5', 'Poleposition - Stream 5')

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
