import urllib2, sys, socket
from ..utils import xbmcutil, stream

def addChannel(name, url, internal=None):
    print(internal)
    try:
        response = urllib2.urlopen(url, timeout=xbmcutil.getTimeout())
    	if response and response.getcode() == 200:
            displayName = '[COLOR green]'+name+'[/COLOR]'
            veetleId = stream.getIdByUrl(url)
            veetleUrl = 'plugin://plugin.video.veetle/?channel='+veetleId
            xbmcutil.addMenuItem(displayName, veetleUrl, 'true', internal, internal)
            xbmcutil.logMessage('SUCCESS: ' + name + ' ['+url+'] is successfully added!')
        else:
            print("Response code: "+response.getcode())
            xbmcutil.logMessage('NOTICE: ' + name + ' is offline!')
            xbmcutil.addMenuItem('[COLOR red]'+name+'[/COLOR]', 'plugin://plugin.video.dss/none', 'false', internal, internal)
    except:
        e = sys.exc_info()[0]
        print( "Error: %s" % e )
        xbmcutil.logMessage('NOTICE: ' + name + ' is offline!')
        xbmcutil.addMenuItem('[COLOR red]'+name+'[/COLOR]', 'plugin://plugin.video.dss/none', 'false', internal, internal)

def startSocket():
    HOST = '127.0.0.1'   # Symbolic name, meaning all available interfaces
    PORT = 9000 # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket created'
    #Bind socket to local host and port
    try:
        s.bind((HOST, PORT))
    except:
        print 'Address '+HOST+':'+str(PORT)+' is already in use'
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
    print 'Socket bind complete'
    #Start listening on socket
    s.close()
