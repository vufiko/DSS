import urllib2, bitly
import xml.etree.ElementTree as ET

xmlLocation = 'YUhSMGNEb3ZMM0JoYzNSbFltbHVMbU52YlM5eVlYY3VjR2h3UDJrOVF6ZHpaWE0wUms0PQ=='

def getUrlByName(name):
    req = urllib2.Request(bitly.getStreamUrl(bitly.getStreamUrl(xmlLocation)) ,None)
    response = urllib2.urlopen(req)
    data = response.read()
    response.close()
    root = ET.fromstring(data)
    return root.find('./stream[name="'+name+'"]/url').text
