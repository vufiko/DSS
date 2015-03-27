import urllib2
import re
import common

ROOT = 'http://www.allmusic.com/artist/'
NAME = 'All.Music'


def GetImages(artist):
    if artist == '':
        return []

    artist = artist.upper().replace(' & ',' ').replace(',','+').replace('(','').replace(')','').replace(' ','+')
    artist = artist.replace('++', '+')

    images = []

    try:        
        url = GetURL(artist)

        print NAME + ' 2nd URL requested: %s' % url

        if url != '':
            link = common.GetHTML(url, referer=ROOT)
            link = link.replace('\n', '')

            #image1 = re.compile('<meta name="image" content="(.+?).jpg').search(link).group(1)
            #images.append(image1+'.jpg')

            gallery = link.split('Photo Gallery', 1)[1]
            gallery = gallery.split('<span class', 1)[0]
            gallery = gallery.replace('_jpg', '*j*p*g')

            match   = re.compile('<img src="(.+?).jpg').findall(gallery)
            for img in match:
                #if 'cps-static.rovicorp.com/3' in img:
                if 'rovi' in img:                
                    img   = img.replace('*j*p*g', '_jpg')
                    img = img.replace('170', '500')
                    images.append(img+'.jpg')

    except Exception, e:
        print str(e)
        pass

    #print NAME + ' Found - %d images' % len(images)
    return images


def GetURL(artist):
    try:
        reverse = ''
        split   = artist.split('+')
        for item in split:
            reverse = item + reverse
        forward = artist.replace('+', '')

        #NB forward and reverse DO NOT contain any '+'

        url = 'http://www.allmusic.com/search/artists/' + artist
   
        print NAME + ' 1st URL requested: %s' % url           
        link = common.GetHTML(url, referer=ROOT)

        match = re.compile('<a href="/artist/(.+?)" data-tooltip.+?alt="(.+?)">').findall(link)

        for url, artist in match:
            artist = artist.replace(' ', '').upper()
            if (forward in artist) or (reverse in artist):
                return ROOT + url

        #all else fails, just return the first one
        return ROOT + match[0][0]

    except Exception, e:
        print str(e)
        pass

    return ''
