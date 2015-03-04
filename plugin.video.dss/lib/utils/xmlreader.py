import urllib2, bitly
import xml.etree.ElementTree as ET

xmlLocation = 'YUhSMGNITTZMeTl1YkhOd2IzSjBjeTVuYjI5bmJHVmpiMlJsTG1OdmJTOW5hWFF2YzI5MWNtTmxjeTU0Yld3PQ=='

def getUrlByName(name):
    req = urllib2.Request(bitly.getStreamUrl(bitly.getStreamUrl(xmlLocation)) ,None)
    response = urllib2.urlopen(req)
    data = response.read()
    response.close()
    root = ET.fromstring(data)
    return root.find('./stream[name="'+name+'"]/url').text
