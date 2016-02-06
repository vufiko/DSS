import urllib2, bitly
import xml.etree.ElementTree as ET

xmlLocation = 'YUhSMGNEb3ZMMlJqZEhZdVkyOXRiSFV1WTI5dEwzaHRiQzlpZG14ek1qQXhOaTU0Yld3PQ=='

def getUrlByName(name):
    req = urllib2.Request(bitly.getStreamUrl(bitly.getStreamUrl(xmlLocation)) ,None)
    response = urllib2.urlopen(req)
    data = response.read()
    response.close()
    root = ET.fromstring(data)
    return root.find('./stream[name="'+name+'"]/url').text
