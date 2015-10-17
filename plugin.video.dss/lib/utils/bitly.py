import urllib2, re, base64, xmlreader, ua
import xbmcutil

def getResponse(url, referer=None, ua=None) :
    if getPage(url, referer, ua) == "":
        return False
    else :
        return True

def getSourceUrl(name):
    url = xmlreader.getUrlByName(name)
    return url

def getUserAgent():
    #link = basesite + 'getua.php'
    #return getPage(link)
    return ua.getUa()

def getLink(streamName, referer=None):
    userAgent = getUserAgent()
    pagecontent = getPage(getSourceUrl(streamName), referer, userAgent)
    base64 = getBaseEncodedString(pagecontent)
    return getStreamUrl(base64)
    
def getIdByUrl(url):
    _regex_getM3u = re.compile("http://(.*?)/flv/(.*?)/1.flv", re.DOTALL)
    streamId = _regex_getM3u.search(url).group(2)
    return streamId
	
def getPage(page, referer=None, ua=None):                                
    url = page                                                           
    try:                                                                 
        req = urllib2.Request(url ,None)                                                                          
        if(referer is not None):                                                                                  
            req.add_header('Referer', referer)                                                                    
                                                                                                                  
        if(ua is not None):                                                                                       
            req.add_header('User-Agent', ua)                                                                      
                                                                                                                  
        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')               
        req.add_header('Accept-Language', 'nl,en-US;q=0.7,en;q=0.3')                                              
        req.add_header('Accept-Encoding', 'deflate')                                                        
        req.add_header('Connection', 'keep-alive')                                                                
        response = urllib2.urlopen(req, timeout=xbmcutil.getTimeout())                                            
        data = response.read()                                                                                    
        response.close()                                                                                          
        if(ua is None) :                                                                                          
            print(data)                                                                            
        return str(data)                                                                           
    except :                                                                                       
        return ''                                                                                  
        print('We failed to open '+url)

def getBaseEncodedString(streamPage):
    try:
        _regex_encodedstring = re.compile("file\s*\:\s*window\.atob\(\'(.*?)\'\)" , re.DOTALL)
        baseEncoded = _regex_encodedstring.search(streamPage).group(1)
        return baseEncoded
    except:
        return ''

def getStreamUrl(baseEncoded):
    return base64.b64decode(baseEncoded)

def getAceHash(webpage):
    try:
        pagecontent = getPage(webpage)
        # search for: http://torrentstream.org/embed/{ACEHASH}?autoplay=1
        _regex_getM3u = re.compile("http://torrentstream.org/embed/(.*?)\?autoplay", re.DOTALL)
        streamId = _regex_getM3u.search(pagecontent).group(1)
        return streamId
    except:
        return ''
	
def resolveTorrentTv(webpage):
    pagecontent = getPage(webpage)
    # Search for loadPlayer("{acehash}",{autoplay: true});
    _regex_getM3u = re.compile("loadPlayer\(\"(.*?)\",{autoplay: true}", re.DOTALL)
    streamId = _regex_getM3u.search(pagecontent).group(1)
    return streamId
