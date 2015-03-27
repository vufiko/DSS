import urllib2
import re
import common

ROOT = 'http://fanart.tv/'
NAME = 'Fanart.TV'

def GetImages(artist):
    if artist == '':
        return []

    artist = artist.upper().replace(' & ',' ').replace(',','+').replace('(','').replace(')','').replace(' ','+')
    artist = artist.replace('++', '+')

    try:
        url    = ROOT + 'api/getdata.php?type=2&s=' + artist
        images = []

        #print NAME + ' 1st URL requested: %s' % url
        link = common.GetHTML(url)

        max = -1
        url = None

        match = re.compile('<div class="item-name"><a href="/(.+?)".+?<span class="pop">(.+?)</span>').findall(link)
        for link, qty in match:
            qty = int(qty)
            if max < qty:
                max = qty
                url = link

        if not url:
            return images

        url = ROOT + url
    
        #print NAME + ' 2nd URL requested: %s' % url
        link = common.GetHTML(url)

        match = re.compile('href="/fanart/(.+?).(?:jpg|png|jpeg|JPG)"').findall(link)

        for img in match:
            if img + '.jpg' in link:
                images.append(ROOT+'fanart/'+img+'.jpg')
            elif img + '.JPG' in link:
                images.append(ROOT+'fanart/'+img+'.JPG')
            elif img + '.jpeg' in link:
                images.append(ROOT+'fanart/'+img+'.jpeg')
    except Exception, e:
        pass

    #print NAME + ' Found - %d images' % len(images)
    return images
