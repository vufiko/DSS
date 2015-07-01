import urllib2, re, base64
import xbmcutil

def getResponse(url, referer=None, ua=None) :
    if getPage(url, referer, ua) == "":
        return False
    else :
        return True


	
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

