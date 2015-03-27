import os
import time
import glob
import urllib2

gCacheDir = ""
gCacheSize = 100



def SetCacheDir(cacheDir):
    global gCacheDir
    gCacheDir = cacheDir
    if not os.path.isdir(gCacheDir):
        os.makedirs(gCacheDir)


def CheckCacheDir():
    if gCacheDir == '':
        raise Exception('CacheDir not defined')


def GetURLNoCache(url, referer=None):
    response = None
    html = ''

    try:
        req = urllib2.Request(url)

        if referer:
            req.add_header('Referer', referer)

        response = urllib2.urlopen(req, timeout=10)
        html     = response.read()
    except Exception, e:
        pass

    if response:
        response.close()

    return html


def GetURL(url, maxSecs = 0, referer=None):        
    if url == None:
        return None

    CheckCacheDir()
    if maxSecs > 0:
        #is URL cached?
	cachedURLTimestamp = CacheGetURLTimestamp(url)
	if cachedURLTimestamp > 0:
	    if (time.time() - cachedURLTimestamp) <= maxSecs:
		return CacheGetData(url)

    data = GetURLNoCache(url, referer)
    CacheAdd(url, data)    
    return data


def CacheGetURLTimestamp(url):
    cacheKey          = CacheCreateKey(url)
    cacheFileFullPath = os.path.join(gCacheDir, cacheKey)

    if os.path.isfile(cacheFileFullPath):
        return os.path.getmtime(cacheFileFullPath)

    return 0


def CacheGetData(url):
    cacheKey          = CacheCreateKey(url)
    cacheFileFullPath = os.path.join(gCacheDir, cacheKey)
    f                 = file(cacheFileFullPath, "r")

    data = f.read()
    f.close()

    return data


def CacheAdd(url, data):
    cacheKey          = CacheCreateKey(url)
    cacheFileFullPath = os.path.join(gCacheDir, cacheKey)
    f                 = file(cacheFileFullPath, "w")

    f.write(data)
    f.close()

    CacheTrim()


def CacheCreateKey(url):
    try:
        from hashlib import md5
        return md5(url).hexdigest()
    except:
        import md5
        return md5.new(url).hexdigest()


def CacheTrim():

    files  = glob.glob(os.path.join(gCacheDir, '*'))
    nFiles = len(files)

    try:
        while nFiles > gCacheSize:            
            #if len(files) <= gCacheSize:
            #    return

            oldestFile        = GetOldestFile(files)
            cacheFileFullPath = os.path.join(gCacheDir, oldestFile)
 
            while os.path.exists(cacheFileFullPath):
                os.remove(cacheFileFullPath)

            files  = glob.glob(os.path.join(gCacheDir, '*'))
            nFiles = len(files)
    except:
        pass


def GetOldestFile(files):
    if not files:
        return None
    
    now    = time.time()
    oldest = files[0], now - os.path.getctime(files[0])

    for f in files[1:]:
        age = now - os.path.getctime(f)
        if age > oldest[1]:
            oldest = f, age

    return oldest[0]
