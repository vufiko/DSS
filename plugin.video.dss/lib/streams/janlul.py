from ..utils import bitly, xbmcutil
from . import veetle


sourceSite = 'http://janlul.com'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sport Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 16, 'JanLul 1')
    # jl_stream1 = bitly.getLink('janlul1', sourceSite)
    # veetle.addChannel('JanLul.com - Stream 1', jl_stream1, 'janlul')
    janlul1 = 'http://cctv-lh.akamaihd.net/i/janlul1_live@125119/master.m3u8'
    if(xbmcutil.getResponse(janlul1)):
        color = 'green'
    else :
        color = 'red'
    xbmcutil.addMenuItem('[COLOR '+color+']JanLul.com - Stream 1[/COLOR]', janlul1, 'true', 'janlul', 'janlul')
	
    xbmcutil.updateProgressBar(pBar, 32, 'JanLul 2')
    #jl_stream2 = bitly.getLink('janlul2', sourceSite)
    #veetle.addChannel('JanLul.com - Stream 2', jl_stream2, 'janlul')
    janlul2 = 'http://cctv-lh.akamaihd.net/i/janlul2_live@125116/master.m3u8'
    if(xbmcutil.getResponse(janlul2)):
        color = 'green'
    else :
        color = 'red'
    xbmcutil.addMenuItem('[COLOR '+color+']JanLul.com - Stream 2[/COLOR]', janlul2, 'true', 'janlul', 'janlul')

    xbmcutil.updateProgressBar(pBar, 48, 'JanLul 3')
    jl_stream3 = bitly.getLink('janlul3', sourceSite)
    veetle.addChannel('JanLul.com - Stream 3', jl_stream3, 'janlul')

    xbmcutil.updateProgressBar(pBar, 64, 'JanLul 4')
    jl_stream4 = bitly.getLink('janlul4', sourceSite)
    veetle.addChannel('JanLul.com - Stream 4', jl_stream4, 'janlul')

    xbmcutil.updateProgressBar(pBar, 80, 'JanLul 5')
    jl_stream5 = bitly.getLink('janlul5', sourceSite)
    veetle.addChannel('JanLul.com - Stream 5', jl_stream5, 'janlul')

    xbmcutil.updateProgressBar(pBar, 96, 'JanLul 6')
    # jl_stream6 = bitly.getLink('janlul6', sourceSite)
    # veetle.addChannel('JanLul.com - Stream 6', jl_stream6, 'janlul')
    janlul6 = 'http://stream.ssh101.com/hls/janlul6.m3u8'
    if(xbmcutil.getResponse(janlul6)):
        color = 'green'
    else :
        color = 'red'
    xbmcutil.addMenuItem('[COLOR '+color+']JanLul.com - Stream 6[/COLOR]', janlul6, 'true', 'janlul', 'janlul')
    
    
    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()
