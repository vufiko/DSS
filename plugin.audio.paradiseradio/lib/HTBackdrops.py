import urllib2
import re
import common

ROOT   = 'http://htbackdrops.org/api/'
API    = '96d681ea0dcb07ad9d27a347e64b652a'
SEARCH = ROOT + API + '/searchXML?inc=images&default_operator=and&keywords='
NAME   = 'HTBackdrops'


def GetImages(artist):
    if artist == '':
        return []

    artist = artist.upper().replace(' & ',' ').replace(',','+').replace('(','').replace(')','').replace(' ','+')
    artist = artist.replace('++', '+')

    try:
        url = SEARCH + artist#.replace('+', ' ')

        images = []

        #print NAME + ' 1st URL requested: %s' % url           
        link = common.GetHTML(url)

        match = re.compile('<id>(.+?)</id>').findall(link)

        for id in match:
            img = ROOT + API + '/download/' + id  + '/fullsize'
            images.append(img)

    except Exception, e:
        pass

    #print NAME + ' Found - %d images' % len(images)
    return images