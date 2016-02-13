import urllib, re, urllib2


sourceSite = 'http://bvls2016.sc/'

def GetHTML(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link


def GetStream(streamlink):
    streamhtml = GetHTML(streamlink)
    streamjs = re.compile('<script type="text/javascript"><!--(.*?)--></script>', re.DOTALL | re.IGNORECASE).findall(streamhtml)[0]
    cipher = re.compile(r'\w{4}="(.*?)",', re.DOTALL | re.IGNORECASE).findall(streamjs)[0]
    enctext = re.compile(r'\}\w{4}\("(.*?)"\);', re.DOTALL | re.IGNORECASE).findall(streamjs)[0]
    decrypted = decryptbvls(cipher, enctext)
    iframesrc = re.compile('id\=\"iframe\" allowfullscreen\=\"true\" src\=\"(.*?)\"\ ', re.DOTALL | re.IGNORECASE).findall(decrypted)[0]
    return iframesrc


def decryptbvls(a, b):
    a = a.replace('\\"','"')
    b = b.replace('\\"','"')
    alength = len(a)
    blength = len(b)
    i = 0
    dectext = ""
    while i < blength:
        bchar = urllib.unquote(b[i])
        aindex = a.find(bchar)
        if (aindex > -1):
            aindex -= (i + 1) % alength
            if (aindex < 0):
                aindex += alength
            dectext = dectext + urllib.unquote(a[aindex])
        else:
            dectext = dectext + bchar
        i += 1
    return dectext
