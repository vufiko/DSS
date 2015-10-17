import urllib2, re, base64

def getIdByUrl(url):
    _regex_getM3u = re.compile("http://(.*?)/flv/(.*?)/1.flv", re.DOTALL)
    streamId = _regex_getM3u.search(url).group(2)
    return streamId

def getBaseEncodedString(streamPage):
    _regex_encodedstring = re.compile("window\.atob\(\'(.*?)\'\)" , re.DOTALL)
    baseEncoded = _regex_encodedstring.search(streamPage).group(1)
    return baseEncoded

def getStreamUrl(baseEncoded):
    return base64.b64decode(baseEncoded)